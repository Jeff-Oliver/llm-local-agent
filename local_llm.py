import os

# Ensure oneDNN optimizations are disabled for this process.
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch_directml
print("Dependencies loaded successfully, now loading the model...")

# Define the model checkpoint to load. You can replace this with any compatible model checkpoint from Hugging Face or your local directory.
checkpoint = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
print("Model loaded successfully, now running inference...")

'''
- device = "cpu" # for CPU usage
- device = "cuda" # for GPU usage (requires PyTorch with CUDA support and a compatible NVIDIA GPU)
- device = torch_directml.device() # for DirectML GPU usage (DML support is experimental and may require additional setup for DirectX 12 compatible GPUs on Windows)
'''
device = torch_directml.device()

print(f"Using device: {device}")

tokenizer = AutoTokenizer.from_pretrained(checkpoint)

if tokenizer.pad_token is None:
    tokenizer.add_special_tokens({"pad_token": "<|pad|>"})
    model = AutoModelForCausalLM.from_pretrained(checkpoint)
    model.resize_token_embeddings(len(tokenizer))
else:
    model = AutoModelForCausalLM.from_pretrained(checkpoint)

# Set the model's padding token ID to match the tokenizer so padding is handled consistently during generation.
model.config.pad_token_id = tokenizer.pad_token_id
# Set the model's end-of-sequence token ID to match the tokenizer so generation can stop at the correct EOS (end of sequence) token.
model.config.eos_token_id = tokenizer.eos_token_id

# Move the model to the specified device
model = model.to(device)

messages = [{"role": "user",
             "content": "What is the capital of France."
             }]

input_text = tokenizer.apply_chat_template(messages, tokenize=False)

inputs = tokenizer(input_text, return_tensors="pt", padding=True)
inputs = {key: value.to(device) for key, value in inputs.items()}

outputs = model.generate(
    inputs["input_ids"],
    attention_mask=inputs.get("attention_mask"),
    max_new_tokens=50,
    temperature=0.2,
    top_p=0.9,
    do_sample=True,
)

print(tokenizer.decode(outputs[0]))
