#Mutation
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string

def count_substring(string, sub_string):
    count=0
    #for j in range (0, len(sub_string)):
    for i in range (len(string)):
        if string[i:i+(len(sub_string))]==sub_string:
            count +=1
    return count


def string_validator(string):

    for i in s:
        if i.isalnum() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isalpha() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isdigit() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.islower() == True:
            print("True")
            break
    else:
        print("False")

    for i in s:
        if i.isupper() == True:
            print("True")
            break
    else:
        print("False")


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


from itertools import product
def iter():
    A = (map(int, input().split()))
    B = list(map(int, input().split()))
    mylist = []
    mylist = (list(product(A, B)))

    print(*[tuple(map(int, t)) for t in mylist])


from itertools import permutations

A = input()
myList = []
num = 0
for i in A:
    if i.isalpha():
        myList.append(i)
    elif i.isnumeric():
        num = int(i)

# print(myList)
# array = [(x) for x in input().split()]
B = list(permutations(myList, num))
C = sorted(B)
for j in C:
    c = ''.join(j)
    print(c)




from itertools import combinations
io = input().split()
S = io[0]
k = int(io[1])

for j in range(1, k + 1):
    for j in combinations(sorted(S), j):
        print(''.join(j))


def print_full_name(first, last):
    print('Hello', first, last+'! You just delved into python.' )

def split_and_join(line):
    # write your code here
    a = line.split(" ")
    ab = "-".join(a)
    return ab


def swap_case(s):
    A=[]
    for i in s:
        if i.islower():
            A.append(i.upper())
        elif i.isupper:
            A.append(i.lower())
    str1 = ''.join(A)
    return str1



import calendar
A = input().split()
B = calendar.weekday(int(A[2]),int(A[0]), int(A[1]))
if B == 0:
    print('MONDAY')
elif B==1:
    print('TUEDSAY')
elif B==2:
    print('WEDNESDAY')
elif B==3:
    print('THURSDAY')
elif B==4:
    print('FRIDAY')
elif B==5:
    print('SATURDAY')
elif B == 6:
    print('SUNDAY')
