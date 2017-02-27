# solve type 4
from _operator import ne
from pydoc import ispackage

from sympy import *
import re
from sympy.abc import v, u, a, s


# v,u,a,s = Symbol('v,u,a,s')

class Subject:
    totmarks = 0
    isPartiallyCorrect = false
    isFinalAnswerCorrect = false
    isStepIncorrect = false
    incorrectStepNum = 0
    def get(self):
        with open('questions/subject_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)

        filein.close()

        # listq = data.split(",")
        # answer = input("Change " + listq[1] + " the subject of " + listq[0] + "\n")

        with open('answers/subject_1_3.txt') as filein:
            answer = "\n".join(line.rstrip() for line in filein)

        filein.close()

        with open('marking scheme/subject_1.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum

        isPartiallyCorrect = false
        isFinalAnswerCorrect = false
        isStepIncorrect = false
        incorrectStepNum = 0

        marks = 0;
        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        listms1 = ms1.split("=")
        marks1 = listms1[1]

        # ms2 = listms[1]
        # listms2 = ms2.split("=")
        # marks2 = listms2[1]

        if len(listms) == 3:
            ms3 = listms[2]
            if ms3 != "":
                listms3 = ms3.split("=")
                marks3 = listms3[1]

        listans = answer.replace(" ", "").split("\n")
        # print(isPartiallyCorrect)

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")

        global totmarks
        totmarks = 0
        for line in listans:
            gotmarks = solveQ(data,line,ms,listans.index(line))
            totmarks = gotmarks + totmarks

        # if totmarks>int(marks1):
        #     totmarks = int(marks1)
        print("\n\nTotal marks = " + str(totmarks) + " out of " + str(marks1))
        print("-----------------------------------------------")


def solveQ(data,answer,ms,linenum):
        print("\nline " + str(linenum + 1) + " :")
        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum
        # print(isPartiallyCorrect)
        marks = 0;
        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        listms1 = ms1.split("=")
        marks1 = listms1[1]

        ms2 = listms[1]
        listms2 = ms2.split("=")
        marks2 = listms2[1]

        if len(listms) == 3:
            ms3 = listms[2]
            if ms3 != "":
                listms3 = ms3.split("=")
                marks3 = listms3[1]

        # lista = answer.split("=")
        # listq0 = listq[0].split("=")

        question = data.split(",")
        qequation = question[0].replace(" ", "")
        listequ = qequation.split("=")
        stlhs = question[1].replace(" ", "")

        answers = answer.split("=")
        anslhs = answers[0].replace(" ", "")
        ansrhs = answers[1].replace(" ", "")

        wronganswer = ""

        coeffanslhs = sympify(str(listequ[0] + "-(" + listequ[1] + ")")).coeff(sympify(anslhs))

        if isStepIncorrect == true :
            # print("Correct the error in line "+ str(incorrectStepNum) +" to get full marks")
            print("This line is not marked due to the error in line "+str(incorrectStepNum)+"\nMarks = 0")
        elif anslhs == stlhs:
            # if str(simplify(sympify(listq0[1].replace(listq[1],lista[1]).replace(" ","")))) == listq0[0].replace(" ","") :
            exp = str(simplify(sympify(sympify(listequ[1]).subs(stlhs, ansrhs))))
            if exp == listequ[0].replace(" ", ""):
                if isFinalAnswerCorrect == false:
                    marks = int(marks1) - totmarks
                else:
                    print("Already provided the marks for the final answer in earlier steps")
                print("Final answer is correct \nMarks = " + str(marks))
                isFinalAnswerCorrect = true
            # else:
            #     print("Incorrect\nMarks = " + str(marks))
            elif anslhs != listequ[0]:
                if listequ[0].find(str("-" + stlhs)) != -1:
                    if sympify(ansrhs) == sympify(
                            str(solve(listequ[0] + "-(" + listequ[1] + ")", stlhs)).replace("[", "").replace("]", "")):
                        if isFinalAnswerCorrect == false:
                            marks = int(marks1) - totmarks
                        else:
                            print("Already provided the marks for the final answer in earlier steps")
                        print("Final answer is correct \nMarks = " + str(marks))
                        isFinalAnswerCorrect = true
                    else:
                        print("Incorrect\nMarks = " + str(marks))
                elif listequ[1].find(str("-" + stlhs)) != -1:
                    if sympify(ansrhs) == sympify(
                            str(solve(listequ[1] + "-(" + listequ[0] + ")", stlhs)).replace("[", "").replace("]", "")):
                        if isFinalAnswerCorrect == false:
                            marks = int(marks1) - totmarks
                        else:
                            print("Already provided the marks for the final answer in earlier steps")
                        print("Final answer is correct \nMarks = " + str(marks))
                        isFinalAnswerCorrect = true
                    else:
                        print("Incorrect\nMarks = " + str(marks))
                        if isStepIncorrect == false:
                            incorrectStepNum = linenum + 1
                        isStepIncorrect = true
                else:
                    print("Incorrect\nMarks = " + str(marks))
                    if isStepIncorrect == false:
                        incorrectStepNum = linenum+1
                    isStepIncorrect = true

            else:
                print("Incorrect\nMarks = " + str(marks))
                if isStepIncorrect == false:
                    incorrectStepNum = linenum + 1
                isStepIncorrect = true

        # listqf = listq[0].replace("'","").replace(" ","").split("+")
        # else:
        #     listqf = listq[0].replace("'", "").replace(" ","").split("-")
        #

        # print(solve(listequ[1]+"-"+listequ[0],stlhs))
        elif sympify(str(solve(listequ[0]+"-("+listequ[1]+")",anslhs)).replace("[", "").replace("]", "")) == sympify(ansrhs):
                        # sympify(str(solve(listequ[0]+"-("+listequ[1]+")",anslhs)).replace("[", "").replace("]", "")) == sympify(ansrhs):
            # print(isPartiallyCorrect)
            if simplify(sympify(listequ[0]+"-("+listequ[1]+")")) == simplify(sympify(str(anslhs+"-("+ansrhs+")").replace(" ","")))*coeffanslhs :
                if isPartiallyCorrect == false:
                    marks = marks2
                else:
                    print("Already provided the marks for partial correctness in earlier steps")
                print("Partially correct \nMarks = " +str(marks))
                isPartiallyCorrect = true
            else:
                wronganswer = answer

            # if sympify(ansrhs) == sympify(
            #         str(solve(listequ[1] + "-(" + listequ[0] + ")", stlhs)).replace("[", "").replace("]", "")):
            #     marks = int(marks1)-totmarks
            #     print("Final answer is correct \nMarks = " + str(marks))
        else:
            print("Incorrect\nMarks = " + str(marks))
            if isStepIncorrect == false:
                incorrectStepNum = linenum + 1
            isStepIncorrect = true

        if wronganswer != "":
            if sympify(str(solve(listequ[0]+"-("+listequ[1]+")",anslhs)).replace("[", "").replace("]", "")) == sympify(ansrhs):
                if isPartiallyCorrect == false:
                    marks = marks2
                else:
                    print("Already provided the marks for partial correctness in earlier steps")
                print("Partially correct \nMarks = " + str(marks))
                isPartiallyCorrect = true


        # print(sympify(str(listequ[0]+"-("+listequ[1]+")")).coeff(sympify(anslhs)))


        return int(marks)


Subject().get()
