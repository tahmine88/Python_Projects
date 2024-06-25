countinue = True
for i in range(1,101):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 5 == 0:
                result = ("FizzBuzz")
            else:
                result = ('Fizz')
        elif i % 5 == 0:
            result = ("Buzz")
        else:
            result = (i)
        number = (input("YOU: "))
        if int(number) != result:
            print("YOU SAY THE WRONG NUMBER!!")
            countinue = False
            break

    else:
        if countinue == True:
            if i % 3 == 0:
                if i % 5 == 0:
                    print("ME: FizzBuzz")
                else:
                    print('ME: Fizz')
            elif i % 5 == 0:
                print("ME: Buzz")
            else:
                print("ME: "+ str(i))
        else:
            break

    password_part_2 += rand_number
print("Your password is:", password_part_1 + "_" + password_part_2)
