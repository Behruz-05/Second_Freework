name = input("Enter your name: ")
age = int(input("Enter the year you were born: "))

print(f"Hello", name,"!", "You are", 2026 - age, "years old")


randomnumber = int(input("Enter a random number: "))
if randomnumber % 2 == 0:
    print(f"{randomnumber} is even")
else: print(f"{randomnumber} is odd")


numbers = [12, 32, 42, 55, 10, 41, 50, 70, 35]
numbers.sort()
for num in numbers:
    if num % 5 == 0:
        print(num)
