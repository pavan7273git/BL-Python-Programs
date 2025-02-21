'''
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name'''

#Taking input from user
user_name=input('Enter the User Name: ')

#if
while True:
    if len(user_name)>=3 :
      print(f'\"Hello {user_name}, How are you?\"')
      break

    else:
      print("The User Name Should contain minimum 3 Characters")
      user_name=input('Enter the User Name again: ')