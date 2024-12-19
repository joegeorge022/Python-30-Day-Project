def greet(name):
    
    def message():
        return "How u doin :)!"

    return f"Sup, {name}. {message()}"
name=input("Enter you name:")
print(greet(name))


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

a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
results = calculator(a,b)
print("Addition:", results["add"])        
print("Subtraction:", results["subtract"]) 
print("Multiplication:", results["multiply"])
print("Division:", results["divide"])    