while True:
    print("Enter x to exit")
    value1=input("Enter String:")
    if value1=='x':
        break
    else:
        newvalue=value1
        punctuations='''!(){}[]:;'"\,<>.@#$%^&*'''
        for x in value1.lower():
            if x in punctuations:
                newvalue=newvalue.replace(x,"")
        print("new String =",newvalue)
