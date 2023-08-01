
print("Hello world!")
print(100)

n,m = 0, "abc"

print(m)

#if statements

n = 1
if n>2:
    n-=1
elif n == 2:
    n*=2
else:
    n=0

print(n)

#parentheses needed for muli-line conditions.
# and = &&
# or = ||

n,m = 1, 2
if((n > 2 and n != m) or n == m):
    n += 1

#while loops are similar
n=0
while n< 5:
    print(n)
    n = n+1

#for loop
for i in range(5):
    print(i)

for i in range(2,6): # starting at 2 and going to six but not 6
    print(i)

for i in range(5, 1, -1): # decrement by 1 going 5 down to 2
    print(i)

#division is decimal by default
print(5/2)

#doubl slash rounds down
print(5//2)

# most languages round towards 0 by default so negative numbers will round down
print(-3//2)

#A workaround for rounding towards zero is to use decimal division and then convert to int.
print(int(-3/2))

#modding 
print(10 %3)

#except for negative values
print(-10 % 3)

#to be consistent with other languages
import math 
print(math.fmod(-10,3))

#more math helpers
print(math.floor(3/2))
print(math.ceil(3/2))
print(math.sqrt(2))
print(math.pow(2,3))

# Max/ Min Int
float("inf")
float("-inf")
 #python  numbers are infinite so they never overflow
import math
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2,200) < float("inf"))

# Arrays (called lists in python)
arr = [1,2,3]
print(arr)

#can be uses as a stack
arr.append(4)
arr.append(5)
print(arr)

arr.pop()
print(arr)
arr.insert(2,7)
print(arr)

arr[0] = 0
arr[3] = 0
print(arr)

#initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print(arr)
print(len(arr))

#careful: -1 is not out of bounds, its the last value
arr = [1,2,3]
print(arr[-1])
#indexing -2 is the seconds to last value
print(arr[-2])

#sublists (aka slicing)
arr = [1,2,3,4]
print(arr[1:3])

#unpacking
a, b, c  = [1, 2, 3]
print(a,b,c)

# loop through arrays
nums = [1, 2, 3]
#using index
for i in range(len(nums)):
    print(nums[i])

#without index





