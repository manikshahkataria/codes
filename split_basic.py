#user='harsh 24'.split( )
#print(user)
user=input('enter the info').split(',' )#split on the basis of space and convert string into the list
print(user)
name,age=input('enter name and age').split(',')
print(name)
print(age)
print(type(age))
print(','.join(user))
