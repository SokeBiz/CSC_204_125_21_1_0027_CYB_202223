print("Hello world")

#writing my day two code below here
num = input("Enter any two digit number:")
first = int(num[0])
second = int(num[1])
sum = first + second
print(sum)

#calculate body mass index
weight = int(input("Enter your weight in kilograms:"))
height = float(input("Enter your height in metres:"))
square_height = height ** 2
bmi = int(weight / square_height)
print("Your Body Mass Index is ", bmi)

print(round(19 / 3, 3))

# calculate if u go die young
age = input("What is your age?")
years = 90 - int(age)
days = 365 *  int(years)
weeks = 52 * int(years)
months = 12 * int(years)
print(f"You have {days} days, {weeks} weeks and {months} months left ")

#tip calculator 
print("Tip Calculator")
total = float(input("What was the total bill? #"))
percentage = int(input("What percentage would you like to give? 5, 10 or 15? "))
people = int(input("How many people are to split the bill? "))
percentage_converted = percentage / 100 * total + total
each = round(percentage_converted / people, 2)
print("Each person should pay #",each)

