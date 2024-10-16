print("We will find your body mass and tell you if you're overweight,slim,obese,or skinny\n")
print("Please type your height and weight")
x=int(input('Your height in inches: '))
y=int(input('Your weight in pounds: '))
x = x*2.54
BMI=y/x
print("Your BMI is " + str(BMI))
if .95>BMI>.85:
    print("You are overweight")
    print("Start dieting and include aerobic exercises in your daily workouts\n")
if BMI>.95:
    print("You are obese")
    print("You should go see a bariatric physician and discuss plans for weight loss\n")
if .85>BMI>.70:
    print("You are slim")
    print("Continue your current diet and exercise regimen")
if BMI<.70:
    print("You are skinny")
    print("Try working out more and building muscle")
print("We will find your body mass and tell you if you're overweight,slim,obese,or skinny\n")
print("Please type your height and weight")
x=int(input('Your height in inches: '))
y=int(input('Your weight in pounds: '))
x = x*2.54
BMI=y/x
print("Your BMI is " + str(BMI))
if .95>BMI>.85:
    print("You are overweight")
    print("Start dieting and include aerobic exercises in your daily workouts\n")
if BMI>.95:
    print("You are obese")
