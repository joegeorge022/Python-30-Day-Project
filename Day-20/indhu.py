def calculator(a, b):
    def add():
        return a + b

    def subtract():
        return a - b

    def multiply():
        return a * b

    def divide():
        return a / b if b != 0 else "Division by zero!"

    return {
        "add": add(),
        "subtract": subtract(),
        "multiply": multiply(),
        "divide": divide()
    }

results = calculator(8, 3)
print("Addition:",results["add"])       
print("Subtraction:",results["subtract"]) 
print("Multiplication:",results["multiply"])
print("Division:", results["divide"])


def updated_numbers(numbers):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    results = {"squares": [], "cubes": []}
    for num in numbers:
        results["squares"].append(square(num))
        results["cubes"].append(cube(num))

    return results

numbers = [15, 25, 35, 45]
updated =updated_numbers(numbers)
print("Squares:",updated["squares"]) 
print("Cubes:", updated["cubes"])

def power(exponent):
    def calculate(base):
        return base ** exponent

    return calculate

square = power(2)  

cube = power(3)   

print(square(5))  
print(cube(7))