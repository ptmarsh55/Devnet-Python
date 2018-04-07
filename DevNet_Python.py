# ==================================================================================================
# This is my DevNet Express Intro to Python Exercise suite.
#    Select Corresponding Exercise number or type Exit to quit.
#    The simple Exercises are inline, while some of the more-complex ones are in Functions
# --------------------------------------------------------------------------------------------------
#
NumExercises = 18

# ==================================================================================================
# MathFun(radius) - 
# --------------------------------------------------------------------------------------------------
#
def MathFun(Rad):
    from math import pi
    RadSquare = Rad ** 2
    return (pi*RadSquare, RadSquare)

# ==================================================================================================
# my_function() - 
# --------------------------------------------------------------------------------------------------
#
def my_function():
    pass

# ==================================================================================================
# my_function1(cnt) - 
# --------------------------------------------------------------------------------------------------
#
def my_function1(cnt):
    print("My last count was: ",cnt)

# ==================================================================================================
# my_function2(cnt) - 
# --------------------------------------------------------------------------------------------------
#
def my_function2(cnt):
    import math
    return(math.pi * cnt)
# ==================================================================================================
# my_function2(cnt) - 
# --------------------------------------------------------------------------------------------------
#
def scopeFun(x):
    x += 5
    print("scopeFun: x = ", x)
    return()

# ==================================================================================================
# scopeGlob() - 
# --------------------------------------------------------------------------------------------------
#
def scopeGlob():
    global x
    x += 5
    print("scopeGlob: x = ", x)
    return()

