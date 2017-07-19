# this class can solves matrix questions which have matrix with variables
from _operator import ne
from pydoc import ispackage

from sympy import *
import re


class LCM:
    def solve(self):

        with open('questions/LCM_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)
        filein.close()

        # answer = input("Find the LCM of " + data + "\n")

        with open('answers/LCM_1.txt') as filein:
            answer = "".join(line.rstrip() for line in filein)

        filein.close()

        with open('marking scheme/LCM_1.txt') as filein:
            ms = "".join(line.rstrip() for line in filein)

        filein.close()

        marks = 0


        listms = ms.split("=")


        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")


        if simplify(sympify(answer.replace(" ",""))) == gcd(sympify(data.replace(" ",""))) :
            print("You have found the greatest common divisor instead of lowest common multiple")
            print("Incorrect\nMarks = " + str(marks))
        elif answer.find('(') == -1:
            if sympify(answer) == lcm(sympify(data)):
                marks = listms[1].replace(" ","")
                print("Correct \nMarks = " + marks)
            else :

                print("Incorrect\nMarks = " + str(marks))
        # x**2*(x+2)
        elif answer.find('*(') != -1 or answer.find(')*') != -1:
            if answer.find('(') and answer.find(')') != -1 :
                if sympify(answer)  == factor(lcm(sympify(data))):
                    marks = listms[1].replace(" ","")
                    print("Correct \nMarks = " + marks)
                else :
                    temp = simplify(sympify("("+str(lcm(sympify(data.replace(" ","")))).replace(" ","")+")/("+str(answer)+")"))
                    print(str(lcm(sympify(data.replace(" ","")))))
                    print("Power of "+ str(temp)+" is incorrect")
                    print("Incorrect\nMarks = " + str(marks))
            else :
                print("Incorrect\nMarks = " + str(marks))
        # x**2(x+2)
        elif answer.replace(" ", "").endswith(')'):
            if sympify(answer.replace(" ", "").replace("(", "*(")) == factor(lcm(sympify(data))):
                marks = listms[1].replace(" ","")
                print("Correct \nMarks = " + marks)
            else:
                print("Incorrect\nMarks = " + str(marks))
        # (x-2)x**2
        elif answer.replace(" ", "").startswith('('):
            if sympify(answer.replace(" ", "").replace(")", ")*")) == factor(lcm(sympify(data))):
                marks = listms[1].replace(" ","")
                print("Correct \nMarks = " + marks)
            else:
                print("Incorrect\nMarks = " + str(marks))
        else:
            print("Incorrect\nMarks = " + str(marks))

        print("-----------------------------------------------")


LCM().solve()
