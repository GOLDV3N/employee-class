'''Employee in and Out
Outline:
Write a program to create a class with the named employee and create a constructor and destructor. Then, write a function to create an object for that class and delete the object. Make sure you call the function to get everything implemented!'''

class employee:
    def __init__(self):
        print('employee created')
    def __del__(self):
        print("destructer called")

def creat_obj():
    print('making object....')
    obj = employee()
    print('function end....')
    return obj
print('calling create_obj() function....')
obj = creat_obj()
print('object end....')