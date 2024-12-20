
dict1 = {
    "name":"Joe",
    "status":"alive",
    "age":18,
    "profession":"engineer",
    "location":"Kottayam"
}

print(dict1)
print(dict1.keys())
print(dict1.values())
print(dict1.items())

dict2 = {
    "name":"Better Joe",
    "status":"alive",
    "age":24,
    "profession":"asset manager",
    "location":"New York"
}

dict1.update(dict2)
print(dict1)

dict3 = {
    "name":"Happy Joe",
    "status":"alive",
    "age":40,
    "profession":"retired",
    "location":"Switzerland"
}


dict3.pop("age")
print(dict3)


dict1.clear()
dict2.clear()

print(dict2,dict1)

dict4 = {
    "name":"Joe",
    "age":41,
    "status":"dead",
    "profession":"none",
    "location":"unknown"
}

print(dict4)
