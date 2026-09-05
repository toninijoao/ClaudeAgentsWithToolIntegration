import json
from anthropic import Anthropic
from functions import sum_numbers, multiply_numbers

client = Anthropic()

tools = {
    "sum_numbers": sum_numbers,
    "multiply_numbers": multiply_numbers
}

model="claude-sonnet-4-6"

system_prompt = (
    "You are a helpful math assistant."
    "Always use the available tools to perform calculations accurately."
)

with open('schemas.json', 'r') as f:
    tool_schemas = json.load(f)

messages = [
    {"role": "user",
     "content": "Please calculate 15 + 27"
     }
]

response = client.messages.create(
    model=model,
    max_tokens=2000,
    messages = messages,
    system=system_prompt,
    tools=tool_schemas.
)

messages.append({
    "role": "user",
    "content": response.content
})

if response.stop_reason == "tool_use":
    tool_results = []

    for content_item in response.content:
        if content_item.type == "tool_use":
            tool_name = content_item.name
            tool_input = content_item.input
            tool_id = content_item.id

            print(f"Executing: {tool_name}({tool_input})")


if response.stop_reason == "tool_use":
    tool_results = []
    
    for content_item in response.content:
        if content_item.type == "tool_use":
            
            try:
            except Exception as e:
                # Handle errors...
            
            print(f"Result: {result}")
            
            tool_results.append({
                "type": "tool_result",         
                "tool_use_id": tool_id,        
                "content": str(result)         
            })

    messages.append({
        "role": "user",                        
        "content": tool_results                
    })

    final_response = client.messages.create(
        model=model,
        max_tokens=2000,
        messages=messages,
        system=system_prompt,
        tools=tool_schemas
    )

    messages.append({
        "role": "assistant",
        "content": final_response.content
    })

    print("\nClaude's final response: ")
    print(final_response.content[0].text)

print("Messages history: ")

for i, message in enumerate(messages):
    print(f"\nMessage {i+1} - Role: {message['role']}")

    if isinstance(message['content'], str):
        print(f"content: {message['content']}")
    else:
        for j, content in enumerate(message['content']):
            print(f"content {j+1}: {content}")