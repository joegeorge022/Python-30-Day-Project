# QUESTION 1
def greet(name):
    def message():
        return "Merry Christmas!"

    return f"Hello, {name} \n{message()}"

print(greet("Sarju Sir"))




# QUESTION 2
def nums(numbers):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    results = {"squares": [], "cubes": []}
    for i in numbers:
        results["squares"].append(square(i))
        results["cubes"].append(cube(i))

    return results

numbers = [1, 2, 3, 4,5]
processed = nums(numbers)
print("Squares:", processed["squares"])
print("Cubes:", processed["cubes"])
