l1=[1,2,"php",2.22]
print(type(l1))
print(l1[2])
l1.append("python")
l1.insert(2,3)
print(l1)
t1=(1,2,'mango',9.0)
print(t1)
print(type(t1))
courses={1:"php",2:"python"}
print(courses)
print(type(courses))
courses[3]="Java"
print(courses)
print(dir(courses))
courses.pop(2)
print(courses)
fruit=["pear","mango","watermelon",[
    [
        ["orange"]
    ]
]]
print(fruit[2][0][0])
print(dir(fruit))
fruit.append("apple")
fruit.insert(3,"pineapple")
fruit.pop(0)
print(fruit)
a=[1,2,3,4,5]
a.pop(1)   #1 is the index 
print(a)