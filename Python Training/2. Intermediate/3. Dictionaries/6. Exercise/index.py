details = {"name":"archit","contact number":620141}
print(type(details))

list_ = [("name","ankit"),("hum","tum")]
dict_ = dict(list_)
print(dict_)
print(type(dict_))

movie = {"name":"Titanic",'year': 1999,"director":"abc"}
print(movie['name'])
print(movie['year'])
print(movie['director'])

student = {"name":"ankit","grade":"A+"}
student_update = {"name":"archit","grade":"A++"}
student.update(student_update)
print(student)

shopping = {"maggie":4,"brush":6}
del shopping["brush"]
print(shopping)

check = "address"
if check in shopping:
    print(check,shopping[check])
else:
    print("not found check")

shopping.get("address","not available")

employee = {"name":"ankit","dept":"MIS",
            "name":"archit","dept":"software"}
for key,value in employee.items():
    print(f'{key}:{value}')


customer = {"customer1":{"name":"ankit","address":"delhi","contact number":6201},"customer2":{"name":"archit","address":"ads","contact":2322}}
print(customer["customer1"]["name"])
print(customer["customer1"]["address"])

