#this program will prompt the user for which application they would like to remember their passwords for. 
#it will also return the passowrds, emails, and usernames they enter for their applications
print("Welcome! ")
application_1 = input("What application are you using? ")
username_1 = input(f"What's your username for {application_1}? ")
email_1 = input(f"What's your email for {application_1}? ")
password_1 = input(f"What's your password for {application_1}? ")
cat = input(str("Which application do you need information for? ")).lower()
list_1 = []
list_1.append(username_1)
list_1.append(email_1)
list_1.append(password_1)

if cat == application_1:
    for i in list_1:
      print(i)

print("Hey")
