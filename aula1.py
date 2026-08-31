import json
from functions import sum_numbers, multiply_numbers

with open('aula1schemas.json', 'r') as f:
    tool_schemas = json.load(f)

tools = {
    "sum_numbers": sum_numbers,
    "multiply_numbers": multiply_numbers
}

print(json.dumps(tool_schemas, indent=2))

result1 = tools['sum_numbers'](10, 5)
print(f"sum_numbers(10, 5) = {result1}")

result2 = tools['multiply_numbers'](4, 7)
print(f"multiply_numbers(4, 7) = {result2}")

def sum_numbers(a:float, b:float) -> float:
    """
    Sum two numbers and return the result.

    Args:
    a (float): First number to add
    b (float): Second number to add

    Returns:
        float: The sum of a and b
    """
    return a + b

def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers and return the result.

    Args:
    a (float): First number to multiply
    b (float): Second number to multiply

    Returns:
    float: The product of a and b
    """
    return a * b