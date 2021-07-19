def CountToNumber():
    x = int(input("please enter a number: "))
    y = 0
    

    while y < x:
        print(y)
        y += 1
    

        if y == x:
            print(x)
            

            if x <= 100 * 10000:
                break 
            else:
                pass

CountToNumber()