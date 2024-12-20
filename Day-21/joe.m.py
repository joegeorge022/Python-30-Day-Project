"""
AUTHOR : JOE MARTIN RINCE
"""


original = "  Hello, Python!  "


length = len(original)


lowercase = original.lower()


uppercase = original.upper()


stripped = original.strip()


replaced = stripped.replace("Python", "World")


find_python = stripped.find("Python")


split_by_comma = stripped.split(",")


is_numeric = "123".isnumeric()


name = "John"
formatted_string = f"Welcome, {name}!"


print("Original string:", repr(original))
print("Length of string:", length)
print("Lowercase:", repr(lowercase))
print("Uppercase:", repr(uppercase))
print("Stripped:", repr(stripped))
print('Replaced "Python" with "World":', repr(replaced))
print('Find "Python":', find_python)
print("Split by ',':", split_by_comma)
print('Is "123" numeric?:', is_numeric)
print("Formatted string:", repr(formatted_string))
