for x in range(10): #iterate for loop
    if x % 20 == 0: #condition 1
        print("twist" , x)

    elif x % 15 == 0: #condition 2
        pass      #pass statement

    elif x % 5 == 0: #condition 3
        print("fizz" , x)   #display result

    elif x % 3 == 0: #condition 4
        print("buzz" , x)   #display result

    else:       #condition 5
        print(x)   #display result