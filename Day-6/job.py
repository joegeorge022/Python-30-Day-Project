"""Author :Job Thomas Cherian
Date:13/11/24"""

film = ["Avengers", "infinity", "war"]
print("Name of the film is",film[0])
film.append(2018)
year=film[-1]
print("the film is produced on",year)
film.remove("Avengers")
print(film)
print(f"length of the list is {len(film)}")
