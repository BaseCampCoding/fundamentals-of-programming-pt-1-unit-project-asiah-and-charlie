import json
with open("passwords.json") as file:
  json.load(file)

accounts = []
import computing
print("Welcome to your password manager! ")
while True:
  answer = input("""Which would you like to do?
    -save 
    -view 
    -exit
               """)
  if answer == 'save':
    while True:
      application_1 = input("What application are you using? ")
      check_account = computing.check_for_account(accounts, application_1)
      if check_account == False:
        print("Looks like you've already stored information for this account. ")
        variable = input("Would you like to save anyways? [Y/N] ").upper()
        if variable == 'Y':
          break
        else:
          continue
      else:
        break
  
    username_1 = input(f"What's your username for {application_1}? ")
    email_1 = input(f"What's your email for {application_1}? ")
    password_1 = input(f"What's your password for {application_1}? ")

     
    check = computing.check_for_pass(accounts, password_1)
    if check == True:
      print("It's not good practice to use the same password! ")
      them = input("Would you like to save anyways? [Y/N] ").upper()
      if them == 'Y':
        break
      elif them == 'N':
        print("Choose new password. ")
        password_1 = input(f"What's your password for {application_1}? ")
        while True:
          if len(password_1) > 5:
            print("Strong Password")
            break
          else:
            print("That's a weak password. Enter a stronger password.")
            password_1 = input(f"What's your password for {application_1}? ")
      print("Everything saved successfully!")
    else:
      while True:
        if len(password_1) > 5:
          print("Strong Password")
          break
        else:
          print("That's a weak password. Enter a stronger password.")
          password_1 = input(f"What's your password for {application_1}? ")
      print("Everything saved successfully!")
      accounts.append({'account': application_1, 'username': username_1, 'email': email_1, 'password': password_1})
      with open("passwords.json", "a") as file:
        json.dump(accounts, file)
        
        
  elif answer == 'view':
    with open('passwords.json') as file:
      info = json.load(file)
      print(info)
      
  elif answer == 'exit':
    break
  else:
    print("Invalid option, try again! ")
    # change view function to just throw all the dictonaries at the user when view is selected.