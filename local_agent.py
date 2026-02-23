# Ensure oneDNN optimizations are disabled for this process.
import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

from smolagents import CodeAgent, TransformersModel, DuckDuckGoSearchTool
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch_directml
print("Dependencies loaded successfully, now defining checkpoint...")

# Define the model checkpoint to load. You can replace this with any compatible model checkpoint from Hugging Face or your local directory.
checkpoint = "HuggingFaceTB/SmolLM2-1.7B-Instruct"
print("Checkpoint loaded successfully, now setting device...")

'''
- device = "cpu" for CPU usage
- device = "cuda" for GPU usage (requires PyTorch with CUDA support and a compatible NVIDIA GPU)
- device = torch_directml.device() for DirectML GPU usage (DML support is experimental and may require additional setup for directX 12 compatible GPUs on Windows)
'''
device = "cpu"

print(f"Using device: {device}, now loading the model...")

model = TransformersModel(
    model_id=checkpoint,
    device=device
)
print("Model loaded successfully, now creating the agent...")

agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
)
print("Agent created successfully, now running the agent...")

# Now the agent can search the web!
result = agent.run("What is the current weather in Paris?")
print(result)
