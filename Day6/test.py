# class student:
#     name='arun'
#     age=23
# s1=student()
# print(s1.name)
# print(s1.age)

#----------------------

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
# c1=Student("arn",26)
# c2=Student("lee",25)
# print(c1.name)
# print(c2.age)

# class customer:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

#     def display(self):
#         print(self.name,"AGE:",c1.age)

# name=input("Enter name:")
# age=int(input("Enter age:"))

# c1=customer(name,age)
# c1.display()

class teacher():
    def __init__(self,name,age):
        self.name=name 
        self.age=age

class student(teacher):
    def show(self):
        print(self.name,self.age)

t1=student("arun",12)
t1.show()

