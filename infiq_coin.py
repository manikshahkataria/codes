
def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    extra=rupees_to_make%5
    if (rupees_to_make<=(int(no_of_one*1))+(int(no_of_five*5))):
        
        
        if (extra==0):
            five_needed=int(rupees_to_make/5)
            
            
            
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
        else:
        
            five_needed=int(rupees_to_make/5)
            one_needed=extra
            
            print("No. of Five needed :", five_needed)
            print("No. of One needed  :", one_needed)
    else:
        print(-1)

    #Start writing your code here
    #Populate the variables: five_needed and one_needed


    # Use the below given print statements to display the output
    # Also, do not modify them for verification to work



#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(93,19,2)
