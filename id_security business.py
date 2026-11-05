card = input("enter access card:")
if card == str("blue"):
    print("access granted")
elif card != str("blue"):
    print("access denied") 
    pin = int(input("enter user pin"))
if pin == int("20028168") or int("20028175"):
 print("access granted")
elif pin != int("20028168") or int("20028175"):
    print("access denied")