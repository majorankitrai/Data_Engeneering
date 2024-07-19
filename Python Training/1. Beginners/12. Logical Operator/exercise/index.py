age = int(input("enter your age :"))
grade = int(input("enter your grade :"))
if age >= 18 and grade >= 60:
    print("You got scholarship")
elif age < 18:
    print("Your age is not appropriate")
elif grade < 60 :
    print("grade is not good")

else:
    print("Not eligible")


membership = input("enter either True/False :").lower() == "true"
Coupan = input("enter has coupan :").lower() == "Yes"
price = 1000
discount = 0.10
final_price = price - 1000*0.10
if membership or Coupan:
    print("price :",final_price)
elif membership:
    print("price :",final_price)
elif Coupan:
    print("price :",final_price)
else:
    print("Nhi milega")

a= input("enter your days: ")
weekday = ['Monday','Tuesday','Wednesday','Thrusday','Friday']
weekends = ['Saturday','Sunday']

if a in weekday:
    print("weekdays",a)
elif a in weekends:
    print("weekends",a)
else:
    print("enter right data")


username = input("enter user name:") == 'user123'
password = input("enter password: ") == " "
if username and password:
    print("login successful")
elif username:
    print("Password not correct")
elif password:
    print("username not correct")
else:
    print("put valid details")








