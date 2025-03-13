# 1. Print: Hello World
print("Hello World of programmers!!!")

# 2. Write an if statement
n = 1
if n == 1:
    print("First if statement in Python!")

# 3. Write a while loop
n = 2
while n > 0:
    print("Printing while N is bigger than 0: " + str(n))
    n-=1
# 4. Write a for loop
n = 3
for i in range(int(n)):
    print("Printing from 0 to N: " + str(i))

# reversed for loop
for i in range(int(n)-1, -1, -1):
    print("Printing from N to 0: " + str(i))

# 5. Check the data type of a variable
s = "what's up???"
print(type(s))
f = 13.2
print(type(f))
g = True
print(type(g))

# 6. Functions
def function():
    print("Hello World of function!")
function()
# sums 2 numbers
def sum(a,b):
    return a + b
print(sum(1.1,2))
# check for a palindrome
def palindrome(a):
    b = a
    c = False
    for i in range(len(a)-1, -1,-1):
        if b[i] == a[i]:
            c = True
        else:
            c = False

    return c
print(palindrome('ana'))
print(palindrome('madam'))
print(palindrome("racecar"))