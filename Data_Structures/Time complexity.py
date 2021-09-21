def get_squared_number(numbers):
    squared_numbers=[]
    for n in numbers:
        squared_numbers.append(n*n)
    return print(squared_numbers)

numbers=[2,5,6,8]
get_squared_number(numbers)

#Big O used to calculate the running time

"""
time= a*n+b
--> Keep the faster growing term i.e a*n
--> Drop Constant i.e a
= O(n)
"""

# order of one complexity
# O(1)

def find_first(prices,eps,index):
    pe=prices[index]/eps[index]
    return pe

#time = a*n^2+b =O(n^2)

n=[3,6,2,4,3,6,8,9]
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]==n[j]:
            print(str(n[i]) + " is duplicate")
            break
