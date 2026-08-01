
# DECREMENT PATTERN OR INVERTED HALF PYRAMID

for i in range (1,6):
    for j in range (i,6):
        print("*",end="  ")
    print()
    

# INCREMENT PATTERN OR INVERTED HALF PYRAMID

for i in range (1,6):
    for j in range (i):
        print("*",end=" ")
    print()
    
    
# FULL PYRAMID
   
for i in range(6):
    for j in range(i,6):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    

# INVERTED FULL PYRAMID    
    
for i in range (6):
    for j in range (i+1):
        print (" ",end=" ")
    for j in range (i,6):
        print ("*",end=" ")
    for j in range (i,6-1):
        print ("*",end=" ")
    print()
