# dz2_AbyzovAA.py

# Task 1
print("\n\t\tTask 1")
import random

list1 = []
for i in range (0, 15):
    list1.append(random.randint(1, 30))

print("Your randomly generated list:\n", list1)

list2 = []
i = 0
while i < len(list1):
    if list1[i] > 10 and list1[i] < 20:
        list2.append(list1[i])
    i+=1

print("Your filtered list:\n", list2)


# Task 2 (*)
print("\n\t\tTask 2")
list3 = []
for i in range (0, 10):
    list3.append(random.randint(-5, 5))

print("Your randomly generated list:\n", list3)

list4 =[]
for i in range (0, len(list3)):
    if list3[i] > 0:
        flag = True
        for j in range (0, len(list3)):
            if list3[i] == list3[j] and i != j:
                flag = False
        if flag:
            list4.append(list3[i])
    else:
        list4.append(list3[i])

print("Your filtered list:\n", list4)


# Task 3 (**)
print("\n\t\tTask 3\nPlease enter your numbers or 'end'")

list5 = []

inp = ""
while inp != "end":
    inp = input(">>> ")
    if inp != "end":
        list5.append(inp)

print("Your original list:\n", list5)

bigest = int(list5[0])
bigestid = 0
for i in range (0, len(list5)):
    if int(list5[i]) > bigest:
        bigest = int(list5[i])
        bigestid = i

if bigestid != 0:
    big = int(list5[0])
else:
    big = int(list5[1])

for j in range (0, len(list5)):
    if int(list5[j]) > big and j != bigestid:
        big = int(list5[j])

print("Your second largest number is: ", big)