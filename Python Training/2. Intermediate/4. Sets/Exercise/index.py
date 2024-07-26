hobbies = {"playing","talking","watching"}
print(type(hobbies))

set_ = {1,1,2,3,4,1,2}
print(set_)

number = {1,2,3,4,5,6,7,8,9}
i = 24
if i in number:
    print("we have it")
else:
    print("we don't have it")

number.add(2)
print(number)

movie = {"titanic","kala jadu","hm utm"}
friend = {"titanic","ankit","sharad"}
either_watched = movie.union(friend)
print("movie watched by either u and your friend",either_watched)

both_watched = movie.intersection(friend)
print("movie seen both of us",both_watched)

different_movie = movie.difference(friend)
print("movie watched by you only:" ,different_movie)

fruits = {"mango","apple","banana"}
fruits.add("lichi")
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.discard("guava")
print(fruits)

