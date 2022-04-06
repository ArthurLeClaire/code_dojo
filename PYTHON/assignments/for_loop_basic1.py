for i in range(151):
    print(i)
for i in range(5, 1001, 5):
    print(i)

for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

min = 0
max = 500000
Oddtotal = 0

for number in range(min, max+1):
    if(number % 2 != 0):
        Oddtotal += number

print(f"the sum of odd numbers from {min} to {max} = {Oddtotal}")

# number = 2018
# while number > 0:
#     print(number)
#     number -= 4

for i in range(2018, 0, -4):
    print(i)

low = 2
high = 9
multi = 3


def flex(low, high, multi):
    for i in range(low, high):
        if i % multi == 0:
            print(i)

# flex(2,9,3)
