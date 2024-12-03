'''
Name:Joe George
Title: Greatest Common Divisor.
Date: 3 December 2024
'''

# Greatest Common Divisor
def gcd(a,b):
    if a % b==0:
        return b
    else:
        return gcd(b,a%b)

print(gcd(12,16))

