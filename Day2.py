# Answer 1

print("Answer 1")
lst=[]
print("Enter 10 no. ")
for i in range(10):
    n=int(input())
    if n%2==0:
        lst.append(n)
print(lst)
print("\n--------------------------------------------")

# Answer 2

print("Answer 2")

print("LIST COMPREHENSION",end="\n\n")
print("List comprehensions are used for creating new lists from other iterables.\nAs list comprehensions return lists, they consist of brackets containing \nthe expression, which is executed for each element along with the for \nloop to iterate over each element.")
print("\n\nFor example: Iterating through a string Using for Loop\n")
print("h_letters = []\n\nfor letter in 'human':\n    h_letters.append(letter)\n\nprint(h_letters)")
print("\nOUTPUT: ['h', 'u', 'm', 'a', 'n']",end="\n\n")
print("\nIterating through a string Using List Comprehension")
print("h_letters = [ letter for letter in 'human' ]\nprint( h_letters)")
print("\nOUTPUT: ['h', 'u', 'm', 'a', 'n']",end="\n\n")

print("\n--------------------------------------------")

# Answer 3

print("Answer 3")
d={}
n=int(input("Input: "))
d={i:i*i for i in range(1,n+1)}
print(d)

print("\n--------------------------------------------")


# Answer 4

print("Answer 4")
initial_x = 0
initial_y = 0
up=0
left=0
right=0
down=0
print("direcctions are in same order as given in question.")
lst=["UP: ", "DOWN: " , "LEFT: ", "RIGHT: "]
no_of_directions = int(input())
for i in range(no_of_directions):
    print(lst[i], end=" ")
    if i==0:
        up=int(input())
    if i==1:
        down=int(input())
    if i==2:
        left=int(input())
    if i==3:
        right=int(input())
if right>left:
    final_x = right-left
else:
    final_x = left-right

if up>down:
    final_y = up-down
else:
    final_y = down-up

temp = pow(final_y,2) + pow(final_x,2)

no_of_steps = pow(temp,0.5)

if type(no_of_steps)==float:
    no_of_steps = round(no_of_steps)
    no_of_steps = int(no_of_steps)
    
print(no_of_steps)
print("\n--------------------------------------------")




















