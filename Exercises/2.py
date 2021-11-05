def email(a):
    if "." in a:
        if "@" in a:
            return True
        else:
            return False
    else:
        return False
email1 = str(input("Enter your e-mail: "))
if email(email1) == True:
    print( email1 + " is a valid e-mail.")
else:
    print( email1 + " is not a valid e-mail.") 