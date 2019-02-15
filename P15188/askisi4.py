def zero(*arg):
    #if this is the first argument(the argument inside the operator)
    if(len(arg) == 0):
        return 0
    else:
        for key in arg:
            #check the operator and do the calculation
            if(key[0] == "*"):
                return 0*key[1]
            elif(key[0] == "+"):
                return 0+key[1]
            elif(key[0] == "-"):
                return 0-key[1]

def one(*arg):
    if(len(arg) == 0):
        return 1
    else:
        for key in arg:
            if(key[0] == "*"):
                return 1*key[1]
            elif(key[0] == "+"):
                return 1+key[1]
            elif(key[0] == "-"):
                return 1-key[1]

def two(*arg):
    if(len(arg) == 0):
        return 2
    else:
        for key in arg:
            if(key[0] == "*"):
                return 2*key[1]
            elif(key[0] == "+"):
                return 2+key[1]
            elif(key[0] == "-"):
                return 2-key[1]

def three(*arg):
    if(len(arg) == 0):
        return 3
    else:
        for key in arg:
            if(key[0] == "*"):
                return 3*key[1]
            elif(key[0] == "+"):
                return 3+key[1]
            elif(key[0] == "-"):
                return 3-key[1]

def four(*arg):
    if(len(arg) == 0):
        return 4
    else:
        for key in arg:
            if(key[0] == "*"):
                return 4*key[1]
            elif(key[0] == "+"):
                return 4+key[1]
            elif(key[0] == "-"):
                return 4-key[1]

def five(*arg):
    if(len(arg) == 0):
        return 5
    else:
        for key in arg:
            if(key[0] == "*"):
                return 5*key[1]
            elif(key[0] == "+"):
                return 5+key[1]
            elif(key[0] == "-"):
                return 5-key[1]

def six(*arg):
    if(len(arg) == 0):
        return 6
    else:
        for key in arg:
            if(key[0] == "*"):
                return 6*key[1]
            elif(key[0] == "+"):
                return 6+key[1]
            elif(key[0] == "-"):
                return 6-key[1]

def seven(*arg):
    if(len(arg) == 0):
        return 7
    else:
        for key in arg:
            if(key[0] == "*"):
                return 7*key[1]
            elif(key[0] == "+"):
                return 7+key[1]
            elif(key[0] == "-"):
                return 7-key[1]

def eight(*arg):
    if(len(arg) == 0):
        return 8
    else:
        for key in arg:
            if(key[0] == "*"):
                return 8*key[1]
            elif(key[0] == "+"):
                return 8+key[1]
            elif(key[0] == "-"):
                return 8-key[1]

def nine(*arg):
    if(len(arg) == 0):
        return 9
    else:
        for key in arg:
            if(key[0] == "*"):
                return 9*key[1]
            elif(key[0] == "+"):
                return 9+key[1]
            elif(key[0] == "-"):
                return 9-key[1]


def times(num):
    #return the number took as argument and the operator
    return "*",num

def plus(num):
    return "+",num

def minus(num):
    return "-",num

if __name__ == '__main__':
    print(eight(minus(three())))
