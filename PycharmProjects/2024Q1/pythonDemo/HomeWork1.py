#   1


start_point = 0
for numbers in range(1, 10, 2):
    start_point = numbers + 1
    print(f"The even number is {start_point}, and the odd number is {numbers}")


  # 2

correct_password = "Naseem2Cool"

attempts = 0

max_attempts = 3

while attempts < max_attempts:
    password = input("Enter the password: ")

    if password == correct_password:
        print("Login successful")
        break

    attempts += 1 # attemtps = attemtpts + 1

    if attempts == max_attempts:
        print("You attempted 3 times and failed. Please try again later.")
    else:
        print(f"Wrong password. Please try again. Attempts left: {max_attempts - attempts}")




   # 3

 # Fist way
lst = [1, 2, 3, 4, 5]

for item in lst:
    print(item)

print(lst)

print('*')
print('**')
print('***')
print('****')
print('*****')

# Second way
print('-------------------------------------------')

num = 25

for i in range(num):
    print(i * '*')

# Third way
print('-------------------------------------------')

for i in reversed(range(num)):
    print(i * '*')





