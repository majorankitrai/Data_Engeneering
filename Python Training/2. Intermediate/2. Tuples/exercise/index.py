food = ('burger','pizza','masala dhosa')
print(type(food))

list_=['a','b','c']
tuple_list = tuple(list_)
print(type(tuple_list))

tuple_ = ('abc',1,True)
print(type(tuple_))

print(tuple_[0])

tuple_[0] = "d"
print(tuple_)
## it raise error because tuple file doesnot support item assigment becuase tuple is immutable.

student = ("archit",24,"A+")
(name,age,grade) = student
print(name)
print(age)
print(grade)




