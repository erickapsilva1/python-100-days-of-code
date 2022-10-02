height = float(input('enter your height in m: '))
weight = float(input('enter your weight in kg: '))

bmi = weight / (height ** 2)
bmi = round(bmi, 2)

print(bmi)

if bmi < 16.0:
    print('Underweight (Severe thinness)')
elif bmi >= 16.0 and bmi <= 16.9:
    print('Underweight (Moderate thinness)')
elif bmi >= 17.0 and bmi <= 18.4:
    print('Underweight (Mild thinness)')
elif bmi >= 18.5 and bmi <= 24.9:
    print('Normal range')
elif bmi >= 25.0 and bmi <= 29.9:
    print('Overweight (Pre-obese)')
elif bmi >= 30.0 and bmi <= 34.9:
    print('Obese (Class I)')
elif bmi >= 35.0 and bmi <= 39.9:
    print('Obese (Class II)')
else:
    print('Obese (Class III)')

