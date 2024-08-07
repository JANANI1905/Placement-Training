h=int(input("Enter your choice 1.Faherinheit or 2.Celsius:"))
if h==1:
    f=float(input("Enter the temperature in Faherinheit :"))
    if f>=100.4:
        print("You have a fever")
    else:
        print("You have no fever..")
elif h==2:
    c=float(input("Enter the temperature in Celsius :"))
    if c>=32:
        print("You have a fever")
    else:
        print("You have no fever..")
else:
    print("Invalid Input...")
