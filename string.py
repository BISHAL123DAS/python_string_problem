#1. Write a program to take input a string of digits and convert it to an integer without
#using int() function.

# n=input("enter your string:")
# sum=0
# for i in n:
#         sum=sum*10+(ord(i)-48)
# print(sum)        

#2.Write a program to take binary input numbers and convert it to an integer without
#using int() function.

#3. WAP to remove i^th character of a string.

# n=input("enter your value:")
# rem=int(input("which i'th charecter you can delte:"))
# a=n[:rem]
# b=n[rem+1:]
# ans=a+b
# print("the new string is:",ans)

#4. WAP to calculate the length of a string, avoid space.
# n=input("enter your string:")
# count=0
# for i in n:
#     if(i!=' '):
#         count+=1
# print(count)  

#5. WAP to print even length words in a string.   
# n=input("enter your string:").split()
# s=''
# for i in n:
#     if(len(i)%2==0):
#         s=s+i+' '
# print(s)        

#6. Write a program uppercase Half String.    
# n=input("enter your string:")
# l=len(n)
# if(l%2==0):
#     a=n[:(l/2)]
#     b=n[l/2:]
# else:
#     a=n[:int(l/2)+1] 
#     b=n[int (l/2)+1:]   
# c=a.upper()+b 
# print(c)   

#7. Write a program to capitalize the first and last character of each word in a string
# n=input("enter your string:").split()
# c=''
# for i in n:
#     st=i[:1]
#     mid=i[1:-1]
#     lst=i[-1]
#     c+=st.capitalize()+mid+lst.capitalize()+' '
# print(c)

#8. Python program to check if a string has at least one letter and one number
# n=input("enter your string:")
# flag=False
# flag2=False
# for i in n:
#     if(65<ord(i)<=90 and 97<ord(i)<=122):
#         flag=True
#     if(48<ord(i)<=57):
#         flag2=True
# if(flag==True & flag2==True):     
#     print("alphabet and number exist")
# elif(flag==True):
#     print("only alphabet exists ")
# elif(flag2==True):
#     print("only number exists")
# else:
#     print("letter and number dosen't exists")

# ----2nd approch
# n=input("enter your string:")
# if n.isalnum():
#     print("number and alphabet exists")
# elif n.isalpha():
#     print("its only alphabet")   #don't completed
# elif n.isnumeric():
#     print("its only print degits")
# else:
#     print("nothing to in string")           

#9. Write a program to accept the strings which contain all vowels
# n=input("enter your string:")
# v=['a','e','i','o','u']
# for i in n:
#     if not (i in v):
#         print("not accepted")
#         break
# else:
#     print("accepted")
        

#  10. Write a program to count the Number of matching characters in a pair of string
# n=input("enter your string:")
# n2=input("enter your strings:")
# st=set(n)
# st2=set(n2)
# count=0
# for i in st:
#     if i in st2:
#         count+=1
# print(count)             

# 11. Write a program to remove all duplicates from a given string in Python, keeping the
#first character only  

# n=input("enter your string:")
# s=' '
# for i in n:
#     if i not in s:
#         s+=i
# print(s)        
            

#12. Write a program to least Frequent Character in String
# n=input("enter your string:")
# dic={}
# for i in n:
#     if (i in dic):
#         dic[i]+=1         
#     else:
#         dic[i]=1
# res=min(dic,key=dic.get)
# print(res)            


#13. Write a program to maximum frequency character in String

# n=input("enter your string:")
# dic={}
# for i in n:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# res=max(dic,key=dic.get)  
# print(res)    

#14. Write a program to odd Frequency Characters
# n=input("enter your string:")
# s=[]
# for i in n:
#     if(n.index(i)%2!=0):
#         s.append(i)
# string = ",".join(s)       
# print(string)

#15. Write a program to specific Characters Frequency in String List

#-----single word find out---

# n=input("enter your string:")
# w=input("enter your word")
# l=n.count(w)
# print(l)

# n=input("enter your string:")
# find=input("which word you find?").split()
# l=[]
# for i in find:
#     l.append(n.count(i))
# print(l)    
    

#16. Write a program to frequency of numbers in String
# n=input("enter your string:")
# dic={}
# for i in n:
#     if(48<ord(i)<=57):
#         dic[i]=n.count(i)
# print(dic)                  

#17. Write a program to program to check if a string contains any special character
# n=input("enter your string:")
# spl='[~!@#$%^&*()]'
# flag=False
# for i in n:
#     if i in spl:
#         flag=True
# if(flag==True):
#     print("yes")
# else:
#     print("no")    

#18. Write a program to generating random strings until a given string is generated


#19. Write a program to find words that are greater than the given length k
# n=input("enter your string:").split()
# l=int(input("enter your given length:"))
# nl=[]
# for i in n:
#     if(len(i)>l):
#         nl.append(i)
# string=" ".join(nl)        
# print(string)        

#20. Write a program for removing i-th character from a string


#----check 3 no question

#21. Write a program to split and join a string
# n=input("enter your string:").split()
# s=''
# for i in n:
#     s+=i+' '
# print(s)    

#22. Write a program to find all close matches of input string from a list

#23. Write a program to find uncommon words from two Strings

# n=input("enter your strings:").split()
# n2=input("enter your strings:").split()
# for i in n:
#     if i not in n2:
#         print(i)

# for i in n2:
#     if i not in n:
#         print(i)        

#24. Write a program to swap commas and dots in a String
# n=input("enter your string:")
# st=''
# for i in n:
#     if(i==','):
#         st+='.'
#     elif(i=='.'):
#         st+=','
#     else:
#         st+=i
# print(st)                

#25. Write a program to print permutation of a given string using inbuilt function

#26. Write a program to convert numeric words to numbers
# n=input("enter your nummeric words:")
# sum  =0
# for i in n:
#     sum=sum*10+ord(i)-48
# print(sum)  

#27. Write a program to word location in String
# n=input("enter your strng:")
# for i in n:
#     print(i,"index of",n.index(i))

#28. Write a program to find consecutive characters frequency
# n=input("enter your string:")
# dic={}
# for i in n:
#     if i in dic:
#         dic[i]+=1
#     else:
#         dic[i]=1
# for i in dic:
#     print(i,'times',dic[i])    

#  29. Write a program to preform string slicing in Python to rotate a string   
# n=input("enter your string:")
# num=int(input("enter your number:"))
# a=n[:num]
# l=n[num:]
# res=l+a
# print(res)

#30. Write a program to string slicing in Python to check if a string can become empty by recursive deletion
# n=input('enter your string:')
# de=input("enter your strings")
# st=''
# if(len(n)%len(de)!=0):
#     print("not posssibles!")
# else:
#     l=len(n)//len(de)
#     for i in range(l):   #not proper solutions
#         st+=de
#     else:
#         if(n==st):
#             print("possible")
#         else:
#             print("not possible!")    

#31. Write a program to find minimum number of rotations to obtain actual string

#32. Write a program to sort String list by K character frequency
# n=int(input("how many times:"))
# l=[]
# for i in range(n):
#     s=input("enter your string:")
#     l.append(s)
# c=input("enter your charecter?")
# dic={}                                   #its to not clear this line
# for i in l:
#     dic[i]=i.count(c)
# res_list = sorted(dic)
# print(res_list)   
