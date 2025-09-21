print("Welcome to Body Mass Index Calculator")
# the function below accepts standard metric unit as kg and meter
def metric(weight,height):
    index=weight/(height)**2
    if index<18.5:
        return(f'{round(index,1)}:you are underweight')
    elif (18.5<=index<=24.9):
        return(f'{round(index,1)}:you have a normal weight')
    elif (25<=index<=29.9):
        return(f'{round(index,1)}:you are overweight')
    elif (30<=index<=34.9):
        return(f'{round(index,1)}:you have class1 obesity')
    elif (35<=index<=39.9):
        return(f'{round(index,1)}:you have class2 obesity')
    elif index>=40:
        return(f'{round(index,1)}:you have class3 obesity')
# the function below accepts imperial units such as pounds and inches
def imperial(weight1,height1):
    index1=(weight1/(height1)**2)*703
# below shows the BMI weight category
    if index1<18.5:
        return(f'{round(index1,1)}:you are underweight')
    elif (18.5<=index1<=24.9):
        return(f'{round(index1,1)}:you have a normal weight')
    elif (25<=index1<=29.9):
        return(f'{round(index1,1)}:you are overweight')
    elif (30<=index1<=34.9):
        return(f'{round(index1,1)}:you have class1 obesity')
    elif (35<=index1<=39.9):
        return(f'{round(index1,1)}:you have class2 obesity')
    elif index1>=40:
        return(f'{round(index1,1)}:you have class3 obesity')

weight=int(input('Enter weight in kg: '))
height=float(input('Enter height in m: '))
index2=metric(weight,height)

weight1=int(input('Enter weight in lbs: '))
height1=int(input('Enter height in inches: '))
index3=imperial(weight1,height1)  
for i in range(2):
    choice=input('choose an option 0-1: ')
    if choice == '0':
        print(index2)
    elif choice == '1':
        print(index3)
    else:
        print('invalid selection')