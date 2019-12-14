#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n) -- linear (grows in direct proportion of the input size)


b) O(n log n) -- logarithmic 


c) O(n) -- linear (grows in direct proportion of the input size)

## Exercise II
_____________
|           |
|           |
|           | <===> Start in the middle
|           |
|___________|


1. Start in the middle of the building (Binary search)
2. If the egg DOES break:
    - then we know floor F is less than the middle of the building.
    - So we would continue one floor down from the middle until we find floor F
3. If the egg DOESN'T break, we know the floor F is higher than the middle of the building.
    - Then we would continue one floor up from the middle until we find floor F

Perhaps O(logN) because 1/2 time