from anthropic import Anthropic
import json

client = Anthropic()
system_prompt = (
    "You are a helpful math assistant. "
    "When performing calculations, use the availables tools for accuracy."
)

with open('aula2schemas.json', 'r') as f:
    tool_schemas = json.load(f)

messages = [
    {"role": "user", "content": "Please calculate 15 + 27"}
]

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=2000,
    messages=messages,
    system_prompt=system_prompt,
    tools=tools_schemas
)

print(json.dumps(response.model_dump(), indent=2))

print(f"Stop Reason: {response.stop_reason}")

system_prompt = (
    "You are a helpful math assistant. "
    "When performing calculations, use the availables tools for accuracy."
)

for i, content_item in enumerate(response.content):
    print(f"\nContent Item {i+1}: ")
    print(f"Type: {content_item.type}")

    if content_item.type == "text":
        print(f"Text: {content_item.text}")
    elif content_item.type == "tool_use":
        print(f"Tool name: {content_item.name}")
        print(f"Tool input: {content_item.input}")
        print(f"Tool id: {content_item.id}")