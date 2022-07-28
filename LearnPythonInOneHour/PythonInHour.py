
# # Quick Python for everyone to get started

# In[2]:


#Checking the python version
from platform import python_version
print(python_version())


# In[3]:


print("Hello world")


# In[4]:


type(5)


# In[5]:


# Int, floats, strings
type(5.0)


# In[6]:


type("5")


# In[7]:


type(5+2j)


# In[8]:


complex_number = (5+2j)
complex_number


# In[9]:


complex_number.real


# In[10]:


complex_number.imag


# In[12]:


complex_number.conjugate()


# In[13]:


message = "I am looking for a chair"
print(message)


# In[14]:


message1 = 'I am looking for a chair'
print(message1)


# In[16]:


message2 = "I 'm looking for a chair"
print(message2)


# In[18]:


use_all_quotes = """I am doing a python tutorial:
"I 'm good at it."""
print(use_all_quotes)


# In[19]:


#Arithmetic operations in Python
10-4


# In[20]:


10+4


# In[22]:


minutes = 105
hours = minutes//60
print(hours)


# In[23]:


remainder = minutes - hours*60
remainder


# In[24]:


minutes%60


# In[27]:


type(5 == 5)


# In[26]:


5 == 4


# In[28]:


bool(1)


# In[29]:


bool(0)


# In[30]:


True+5


# In[31]:


float(5)


# In[32]:


str(5)


# In[33]:


round(5.88844,1)


# In[34]:


temp_pi = 3.14
temp_pi


# In[35]:


import math


# In[36]:


math.pi


# In[37]:


math.sqrt(9)


# In[38]:


signal_power = 10
noise_power = 2
ratio = signal_power/noise_power
decibels = 10*math.log10(ratio)
print(decibels)


# In[41]:


degrees = int(input("please enther the degrees here = ")) # taking input from the user
radians = degrees/180*math.pi
print(radians)


# In[42]:


math.radians(150)


# In[47]:


# Decision making in Python
number = int(input("Please enter any number = "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")


# In[50]:


given_number = int(input("Please enter your number"))
if given_number > 20:
    print("The number is greater than 20")
elif given_number == 20:
    print("the number is 20")
else:
    print("the number is smaller than 20")


# In[53]:


#Chained conditionals
x = int(input("Please enter the value of x = "))
y = int(input("Please enter the value of y = "))
if x == y:
    print("x and y are equal")
elif x > y :
    print("x is greater than y")
else:
    print("x is smaller than y")


# In[55]:


#Loops
count = 0
while (count <9):
    print("the count is: ",count)
    count+=1
print("I am outside the loop now")


# In[57]:


#For loop
for i in range(0,9):
    print("the count is = ",i)
print("I am outside the loop now")


# In[58]:


months = ["J","F","M","A","M","J"]
for i in months:
    print(i)


# In[59]:


def area(radius):
    area = math.pi*radius**2
    return area


# In[62]:


area(35)


# In[68]:


#Recursion
from functools import lru_cache
@lru_cache(maxsize = 1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n >2:
        return fibonacci(n-1)+fibonacci(n-2)


# In[71]:


for n  in range(1,10):
    print(n," : ",fibonacci(n))


# In[72]:


#String methods
name = "Hassan Raza"
print(name)


# In[73]:


len(name)


# In[74]:


name.lower()


# In[75]:


name.upper()


# In[76]:


dir()


# In[77]:


#Functions in detail now
def f():
    pass


# In[78]:


f()


# In[79]:


def ping():
    return "Hassan"


# In[80]:


ping()


# In[81]:


dir(math)


# In[91]:


def volume(r):
    """Gives the volume"""
    v = (4/3)*math.pi*r**3
    return v


# In[84]:


volume(7)


# In[85]:


example = volume(7)*2
example


# In[92]:


help(volume)


# In[93]:


def cm(feet = 0, inches = 0):
    inches_to_cm  = inches*2.54
    feet_to_cm = feet*12*2.54
    return inches_to_cm + feet_to_cm


# In[95]:


cm(feet = 5,inches = 0)


# In[96]:


cm(5,0)


# In[97]:


cm(inches = 0,feet = 5)


# In[98]:


cm(5,2)


# In[99]:


name


# In[100]:


name[0]


# In[101]:


name[1]


# In[103]:


name[-2]


# In[104]:


#Lists
#Ordered data
#Two ways of making lists
list1 = list()


# In[105]:


type(list1)


# In[106]:


list2 = []
type(list2)


# In[107]:


list2.append("Hassan")


# In[108]:


list2


# In[109]:


prime = [2,3,5,7,11]


# In[110]:


prime


# In[111]:


prime.append(13)
prime.append(17)
prime


# In[115]:


#Splicing the list
prime[-1]


# In[117]:


prime[-8]
#You can only wrap around otherwise it will generate an error message


# In[120]:


prime[2:5] #includes the first index and exclude the last index


# In[121]:


prime


# In[122]:


list3 = [125,True,"alpha",1.34,[32,False]]
list3


# In[124]:


list3[2]


# In[125]:


list3[4][1]


# In[126]:


combined_list = list3+prime
combined_list


# In[127]:


125 in combined_list


# In[129]:


"hassan" in combined_list


# In[130]:


for i in prime:
    print(i)


# In[132]:


prime*2


# In[136]:


prime[:-2]


# In[137]:


del prime[0]


# In[138]:


prime


# In[139]:


prime.remove(11)


# In[140]:


prime


# In[143]:


s = "I am studying"
string = s.split()
string


# In[144]:


#Delimiter
s = "sam-sam-sam"
delimiter = "-"
string = s.split(delimiter)
string


# In[145]:


a = "hassan"
b = "hassan"
a in b


# In[146]:


a = [1,2]
b = [1,2]
a in b


# In[147]:


#list
prime


# In[148]:


perfect_squares = (1,4,9,16)


# In[150]:


type(perfect_squares)


# In[151]:


for i in prime:
    print(i)


# In[152]:


for i in perfect_squares:
    print(i)


# In[153]:


print("LIST METHODS")
print(dir(prime))
print(125*"*")
print("Tuple methods")
print(dir(perfect_squares))


# In[154]:


import sys
print(dir(sys))


# In[155]:


print(help(sys.getsizeof))


# In[157]:


list_eg = [1,2,3,"name",True]
tuple_eg = (1,2,3,"name",True)
print("list size",sys.getsizeof(list_eg)," Bytes")
print("Tuple size",sys.getsizeof(tuple_eg)," Bytes")


# In[158]:


survey = (27,"USA",True)
age = survey[0]
country = survey[1]
knows_python = survey[2]


# In[160]:


print(country)


# In[161]:


# #Dictionaries
# user_ID = 209
# message = "I am a Robot"
# Language = "machine language"
# location = "2342340-234-.234897923"


# In[162]:


dictionary = {}


# In[163]:


type(dictionary)


# In[164]:


post = {"user_ID":209,"message":"I am a Robot","Language":"machine language"}


# In[165]:


print(post)


# In[166]:


post["Language"]


# In[167]:


post["user_ID"]


# In[168]:


post2 = dict(meassge1 = "its cool", language = "English")
print(post2)


# In[170]:


post2["message1"]


# In[172]:


post2["has"]


# In[174]:


if "time" in post2:
    print(post2["time"])
else:
    print("nothing")


# In[175]:


try:
    print(post2["time"])
except KeyError:
    print("nothing")


# In[176]:


for key in post.keys():
    value = post[key]
    print(key, " = ",value)


# In[177]:


for key,value in post.items():
    print(key, " = ",value)


print("Thanks for visiting")
