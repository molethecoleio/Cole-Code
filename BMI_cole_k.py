#Made by Cole Kleinebekel, kleinebekelc@gmail.com. Have a good day, and as always stay kind!
x = ['Nice Try Ben, thats a string', 'Please enter a positive number... ben']
cole = True
while cole:
    while True:
        type = input('0 for impiral, 1 for standard?')
        try:
            type = int(type)
        except:
            print(x[0])
            continue
        if type != 1 and type != 0:
            print(x[1] + " 0 and 1 are only acceptable answers")
            continue
        break
    
    if  type == 0:
        while True:
            heightF = input('How many feet tall are you?')
            try:
                heightF = int(heightF)
            except:
                print(x[0])
                continue
            if heightF < 1:
                print(x[1])
                continue
            break
        
        while True:
            heightI = input('How many inches on top of the feet are you?')
            try:
                heightI = int(heightI)
            except:
                print(x[0])
                continue
            if heightI < 1 or heightI > 11:
                print(x[1] + "1-11 are only acceptables")
                continue
            break
        
        while True:
            weight = input("How much do you weigh in pounds?")
            try:
                weight = int(weight)
            except:
                print(x[0])
                continue
            if weight < 1:
                print(x[1])
                continue
            break
        
        print('Your BMI is', 703*(weight/((heightF*12 + heightI)**2)))
        
    if  type == 1:
        
        while True:
            heightm = input('How many meters tall are you?')
            try:
                heightm = int(heightm)
            except:
                print(x[0])
                continue
            if heightm < 1 :
                print(x[1])
                continue
            break
        
        while True:
            weightKG = input('How much killigrams do you weigh?')
            try:
                weightKG = int(weightKG)
            except:
                print(x[0])
                continue
            if weightKG < 1 :
                print(x[1])
                continue
            break
        
        print('your bmi is ', weightKG/(heightm**2))
        
    cole = False
    checker = input('would you like to play again y or n')
    if checker == 'y':
        cole = True
