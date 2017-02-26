# this class can solves matrix questions which have matrix with variables
from _operator import ne
from pydoc import ispackage
from sympy.printing.mathml import mathml, print_mathml
from sympy.abc import x

from sympy import *
import re


class Simplifya:
    def solve(self):



        # print(answer)

        with open('questions/simplifya_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)

        filein.close()

        with open('answers/simplifya_1_3.txt') as filein:
            answer = "".join(line.rstrip() for line in filein)

        filein.close()

        with open('marking scheme/simplifya_1.txt') as filein:
            ms = "".join(line.rstrip() for line in filein)

        filein.close()

        marks = 0

        listms = ms.split("=")



        print("\nQuestion : " + data + "\n")
        print("Student answer : "+answer + "\n")
        print("-----------------------------------------------")

        # print_mathml(x+2)
        expression = simplify(sympify(data))
        # print(expression)
        if answer != "" :
            ans = simplify(sympify(answer))

        if answer == "":
            print("You have not answered the question.\nMarks = "+str(marks))
        elif answer.replace(" ","") == str(expression).replace(" ",""):
            marks = listms[1]
            print("Correct \nMarks = " + marks)
        elif ans == expression and len(answer.replace(" ","")) == len(str(expression).replace(" ","")):
            marks = listms[1]
            print("Correct \nMarks = " + marks)
        else:
            if simplify(sympify(answer)+sympify(expression)) == 0:
                print("Answer is negated")
                print("Incorrect\nMarks = " + str(marks))
            # elif answer.find(str(simplify(sympify(answer)+sympify(expression)/2))) != -1 :
            # elif simplify(simplify(sympify(str(sympify(str(expression)))+"-("+str(simplify(simplify(sympify(answer)+sympify(expression))/2))+")")) + sympify(str(sympify(str(expression)+"-("+str(simplify(sympify(answer)+sympify(expression)))+")/2")))) == 0 :
            elif solve(sympify(answer),simplify(sympify(answer)+sympify(expression)/2)) == solve(sympify(expression),simplify(sympify(answer)+sympify(expression)/2)) :
                coeffx = sympify(answer).coeff(sympify(str(expression)+"-("+str(simplify(sympify(answer)+sympify(expression)))+")/2"))
                anscount = str(simplify(sympify(answer))).replace(" ","").replace("+"," +").replace("-"," -").split(" ")
                expcount = str(simplify(sympify(expression))).replace(" ","").replace("+"," +").replace("-"," -").split(" ")

                # if len(anscount) == len (expcount):
                #     print("Simplification is wrong")
                #     # print(" "+ str(sympify(str(expression)+"-("+str(simplify(sympify(answer)+sympify(expression)))+")/2")*(-1))+" in the answer should be "+str(sympify(str(expression)+"-("+str(simplify(sympify(answer)+sympify(expression)))+")/2")))
                # # print(" " + str(coeffx) + " in the answer should be " + str(
                # #     sympify(str(expression) + "-(" + str(simplify(sympify(answer) + sympify(expression))) + ")/2") * (
                # #     -1)))
                # elif len (expcount) >len(anscount):
                #     print("Some variables are missing in your simplification")
                # else :
                #     print("Additional variables are present in your answer")
                print("Simplification is wrong")
                print("Incorrect\nMarks = " + str(marks))
            else:
                print("Incorrect\nMarks = " + str(marks))

        print("-----------------------------------------------")


Simplifya().solve()
