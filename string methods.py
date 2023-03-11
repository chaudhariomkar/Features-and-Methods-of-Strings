""""""
"""
Features of String
Syntax ' '
1.String is an important data types in python
2.String is immutable data types
    Mutable - Values can be updated 
    Immutable - Values cannot be updated
3.Accepts all types of Data 
    Homogenous - Can only store single type of data 
    Hetrogenous - Can store more than one type of data
4.Background Data Structure of string is - ARRAY
5.Sequence order is preserved
6.Indexing (To Fetch Single Element) is Supported
    Positive Indexing - LEFT to RIGHT
    Negative Indexing - RIGHT to LEFT
7.Slicing (To Fetch Multiple Element or Substring in a sequence) is Supported
8.There are many methods in Strings like .....
"""
a = 'Hello Pretesh Chaudhari, Welcome to the World of Python'
print(a)
#1.Uppercase
print(a.upper())
#2.Lowercase
#Method 1
print(a.lower())
#Method 2
print(a.casefold())
#3.Capitalize
print(a.capitalize())
#4.Title - Each Initials Capital
print(a.title())
#5.Swapcase
print(a.swapcase())
#6.Strip,Lstrip,Rstrip
# Default Strips White Spaces
b = "     Kantilal     "
print(b.lstrip())
print(b.rstrip())
print(b.strip())
c = '#####Jayshree------'
# Also Strips given values
print(c.lstrip('#'))
print(c.rstrip('-'))
print(c.strip('#,-'))
#6.Replace
print(c.replace('#',''))
#8.Count
print(c.count('e')) #Single letter
print(c.count('shree')) #Multiple letter
print(c.count('Jayshree')) #Word
#9.Find
print(c.find('e')) #Gives lowest Index Number
print(c.find('k')) #Returns -1 if value is not present
#10.Index
print(c.index('e')) #Gives lowest Index Number. Returns Index Error if Value is not present
#11.Len
print(len(a))
#12.Split
print(a.split())
#13.Join
print(''.join(a))
#14.Startswith - boolean output
print(a.startswith('H'))
#15.Endswith - boolean output
print(a.endswith('w'))
print('------------------------------------')
#Other boolean output
#16.isascii,isidentifier,isprintable,islower,isupper,isspace,istitle,isaplha
x = 'Amol123'
print(x.isascii()) #isascii
print(x.isidentifier()) #isidentifier
print(x.isprintable()) #isprintable
print(x.islower()) #islower
print(x.isupper()) #isupper
print(x.isspace()) #isspace
print(x.istitle()) #istitle
print(x.isalpha()) #isaplha
print('-------------------------------------')
#17.isalnum,isdecimal,isdigit,isnumeric
print(x)
print(x.isalnum()) #isalnum
y = '1000'
print(y)
print(y.isnumeric()) #True - if string is a numeric string
print(y.isdecimal()) #True - if string is a decimal (0-9)
print(y.isdigit()) #True - if string is a digit string


