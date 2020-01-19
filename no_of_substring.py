import re 
# Initialising string 
ini_str = "ababababa"
sub_str = 'aba'
  
# Count count of substrings using re.findall 
res = len(re.findall('(?= aba)', ini_str)) 
  
# Printing result 
print("Number of substrings", res)




#2 sollution








# Initialising string 
ini_str = "ababababa"
sub_str = 'aba'
  
# Count count of substrings using startswith 
res = sum(1 for i in range(len(ini_str))  
         if ini_str.startswith("aba", i)) 
  
# Printing result 
print("Number of substrings", res)
