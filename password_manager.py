import computing
accounts = []
print("Welcome to your password manager! ")
while True:
  answer = input("Which would you like to do? [save, change, view] ")
  if answer == 'save':
     application_1 = input("What application are you using? ")
     username_1 = input(f"What's your username for {application_1}? ")
     email_1 = input(f"What's your email for {application_1}? ")
     password_1 = input(f"What's your password for {application_1}? ")
     accounts.append({'account': application_1, 'username': username_1, 'email': email_1, 'password': password_1})
     while True:
        if len(password_1) > 5:
          print("Strong Password")
          break
        else:
          print("That's a weak password. Enter a stronger password.")
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
     else:
       print("Everything saved successfully!")
  elif answer == 'change':
    pass  
  elif answer == 'view':
    info = input("What account are you needing information for? ")
    account =  computing.get_account_info(accounts, info)
    if account:
      print(account)
    else:
      print("Sorry we couldn't find that account please try again. ")

  else:
    print("Invalid option, try again! ")