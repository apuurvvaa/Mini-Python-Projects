print("Welcome to my Computer Quiz!") #welcome users to the game

playing = input("Do you want to play? ") #here I create an option for the user to play the game

if playing.lower() != "yes": #here I use the .lower() to convert all the answers that the user types in to lower case.
    quit() #this function will immedietly terminate the program


print("Hooray! Let's Play :)")

score = 0

answer1 = input("What does CPU stand for? \n")
if answer1.lower() == "central processing unit":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print("CPU stands for Central Processing Unit!")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y": #here I use the .upper() to convert all the answers that the user types in to upper case.
    print("See you later!")
    quit()


answer2 = input("What does GPU stand for? \n")
if answer2.lower() == "graphics processing unit":
    print("CORRECT!")
    score += 1

else: 
    print ("Incorrect!")
    print ("GPU stands for Graphics Processing Unit!")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y": 
    print("See you later!")
    quit()

answer3 = input("What does RAM stand for? \n")
if answer3.lower() == "random access memory":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print("RAM stands for random access memory")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer4 = input("What does PSU stand for? \n")
if answer4.lower() == "power supply unit":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print ("PSU stand for power supply unit!")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer5 = input("Name one the functions of a computer: \n")
if answer5.lower() == "accepting data":
    print("CORRECT!")
    score += 1
elif answer5.lower() == "processing data": 
    print("CORRECT!") 
    score += 1
elif answer5.lower() == "storing data":
    print("CORRECT!")
    score += 1
elif answer5.lower() == "displaying data":
    print("CORRECT!")
    score += 1
else:
    print ("Incorrect!")
    print ("Four functions of a computer: \n Accepting Data \n Processing Data \n Storing Data \n Displaying Data ")
    print ("Try Again :)")


forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer6 = input("Name one of the factors affecting the Speed of the Microprocessor: \n")
if answer6.lower() == "number of intrustions build in the porcessor":
    print("CORRECT!")
    score += 1
elif answer6.lower() == "bandwidth":
    print("Correct!")
    score += 1
elif answer6.lower() == "clock speed":
    print("Correct!")
    score += 1
elif answer6.lower() == "number of transistors inside the processor":
    print("Correct!")
    score += 1
else: 
    print ("Incorrect!")
    print ("Factors that may a may affect the Speed of the Microprocessor are: \n Number of intrustions build in the porcessor \n Bandwidth \n Clock Speed \n Number of transistors inside the processor")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer7 = input("What does HDD stand for? \n")
if answer7.lower() == "hard disk drive":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print ("HDD stands for Hard Disk Drive")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer8 = input("What does SSD stand for? \n")
if answer8.lower() == "solid state drive":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print ("SSD stand for Solid State Drive")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer9 = input("What does a graphics card do? \n")
if answer9.lower() == "stores and manipulates digital images such as photographs and videos":
    print("CORRECT!")
    score += 1
else: 
    print ("Incorrect!")
    print ("A graphics card stores and manipulates digital images such as photographs and videos")
    print ("Try Again :)")

forward = input("Do you wish to continue?: Y/N \n")
if forward.upper() != "Y":
    print("See you later!")
    quit()

answer10 = input("What is an example of a of storage device? \n")
if answer10.lower() == "hard disk drive (HDD)":
    print("CORRECT!")
    score += 1
elif answer10.lower() == "solid state drive":
    print("Correct!")
    score += 1
elif answer10.lower() == "random access memory":
    print("Correct!")
    score += 1
elif answer10.lower() == "cd":
    print("Correct!")
    score += 1
elif answer10.lower() == "dvd":
    print("Correct!")
    score += 1
elif answer10.lower() == "blu-ray discs":
    print("Correct!")
    score += 1
elif answer10.lower() == "rom":
    print("Correct!")
    score += 1
elif answer10.lower() == "usb flash drive":
    print("Correct!")
    score += 1
else: 
    print ("Incorrect!")
    print ("Examples of storage devices include: \n Hard Disk Drive \n Solid State Drive \n Random Access Memory \n (CD, DVD, Blu-Ray Discs \n ROM \n USB Flash Drive)  ")

print("You got " + str(score) + " question correct!") # the reason for the str here is so that we can combine the numeric and the string value while printing the number, so we convert the int to str

print("You got " + str((score/10) * 100) + "%. \n") # this part is to give the user a percentage of overall score

print("The End!\n")
print("See you later!")
quit()
