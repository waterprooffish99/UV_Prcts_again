from dotenv import load_dotenv
import os
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv()
gemini_api_key=os.getenv("GEMINI_API_KEY")

# Check if the Api key is present, if not raise an error.
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

agent = Agent(
    name = "Translator",
    instructions = "You are a helpful translator.Always translate english sentences into urdu."
)

response = Runner.run_sync(
    agent,
    input = "My Teacher Name is Sir Aneeq. He is teaching us Agentic AI. He is one of the best Teacher I am taught by.",
    run_config = config
)

print(response)