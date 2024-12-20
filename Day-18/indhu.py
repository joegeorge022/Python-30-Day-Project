grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in grid:
	 for element in row:
	 	print(element,end=" ")
	 
n=10

for i in range(1,n+1):
	  for j in range(i):
	  	  print("*",end=" ")
	  print( )
	  
for i in range (1,6):
	  for j in range(1,6):
	  	  print(f"{i* j:2}",end=" ")
	  print( )
	  
words=["hello","python"]
letter_counts={}

for word in words:
	  for letter in word:
	  	  if letter in letter_counts:
	  	  	letter_counts[letter]+=1
	  	  else:
	  	  	letter_counts[letter]=1
print("Letter Counts:",letter_counts)
