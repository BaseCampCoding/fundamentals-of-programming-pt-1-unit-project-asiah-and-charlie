<<<<<<< HEAD
=======
#this program will prompt the user for which application they would like to remember their passwords for. 
#it will also return the passowrds, emails, and usernames they enter for their applications
>>>>>>> 005e6297cadd0887b5084a6dea63092a108058c3
accounts = [
  ['facebook', 'Charles', 'person@whatever', '1234'],
  ['instagram', 'Asiah', 'person@whatever', '1243'],
]
print("Welcome! ")
while True:
  answer = input("Which would you like to do? [save, change, view] ")
  if answer == 'save':
    application_1 = input("What application are you using? ")
    username_1 = input(f"What's your username for {application_1}? ")
    email_1 = input(f"What's your email for {application_1}? ")
    password_1 = input(f"What's your password for {application_1}? ")
  elif answer == 'change':
    cat = input(str("Which application do you need information for? "))
    username_1 = input(f"What's your username for {application_1}? ")
    email_1 = input(f"What's your email for {application_1}? ")
    password_1 = input(f"What's your password for {application_1}? ")
  elif answer == 'view':
    cat = input("Which application do you need information for? ")
    if cat == application_1:
      for i in accounts:
        print(accounts[0])
      break
<<<<<<< HEAD
    elif cat == application_2:
=======
    elif cat == application_1:
>>>>>>> 005e6297cadd0887b5084a6dea63092a108058c3
      for i in accounts:
        print(accounts[1])
        break
    else: 
      print("Sorry, that application isn't saved. Try again. ")
  else:
    print("Invalid option, try again! ")
  
