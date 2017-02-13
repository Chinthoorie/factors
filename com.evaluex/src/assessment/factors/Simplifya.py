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

        with open('answers/simplifya_1_1.txt') as filein:
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
        ans = simplify(sympify(answer))


        if answer.replace(" ","") == str(expression).replace(" ",""):
            marks = listms[1]
            print("Correct \nMarks = " + marks)
        elif ans == expression and len(answer.replace(" ","")) == len(str(expression).replace(" ","")):
            marks = listms[1]
            print("Correct \nMarks = " + marks)
        else:
            print("Incorrect\nMarks = " + str(marks))

        print("-----------------------------------------------")


Simplifya().solve()
