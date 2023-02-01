"""set["John", "peter",10,22]
print(set[1])

for i in range (999):
     print(i)


a =["aipo", "bravo", "charity"]

for s in a:
    print(s[:1])

    
def name():
    print("John")
    name()"""



print ("welcome to isg")
Acc = input("do you have an account")
if Acc == "yes":
    print ("please login:\n")
    user_name = input ("Username:")
    pass_ = input  ("password:")
    print("welcome to your child's profile, what would you like to see ?")
    print ("\nl.Behaviours , \n2.Academics,\n3.Sports\n.3Homeworks")
    select = input ("select any:")
    if select == "1":
        print("Sipho's profile")
        print ("\n Sipho is noisy in class\n -He eats during learning")
    elif select == "2":
            print("formal task february: 30/45")
            print("formal task apri: 12/30")
            print("formal task june: 30/30")

    elif select == "3":
         print ("1st place in javaline")
         print ("3rd place in long jump")
         print ("1st place in athletics")
         other_sports = "NA"
         other_sports = True
         
         while other_sports == True:
             print(other_sports)
             break
            
            
    count = 2
    while count >0:
        count -= 1
        Pass_ = input("Enter password")
        if pass_ =="1234":
                print(" welcome ")
        else:
              retry = input("Retry password")
              count -= 1
              print("Login Failed")
              break
elif Acc == "no":
        print("please register")
        first_name = input ("Name:")
        surname = input ("Surname:")
        email = input ("Email:") 
        pass_word = input ("password:")
        print("confirm password:")
        pass_word = input ("confirm password:")
        if pass_word == pass_word:
                       print ("account confirmed")

        print ("welcome to your child's profile, what would you like to see ?")
        print ("\nl.Behaviours , \n2.Academics,\n3.Sports\n.3Homeworks")
        

else:
            ("Password doesn't match")
            quit()


        

    
