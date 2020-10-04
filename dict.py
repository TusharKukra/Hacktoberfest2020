def dictionairy():  
  
 # Declaring hash function       
 key_value ={}     
   
# Initializing the value  
 key_value[2] = 56       
 key_value[1] = 2 
 key_value[5] = 12 
 key_value[4] = 24
 key_value[6] = 18      
 key_value[3] = 323 
   
  
 print ("Task 3:-\nKeys and Values sorted",  
   "in alphabetical order by the value") 
   
 # Note that it will sort in lexicographical order 
 # For mathematical way, change it to float 
 print(sorted(key_value.items(), key = 
             lambda kv:(kv[1], kv[0])))    
