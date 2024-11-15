people = ['frank','ben','joe','rick']

for i in people:
    if i == 'joe':
       break
    print(i)

for i in people:
    if i == 'ben':
        continue
    print(i)
    
for i in people:
    if i == 'ben':
        pass
    print(i)
