print("Hello world")

#writing my day three code below here
    #Can u ride in Costa Rica
print("Welcome to the roller-costa-rica!")
height = int(input("What is your height in centimeter? "))
if height >= 120:
    print("You can ride the roller-costa-rica")
else:
    print("Sorry Mr/Mrs Dwarf, you have to grow taller before you can ride.")

    #Modulo Operation 
number = int(input("Which number you wan check?"))
if number % 2 == 0:
    print("This is an even number")
else:
    print("This is an odd number")

#BMI 2.0
bmi = 28
if bmi < 18.5:
    print(f"Your BMI is {bmi},you are underweight")
elif bmi<25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically Obese.")
