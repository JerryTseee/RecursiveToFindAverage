"""
Given an array of numbers, use a recursive algoritm to find the average of all
numbers in the array.
"""

def avg(a):
    length = len(a)
    if length == 1:
        return a[0]
    else:
        mid = length//2
        return ((avg(a[:mid])*mid)+(avg(a[mid:])*(length-mid)))/length
    
print(avg([1,2,3]))
