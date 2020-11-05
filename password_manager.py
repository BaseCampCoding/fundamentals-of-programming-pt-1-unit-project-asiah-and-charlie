import sqlite3
import  computing

conn = sqlite3.connect('information.db')
cur = conn.cursor()

cur.execute(""" CREATE TABLE IF NOT EXISTS passwords(
  Application TEXT,
  Username TEXT,
  Email TEXT,
  Password TEXT
)"""
)

print("Welcome to your password manager! ")
while True:
  answer = input("""Which would you like to do?
    -save 
    -view 
    -exit
    > """)
  if answer == 'save':
    while True:
      application_1 = input("What application are you using? ")
      break
  
    username_1 = input(f"What's your username for {application_1}? ")
    email_1 = input(f"What's your email for {application_1}? ")
    password_1 = input(f"What's your password for {application_1}? ")
    
    check = computing.check_for_pass(cur, password_1)
    if check == True:
      print("It's not good practice to use the same password! ")
      them = input("Would you like to save anyways? [Y/N] ").upper()
      if them == 'Y':
        cur.execute(""" INSERT INTO passwords (Application, Username, Email, Password) VALUES (?, ?, ?, ?)""",(application_1, username_1, email_1, password_1))
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
    else:
      cur.execute(""" INSERT INTO passwords (Application, Username, Email, Password) VALUES (?, ?, ?, ?)""",(application_1, username_1, email_1, password_1))
      print("Password saved successfully.")
    # else:
    #   while True:
    #     if len(password_1) > 5:
    #       print("Strong Password")
    #       break
        # else:
        #   print("That's a weak password. Enter a stronger password.")
        #   password_1 = input(f"What's your password for {application_1}? ")

      
  elif answer == 'view':
    cur.execute(""" SELECT * FROM Passwords """)
    for row in cur.fetchall():
      print(row[0] +" - "+ row[1] +" - "+ row[2] +" - "+ row[3])
      
  elif answer == 'exit':
    break
  else:
    print("Invalid option, try again! ")
    # change view function to just throw all the dictonaries at the user when view is selected.