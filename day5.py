#this project about the middle score of a high students:
# students_hight = input('Input a list of student hights: ').split()
# for n in range(0,len(students_hight)):
#     students_hight[n] = int(students_hight[n])
# count = 0
# summ = 0
# for i in students_hight:
#     summ += i
#     count += 1
# print(int(summ/count))


#this progect can say the highst score:
# student_score = input("Input a list of student score: ").split()
# for n in range(0,len(student_score)):
#     student_score[n] = int(student_score[n])
# score = 0
# for i in student_score:
#     if i > score:
#         score = i
# print(score)

# it is the gose formol:
# total = 0
# for i in range(2,102,2):
#     total += i
# print(total)


#this project is FizzBuzz:
# countinue = True
# for i in range(1,101):
#     if i % 2 == 0:
#         if i % 3 == 0:
#             if i % 5 == 0:
#                 result = ("FizzBuzz")
#             else:
#                 result = ('Fizz')
#         elif i % 5 == 0:
#             result = ("Buzz")
#         else:
#             result = (i)
#         number = (input("YOU: "))
#         if int(number) != result:
#             print("YOU SAY THE WRONG NUMBER!!")
#             countinue = False
#             break

#     else:
#         if countinue == True:
#             if i % 3 == 0:
#                 if i % 5 == 0:
#                     print("ME: FizzBuzz")
#                 else:
#                     print('ME: Fizz')
#             elif i % 5 == 0:
#                 print("ME: Buzz")
#             else:
#                 print("ME: "+ str(i))
#         else:
#             break


#this project can make a password for you
import random
letter = ["a",'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = ['1','2','3','4','5','6','7','8','9','10']
password_part_1  = ""
password_part_2 = ""
print("welcome to password maker!")
n_letter = int(input("How many letter do you want to have?"))
n_number = int(input("How many number do you want to have?"))
for i in range(0,n_letter):
    rand_letter = random.choice(letter)
    password_part_1 += rand_letter
for i in range(0,n_number):
    rand_number = random.choice(number)
    password_part_2 += rand_number
print("Your password is:", password_part_1 + "_" + password_part_2)
