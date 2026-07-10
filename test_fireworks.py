from services.fireworks_client import ask_llm

response = ask_llm(
    "In one sentence, explain what a startup is."
)

print(response)