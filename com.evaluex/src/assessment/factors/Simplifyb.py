# this class can solves matrix questions which have matrix with variables
from _operator import ne
from pydoc import ispackage

from sympy import *
import re


class Simplifyb:
    def solve(self):

        with open('questions/simplifyb_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)

        filein.close()

        listquestion = data.split("answer=")
        # answer = input("Choose the expressions that give " + listquestion[1] + " when simplified. \n " + listquestion[0] + "\n")

        with open('answers/simplifyb_1.txt') as filein:
            answer = ",".join(line.rstrip() for line in filein)

        filein.close()

        with open('marking scheme/simplifyb_1.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")

        marks = 0;


        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        ms2 = listms[1]
        ms3 = listms[2]

        listms1 = ms1.split("=")
        marks1 = listms1[1].replace(" ","")
        listms2 = ms2.split("=")
        marks2 = listms2[1].replace(" ","")
        if ms3 != "":
            listms3 = ms3.split("=")
            marks3 = listms3[1].replace(" ","")

        liststudentans = answer.split(",")
        listquestion0 = listquestion[0].split(",")


        # # print(listquestion[0])
        # print(listquestion[1])
        # # print(listquestion0[0])
        # print(listquestion0[1])
        # # print(liststudentans[0])
        # print(liststudentans[1])
        # # print(listquestion0[1].replace(listquestion[1],liststudentans[1]))
        # print((str(listquestion0[1]).replace(listquestion[1],liststudentans[1])))

        listanswers = []


        for expression in listquestion0:  # Second Example
            if simplify(sympify(expression)) == sympify(listquestion[1]) :
                listanswers.append(expression)
        #
        # for expression in listquestion0:  # Second Example
        #     if simplify(sympify(expression)) == sympify(listquestion[1]):
        #         print(expression)

        # if liststudentans,listquestion0 == 0:
        #     print("correct")


        listz = []
        i = 0
        for a in liststudentans:  # Second Example
            for elements in listanswers :
                if str(a).replace(" ","")==str(elements).replace(" ",""):
                    listz.insert(i,a)
                    i += 1

        if len(listanswers) == len(listz):
            if len(liststudentans) - len(listz) == 1:
                marks = marks3
                print("Partially correct \nMarks = " + marks)
            else :
                marks = marks1
                print("Correct \nMarks = " + marks)
        elif len(listanswers) - len(listz) == 1 : #no of right ans taken from marking scheme
            marks = marks2
            print("Partially correct \nMarks = " + marks)
        elif len(listz) - len(listanswers) == 1:  #no of wrong ans -- CHECK
            print("Partially correct \nMarks = " + marks)
        else :
            print("Incorrect\nMarks = " + str(marks))




        # print(str(simplify(sympify(listquestion0[1].replace(listquestion[1],liststudentans[1]).replace(" ","")))))
        #
        # if liststudentans[0].replace(" ","")  == listquestion[1].replace(" ","")  :
        #     if str(simplify(sympify(listquestion0[1].replace(listquestion[1],liststudentans[1]).replace(" ","")))) == listquestion0[0].replace(" ","") :
        #         print("correct")
        #     else:
        #         print("Wrong")
        #
        # # if liststudentans[0].replace(" ","")  == listquestion[1].replace(" ","")  :
        # #     if simplify(sympify(listquestion0[1].replace(listquestion[1],liststudentans[1]))) == sympify(listquestion0[0]) :
        # #         print("correc")
        # else :
        #     print("Wrong")

        print("-----------------------------------------------")


Simplifyb().solve()
