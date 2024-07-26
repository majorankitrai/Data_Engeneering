color = ['blue','green','red']
print(type(color))

a_str = "Hello"
list_str = list(a_str)
print(type(list_str))

list_compre = [i**2 for i in range(1,6)]
print(list_compre)

first_element =color[0]
last_element = color[-1]
print(first_element)
print(last_element)

specific_element = color[1]
print(specific_element)

color[1] = 'pink'
print(color)

color[-1] = 'purple'
print(color)

color.remove('pink')
print(color)

color.pop(0)
print(color)


board_2D = [["-" for _ in range(3)] for _ in range(3)]
print(board_2D)

cube_3D = [[["-" for i in range(3)] for i in range(3)] for i in range(3)]
print(cube_3D)

list_ = ['a','b','c','d','e']
for i in list_:
    print(i)

for i in range(len(list_)):
    print(i,list_[i],end="\n")

for i,j in enumerate(list_):
    print(i,j)

student = ["archit",24,"A+"]
name,age,grade = student
print(name)
print(age)
print(grade)




