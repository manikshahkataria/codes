size = int(input())
  
# FOR THE APEX OF HEART  
for a in range(int(size / 2), size + 1, 2): 
      
    # FOR SPACE BEFORE PEAK-1 : PART 1 
    for b in range(1, size - a, 2):  
        print(" ", end = "") 
  
    # FOR PRINTING PEAK-1 : PART 2 
    for b in range(a): 
        print("A",end="") 
  
    # FOR SPACE B/W PEAK-1 AND PEAK-2 upper midddle space : 
    # PART 3 
    for b in range(1, (size - a) + 1): 
        print(" ", end = "") 
          
    # FOR PRINTING PEAK-2 : PART 4 
    for b in range(1, a): 
        print("A", end = "") 
  
    print("") 
      
  
# FOR THE BASE OF HEART ie. THE INVERTED 
# TRIANGLE  
for a in range(size, -1, -1): 
      
# FOR SPACE BEFORE THE INVERTED TRIANGLE: 
# PART 5  
    for b in range(a, size): 
        print(" ", end = "") 
          
    # FOR PRINTING THE BASE OF TRIANGLE: 
    # PART 6 
    for b in range(1, (a * 2)): 
        print("B", end = "") 
    print("")  
      
# This code is contributed by Smitha. 
