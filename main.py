






#Arithmetic operations
#+ , _ , * , % , / , //
 


Remote = 2000
Yea = 3700

monthly_salary = 2000 + 3700 
print(monthly_salary)

expenses = 370 + 800 + 200 + 450 + 200 
print(expenses )

total_expenses = 3700 - 2020
print(total_expenses)

remaining = 2000 + 1680 
print(remaining)


total_expenses = 5700 - 3680 
print(total_expenses)



Yea = 3700
remote = 2400

total_salary = 3700  * 2400 
print(total_salary )

total_net = 2400 + 3700
print(total_net)

net = 6100 * 12
print(net)

base_salary = 73200 / 12 
print(base_salary)
 
#floor division 
base_salary = 73200 // 12
print(base_salary)


#The asignment operator
#equal to operator  =

#+= 
#-=
#/=
#// =
#*=


# control flow AND conditional statement AND comprisms operator 
 #== , != , > , < , >= , <= , using in creating if blcok 
 # control flow refers to the order in which our code get executed  

expenses = 2020
pay = 6100

if pay > expenses : 
   print('You are the best')
else :
  print('More room for improvement')  

#Assignment

name = input('what is your name ')
print(name)

age = input('what is your age')
print(age)

print(f'Hello {name} ! it is great to meet a {age} year old programer !')


name = input ('what is your name ')
print(name)

age = input ('what is your age')
print(age)


print(f'Hello {name} ! ,it is great to meet a {age} year old programer !')



# Question
#Since you've mastered basic input/output and variables, let's add conditional statements to the mix!

#Goal: Create a program that asks for the user's birth year and calculates their age, then tells them if they're a minor or an adult.

current_year = 2024

birth_year = int(input('what is your birth_year '))

age = current_year-birth_year

if age >= 18 :
         print('You are an aldut')
else :
        print('You are a minor')




# Assignment 2 
#Create a program that asks for the user's birth year AND current year, then provides more detailed age categorization.

# solution .

current_year = 2024

birth_year = int(input('what is your birth_year '))

age = current_year - birth_year
print(age)

if age < 13 :
     print('You are a Child')

elif age >= 13 and age <= 17 :
     print('You are a teen ')

elif age >=18 and age <= 64 : 
     print('You are an Adult')

else :
    print('You are a senior ')
     
# Questions 

#Create a program that asks for the user's age and calculates their movie ticket price with different categories.

age = int(input('what is your age'))

if age <= 13 :
     print(' You will pay the child price 8$')

elif  age <= 17 :
     print('You will pay Teen price 12$')

elif age <= 64 :
     print('You will pay Adult price 15$')


else :
     print('You are a senior you will pay 10$')