# ==================================================================================================
# main() - Infinite loop.  Type "Exit" to quit.
# --------------------------------------------------------------------------------------------------
#
InputString = "Enter Exercise Number (1-" + str(NumExercises) + ") or 'Exit': "
while True:
    Response = str(input(InputString))
    if Response == "EXIT" or Response == "Exit" or Response == "exit" or Response == "E" or Response =="e":
        break
    elif Response == "1":
        # Introduction to Python  Exercise-1
        #    Classic "Hello World" and two variants showing formatting and quotes
        print ("Hello World!")
        print()
        print ('Hello World! \tHow are you?')
        print()
        print ("Hello World! \nHow's it going?")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "2":
        # Introduction to Python  Exercise-2
        #    Variable assignments:  Integer verses Strings - The second print returns an error
        myvar = 10
        print (myvar + 1)
        print()
        myvar = "10"
        #print (myvar + 1)
        # The next statement wouldn't happen because of the error in the previous line
        print (myvar + "1")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "3":
        # Introduction to Python  Exercize-3
        #    Comments & fomatting for reading + Intro to Conditionals and Indentation
        # This is a comment and blank spaces make code readable 

        print()
        print ("Helloworld!")
        num = 1
        if num < 1:
            print ("I'm less than 1!")
            print ("Goodbye Cruel World!")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "4":
        # Introduction to Python  Exercize-4
        #    Extend previous example to include conditionals for "elif" and "else"
        print ("Helloworld!")
        num = 1
        if num < 1:
           print ("I'm less than 1!")
           print ("Cruel World!")
        elif num == 1:
           print ("I’m equal to 1!")
        else:
           print ("I’m greater than 1! ")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "5":
        # Introduction to Python  Exercize-5
        #    Building on Exercise 4.  Adding input from the user.  Note: This will return an error
        print ("Helloworld!")
        num = 1
        num = input("Input a number: ")
        if num < 1:
            # The next statements won't happen because of the error in the previous line
           print ("I'm less than 1!")
           print ("Cruel World!")
        elif num == 1:
           print ("I’m equal to 1!")
        else:
           print ("I’m greater than 1! ")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "6":
        # Introduction to Python  Exercize-6
        #    Correcting the Error in Exercise #5
        print ("Helloworld!")
        num = 1
        num = int(input("Input a number: "))
        if num < 1:
           print ("I'm less than 1!")
           print ("Cruel World!")
        elif num == 1:
           print ("I’m equal to 1!")
        else:
           print ("I’m greater than 1! ")
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "7":
        # Introduction to Python  Exercize-7
        #    Correcting the Error in Exercise #5
        print ("Helloworld!")
        num = 1
        num = int(input("Input a number: "))
        if num < 1:
           print ("I'm less than 1!")
           print ("Goodby Cruel World!")
        elif num == 1:
           print ("I’m equal to 1!")
        else:
           print ("Value is: " + str(num))
           print ("Value is: ", num)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "8":
        # Introduction to Python  Exercize-8
        #    Iteration using For Statement
        num = 1
        
        for count in range(3):
           num = int(input("Input a number: "))
           if num < 1:
              print ("I'm less than 1!")
              print ("Goodby Cruel World!")
           elif num == 1:
              print ("I’m equal to 1!")
           else:
              print ("Value is: " + str(num))
              print ("Value is: ", num)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "9":
        # Introduction to Python  Exercize-9
        #    Iteration using While Statement
        num = 1

        while num > 0:
           num = int(input("Input a number: "))
           if num < 1:
              print ("I'm less than 1!")
              print ("Goodby Cruel World!")
           elif num == 1:
              print ("I’m equal to 1!")
           else:
              print ("Value is: " + str(num))
              print ("Value is: ", num)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "10":
        # Introduction to Python  Exercize-10
        #    Manipulating lists
        print ("MyList Example\n")
        MyList = []
        print (len(MyList), MyList)
        MyList = ['Fred', "Barney", 3, 5.5]
        print (len(MyList), MyList) 
        print()
        MyList.append("Wilma")
        MyList.append("Betty")
        print (len(MyList), MyList) 
        print()
        MyList.remove(3)
        MyList[2] = MyList[1]
        MyList[1] = MyList[3]
        MyList[3] = MyList[4]
        MyList.remove(MyList[3])
        print (len(MyList), MyList)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "11":
        # Introduction to Python  Exercize-11
        #    Manipulating lists - Advanced
        MyList1 = ["Alpha", "Beta", "Gamma", "Delta", "Episilon", "Ztea", "Eta", "Theta", "Iota"]
        MyList2 = MyList1[1:3]
        MyList3 = MyList1[:3]
        MyList4 = MyList1[3:]
        MyList5 = MyList1[:]
        print ("MyList1 Length:", len(MyList1), MyList1, id(MyList1))
        print ("MyList2 Length:", len(MyList2), MyList2, id(MyList2))
        print ("MyList3 Length:", len(MyList3), MyList3, id(MyList3))
        print ("MyList4 Length:", len(MyList4), MyList4, id(MyList4))
        print ("MyList5 Length:", len(MyList5), MyList5, id(MyList5))
        print()
        MyList1 = ["Alpha", "Beta", "Gamma"]
        MyList2 = MyList1
        print (len(MyList1), MyList1)
        print (len(MyList2), MyList2)
        MyList1.append("Delta")
        MyList2.append("Episilon")
        print (len(MyList1), MyList1, id(MyList1))
        print (len(MyList2), MyList2, id(MyList2))
        print()
        MyList2 = list(MyList1)
        print (len(MyList1), MyList1, id(MyList1))
        print (len(MyList2), MyList2, id(MyList2))
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "12":
        # Introduction to Python  Exercize-12
        #    Manipulating lists in lists - Advanced
        MyList = [["red",[255,0,0]],["green",[0,255,0]],["blue",[0,0,255]],["yellow",[255,255,102]]]
        for i in range(len(MyList)):
            print (MyList[i][0],end="")
            for j in range(len(MyList[i][1])):
                print ("\t",MyList[i][1][j])
        print()
        import numpy as np
        aList = np.arange(8)
        print ('Starting with an 8-element array:')
        print (aList)
        bList = aList.reshape(4,2)
        print ('\nReshaped to a 4x2 array:')
        print (bList,"\n")
        print()
        aList = np.arange(9)
        print ('Starting with a 9-element array:')
        print (aList)
        bList = aList.reshape(3,3)
        print ('\nReshaped to a 3x3 array:')
        print (bList,"\n")
        print()
        # Other ways to initialize a list
        print("Creating Initialized lists with numpy.")
        aList = np.zeros(7)
        bList = np.ones(7)
        print("List of zeros: ",aList)
        print("List of ones:  ",bList)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "13":
        # Introduction to Python  Exercize-13
        #    Manipulating Tuples in Python
        print("\nMy Tuple Example:")
        MyTuple = ()
        print (len(MyTuple), MyTuple)
        MyTuple = ("Bldg5", "Switch01", "1/0/1", 20)
        print (len(MyTuple), MyTuple)
        MyTuple1 = ("Bldg5", "Switch02", "1/0/1", 5)
        print (len(MyTuple1), MyTuple1)
        print (MyTuple[1],"GigE",MyTuple[2]," in ",MyTuple[0]," has ", MyTuple[3]-MyTuple1[3], "more errors than ",MyTuple1[1])
        print()
        for i in range(len(MyTuple)):
            print (MyTuple[i])
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "14":
        # Introduction to Python  Exercize-14
        #    List of Tuples
        print("\nMy Tuple Example:")
        MyTuple = ()
        print (len(MyTuple), MyTuple)
        MyTuple = ("Bldg5", "Switch01", "1/0/1", 20)
        print (len(MyTuple), MyTuple)
        MyTuple1 = ("Bldg5", "Switch02", "1/0/1", 5)
        print (len(MyTuple1), MyTuple1)
        print (MyTuple[1],"GigE",MyTuple[2]," in ",MyTuple[0]," has ",
               MyTuple[3]-MyTuple1[3],
               "more errors than ",MyTuple1[1])
        print()
        IntList = []
        IntList.append(MyTuple)
        IntList.append(MyTuple1)
        print (len(IntList), IntList)
        print (IntList[1][1])
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "15":
        print("\nMy Dictionary Example:")
        for count in range(5):
            my_function()
            print(count)
        print()
        MyD = {"Type":"Cat9K","Ports":48,"Name":"Switch1","Loc":"Building 5"}
        print (len(MyD), MyD)
        print()
        print (MyD["Name"]," in ", MyD["Loc"]," is a ", MyD["Type"])
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "16":
        print("\nmy_function()  Examples:")
        for count in range(5):
                my_function()
        print("My Count ",count)
        print()
        for count in range(5):
                my_function1(count)
        print()
        for count in range(5):
            npi = my_function2(count)
            print (count, "times PI = ", npi)
        print()
        x = 5
        scopeFun(x)
        print("Main(): x = ", x)
        print()
        scopeGlob()
        print("Main(): x = ", x)
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "17":
        r = int(input("Input the radius of a circle: "))
        prs, rs = MathFun(r)
        print("Radius = ", r, "\tr^2 = ", rs, "\tThe area of the circle is = ", prs)
        print("\n=======(",Response, ")=======\n")
        
    elif Response =="18":
        food={"vegetables":["carrots","kale","cucumber","tomato"]}
        for veg in food["vegetables"]:
            print(veg)
        print()
        cars={"sports":{"Turbo 911":"Porsche","Viper":"Dodge","Corvette":"Chevy"}}
        for auto in cars["sports"]:
            print(auto, cars["sports"][auto])
        print()
        Devices={"WLC":"5520","Switch":"Nexus9k","Router":"ISR4221"}
        for var in Devices:
            print("Device: " + var + " Model " + Devices[var])
        print()
        myvar={"switches":{"fixed":["2900","3650","3850","9300","9500"]}}
        print(myvar["switches"]["fixed"][0])
        print("My list of access switches are:", end=" ")
        for f in myvar["switches"]["fixed"]:
            print(f, end=" ")
        print()
        myvar={"type":"donut","flavors":{"flavor":[{"type":"chocolate","id":1001},{"type":"glazed","id":1002},{"type":"sprinkled","id":1003}]}}
        print("Id: " + str(myvar[flavors][flavor][0]["id"]) + " type " + myvar[flavors][flavor][0]["type"]) 
        for f in myvar[flavors][flavor]:
            print("Id is: " + str(f["id"]) + " type is: " + f["type"])
        print("\n=======(",Response, ")=======\n")
        
    elif Response == "19":
        
        print("\n=======(",Response, ")=======\n")
    elif Response =="20":
        import pip
        installed_packages = pip.get_installed_distributions()
        installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
        for i in installed_packages])
        print(installed_packages_list)
        print("\n=======(",Response, ")=======\n")
    else:
        print ("Unrecognized Exercize Number.  Value must be in range (1-",NumExercises,").")
        print("\n=======(",Response, ")=======\n")
