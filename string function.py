#string lenght 1
'''
a="saravanan"
count=0
for i in a:
    count+=1
print("len:",count)


#alphabets check 2

a="saravanan"
print(a.isalpha())



#digits check 3

a="1234567"
print(a.isdigit())


#count the number 4

a="saravanan"
count=0
for i in a:
    if i not in "aeiouAEIOU":
        count+=1
print("consonants :",count)



#find the first 5

a="saravanan"
for i in a:
    if a.count(i)==1:
        print(i,end="   ")



#swapcase character  6

a="SaRaVaNaN"
print(a.swapcase())


#Remove all spaces  7

a="saravanan is develaper"
print(a.replace(" ",""))


#start wiht vowels 8

a="apple"
if a[0].lower()in "aeiou":
    print("vowel")
else:
    print("not vowel")


#count the character 9

a="apple,banana"
print(a.count("a"))

#Replace all vowels  10

a= "saravanan"
for i in "aeiou":
    a=(a.replace(i,"*"))    
print(a)


#even index character  11

a="saravanan"
for i in range(0,len(a),2):
    print(a[i])

    
#odd index character   12
    
a="saravanan"
for i in range(1,len(a),2):
    print(a[i])

#list of characters  13

a="saravanan"
print(list(a))


#count special character 14

a="saravanan@#$$"
count=0
for i in a:
    if not i.isalnum():
        count+=1
print(count)'''
































































