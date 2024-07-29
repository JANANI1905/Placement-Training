def printValue(a,b):
    len1 = len(a)
    len2 = len(b)
    if len1>len2:
        print(a)
    elif len2>len1:
        print(b)
    else:
        print("Sorry")   
printValue("apple","orange")