'''properties={}
rental_open=True
while rental_open:
    username=input("\nwhat is your name")
    rent_property=input("\naddress of your property")
    type_of=input("\nwhat type of property")
    properties[username]=rent_property,
    
    repeat=input("\nany more name")
    if repeat=="no":
        rental_open=False
print("\n--- property to rent---")
for username,rent_property, in properties.items():
    print(username+"has"+rent_property+"to rent")
'''
n=['manik','tushar']
no=['yes','tyry']
for q,a in zip(n,no):
    print('name {0} rubish  {1}'.format(q,a))
