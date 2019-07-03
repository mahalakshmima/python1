b =int(input())
if (b>1):   
   for i in range(2, b//2):   
       if (b%i) == 0: 
           print("no")
           break
   else: 
       print("yes") 
else: 
   print("no")
