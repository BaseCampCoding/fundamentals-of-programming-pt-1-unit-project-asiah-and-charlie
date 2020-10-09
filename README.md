# Password Manager
This password manager prompts the user with two choices. They can choose either save/view. They can save their application name, username, email, and password with "save". They can then view their saved information with "view".
The program will also let the user know if they have used the same password more than once and will prompt them if they wanted to save anyways or change it. It will also check if the password is strong. It uses the len function, if the password they typed in is too short, it will print, "Weak password please try again.". 
# Usage
Welcome to your password manager!

Which would you like to do? [save, view] save

What application are you using? facebook

What's your username for facebook? Charles

What's your email for facebook? gmail

What's your password for facebook? 1234

That's a weak password. Enter a stronger password.

What's your password for facebook? 123456

Strong Password

Everything saved successfully!

Which would you like to do? [save, view] view

What account are you needing information for? facebook

{'account': 'facebook', 'username': 'Charles', 'email': 'gmail', 'password': '123456'}

Which would you like to do? [save, view] 

## password_manager.py
This file imports computing.py. It starts by welcoming the user, then prompting them with 2 choices (save/view). The program uses if statements based on which answer they chose. If they choose save, the program prompts them with questions and saves thier answers as a variable. It asks them, what application are you using, what's your username, email, and password. When they type in their password, a len function checks to see if their password is at least 6 characters. It will prompt them saying, "That's a weak password. Enter a stronger password." Also, the program uses a for loop in computing and checks to see if it has already been used before. If it has been used before, it prompts the user saying, "It's not good practice to use the same password. Would you like to save anyways?" If they choose yes, it will go ahead and save the information. If they choose no, it will ask them to "Choose new password."
After they entered their information, the program will print, "Everything saved successfully." Then loops back with a while loop to prompt them with the two questions again (save/view). If user chooses view, it will prompt the user asking them which account they would like information for. If they type in an account that's not saved it will tell the user, "Sorry we couldn't find that account try agian." If they type in an account that is saved, it will print out the dictonary all of the information is stored in.
