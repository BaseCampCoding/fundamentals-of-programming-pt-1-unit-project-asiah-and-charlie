import computing
accounts = []
print("Welcome! ")
while True:
  print(accounts)
  answer = input("Which would you like to do? [save, change, view] ")
  if answer == 'save':
      application_1 = input("What application are you using? ")
      username_1 = input(f"What's your username for {application_1}? ")
      email_1 = input(f"What's your email for {application_1}? ")
      password_1 = input(f"What's your password for {application_1}? ")
      accounts.append({'account': application_1, 'username': username_1, 'email': email_1, 'password': password_1})
  elif answer == 'change':
    pass  
  elif answer == 'view':
    info = input("What account are you needing information for? ")
    accounts =  computing.get_account(accounts, info)
    if accounts == accounts:
      print(accounts)
      print("There you go! ")

  else:
    print("Invalid option, try again! ")
  
