from smolagents import CodeAgent, TransformersModel, DuckDuckGoSearchTool

'''
- device = "cpu" for CPU usage
- device = "cuda" for GPU usage (requires PyTorch with CUDA support and a compatible NVIDIA GPU)
- device = torch_directml.device() for DirectML GPU usage (DML support is experimental and may require additional setup for directX 12 compatible GPUs on Windows)
'''
device = "cpu"

model = TransformersModel(
    model_id="HuggingFaceTB/SmolLM2-1.7B-Instruct",  # or another model
    device=device
)
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
)

# Now the agent can search the web!
result = agent.run("What is the current weather in Paris?")
print(result)
