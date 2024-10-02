import json
# lists usage 
nums=[1,'Ayush',56]
print(nums[0])
#to insert in a list
nums.insert(2,'Gandhi')
nums.extend([29,65,'Foiba'])
print(nums)
#to delete values from a list
nums.remove(56)
print(len(nums))
del nums[2:]
print(nums)
#tuples usage
tup=(2,5,'Ayush',85)
print(tup)
st={1,5,'Ahh!!!',98}
print(st)
#dictionary is like maps in c++
dict={1:'Ayush',2:'Gandhi' , 3:'Akash' , 4:'Asim'}
i=int(input("Enter the value of number"))
while i<6:
    i+=1
print("Value of i = "+str(i))
# while i<6:
#     i+=1
#     if(i==3):
#         continue
print("Value of i = "+str(i))
# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6") using the else we can run the block of code once when the condition is no longer true
#for loop
fruits=["Banana" , "Apple" , "Grapes" , "Pineapple"]
for x in fruits:
    print(x)
for j in range(2,8):
    print(j)
print('\n\n')
for k in range(1,10,3):
    print(k)
else:
    print('This is executed after the loop is finished executing')
def function1():
    print('This is my function 1')
def function2(sudhir='sudhir'):
    print('This is my function 2 using the default argument if there is no arument given '+ sudhir)
function1()
function2()
def function3(*kids):
    print('Here the * before the argument is used when the number of arguments are not fixed ' +kids[1])
function3("Ayush" , "Gandhi" , "Foiba")
#json to python
# json.loads(x3)#here is x is some string in json file
#python to json
# json.dump(x3)#convert the x to json
x2 = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x2))