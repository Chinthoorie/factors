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
    partMarkLine = 0
    finalMarkLine = 0
    def get(self):

        # questions/subject_1.txt
        # answers/subject_1_3.txt
        # questions/trainingset/subject/q3.txt
        # answers/trainingset/subject/q3/a2.txt


        with open('subject_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)

        filein.close()

        with open('subject_1_6.txt') as filein:
            answer = "\n".join(line.rstrip() for line in filein)

        filein.close()

        with open('subjectms.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum
        global partMarkLine
        global finalMarkLine

        isPartiallyCorrect = false
        isFinalAnswerCorrect = false
        isStepIncorrect = false
        incorrectStepNum = 0
        partMarkLine = 0
        finalMarkLine = 0

        marks = 0;
        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        listms1 = ms1.split("=")
        marks1 = listms1[1]

        if len(listms) == 3:
            ms3 = listms[2]
            if ms3 != "":
                listms3 = ms3.split("=")
                marks3 = listms3[1]

        if answer != "" :
            listans = answer.replace(" ", "").split("\n")
        else :
            listans = []

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")

        global totmarks
        totmarks = 0
        if answer == "":
            print("You have not answered the question.\nMarks = " + str(marks))
        else:
            for line in listans:
                gotmarks = solveQ(data,line,ms,listans.index(line))
                totmarks = gotmarks + totmarks

        print("\n\nTotal marks = " + str(totmarks) + " out of " + str(marks1))
        print("-----------------------------------------------")


def solveQ(data,answer,ms,linenum):
        print("\nStep " + str(linenum + 1) + " :")
        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum
        global totmarks
        global partMarkLine
        global finalMarkLine

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
        queslhs = listequ[0]
        quesrhs = listequ[1]
        stlhs = question[1].replace(" ", "")

        if answer != "":
            answers = answer.split("=")
            anslhs = answers[0].replace(" ", "")
            ansrhs = answers[1].replace(" ", "")
        else :
            answers = []
            anslhs = ""
            ansrhs = ""

        wronganswer = ""

        coeffanslhs = sympify(str(queslhs + "-(" + quesrhs + ")")).coeff(sympify(anslhs))

        if isStepIncorrect == true :
            # print("Correct the error in line "+ str(incorrectStepNum) +" to get full marks")
            print("This step is not marked due to the error in step "+str(incorrectStepNum)+"\nMarks = 0")
        elif anslhs == stlhs:
            # if str(simplify(sympify(listq0[1].replace(listq[1],lista[1]).replace(" ","")))) == listq0[0].replace(" ","") :
            exp = str(simplify(sympify(sympify(quesrhs).subs(stlhs, ansrhs))))
            exp1 = sympify(str(solve(queslhs + "-(" + quesrhs + ")", stlhs)).replace("[", "").replace("]", ""))
            if exp1 == sympify(ansrhs):
                # print("Correct")
                if isFinalAnswerCorrect == false:
                    marks = int(marks1) - totmarks
                    finalMarkLine = linenum
                    print("Final answer is correct \nMarks = " + str(marks))
                else:
                    print("Step is correct.\nAlready provided the marks for the final answer in step "+str(finalMarkLine+1))

                isFinalAnswerCorrect = true

            elif exp == queslhs.replace(" ", ""):
                if isFinalAnswerCorrect == false:
                    marks = int(marks1) - totmarks
                    finalMarkLine = linenum
                    print("Final answer is correct \nMarks = " + str(marks))
                else:
                    print("Step is correct.\nAlready provided the marks for the final answer in step "+str(finalMarkLine+1))
                isFinalAnswerCorrect = true
            # else:
            #     print("Incorrect\nMarks = " + str(marks))
            elif anslhs != queslhs:
                if queslhs.find(str("-" + stlhs)) != -1:
                    if sympify(ansrhs) == sympify(
                            str(solve(queslhs + "-(" + quesrhs + ")", stlhs)).replace("[", "").replace("]", "")):
                        if isFinalAnswerCorrect == false:
                            marks = int(marks1) - totmarks
                            finalMarkLine = linenum
                            print("Final answer is correct \nMarks = " + str(marks))
                        else:
                            print("Step is correct.\nAlready provided the marks for the final answer in step "+str(finalMarkLine+1))
                        # print("Final answer is correct \nMarks = " + str(marks))
                        isFinalAnswerCorrect = true
                    else:
                        # print("Incorrect\nMarks = " + str(marks))
                        wronganswer = answer

                elif quesrhs.find(str("-" + stlhs)) != -1:
                    if sympify(ansrhs) == sympify(
                            str(solve(quesrhs + "-(" + queslhs + ")", stlhs)).replace("[", "").replace("]", "")):
                        if isFinalAnswerCorrect == false:
                            marks = int(marks1) - totmarks
                            finalMarkLine = linenum
                            print("Final answer is correct \nMarks = " + str(marks))
                        else:
                            print("Step is correct.\nAlready provided the marks for the final answer in step " + str(finalMarkLine + 1))
                        isFinalAnswerCorrect = true
                    else:
                        wronganswer = answer
                        # print("Incorrect\nMarks = " + str(marks))
                        # if isStepIncorrect == false:
                        #     incorrectStepNum = linenum + 1
                        # isStepIncorrect = true
                else:
                    wronganswer = answer
                    # print("Incorrect\nMarks = " + str(marks))
                    # if isStepIncorrect == false:
                    #     incorrectStepNum = linenum+1
                    # isStepIncorrect = true


            else:
                wronganswer = answer
                # print("Incorrect\nMarks = " + str(marks))
                # if isStepIncorrect == false:
                #     incorrectStepNum = linenum + 1
                # isStepIncorrect = true


        # print(solve(quesrhs+"-"+queslhs,stlhs))
        elif sympify(str(solve(queslhs+"-("+quesrhs+")",anslhs)).replace("[", "").replace("]", "")) == simplify(expand(sympify(ansrhs))):
                        # sympify(str(solve(queslhs+"-("+quesrhs+")",anslhs)).replace("[", "").replace("]", "")) == sympify(ansrhs):
            # print(isPartiallyCorrect)

            if simplify(sympify(queslhs+"-("+quesrhs+")")) == simplify(sympify(str(anslhs+"-("+ansrhs+")").replace(" ","")))*coeffanslhs and coeffanslhs != 1:
                if isPartiallyCorrect == false:
                    marks = marks2
                    partMarkLine = linenum
                    print("Partially correct \nMarks = " + str(marks))
                else:
                    print("Step is correct.\nAlready provided the marks for partial correctness in step " + str(partMarkLine + 1))
                isPartiallyCorrect = true
            elif simplify(sympify(queslhs+"-("+quesrhs+")")) == simplify(sympify(str(anslhs+"-("+ansrhs+")").replace(" ","")))*coeffanslhs and coeffanslhs == 1:
                print("Re-written the given formula")
            else:
                wronganswer = answer
        elif sympify(str(solve(queslhs+"-("+quesrhs+")",anslhs)).replace("[", "").replace("]", "")) == simplify(sympify(ansrhs)):
            if simplify(sympify(queslhs+"-("+quesrhs+")")) == simplify(sympify(str(anslhs+"-("+ansrhs+")").replace(" ","")))*coeffanslhs and coeffanslhs != 1:
                if isPartiallyCorrect == false:
                    marks = marks2
                    partMarkLine = linenum
                    print("Partially correct \nMarks = " + str(marks))
                else:
                    print("Step is correct.\nAlready provided the marks for partial correctness in step " + str(partMarkLine + 1))
                isPartiallyCorrect = true
            elif simplify(sympify(queslhs+"-("+quesrhs+")")) == simplify(sympify(str(anslhs+"-("+ansrhs+")").replace(" ","")))*coeffanslhs and coeffanslhs == 1:
                print("Re-written the given formula")
            else:
                wronganswer = answer
        else:
            wronganswer = answer
            # print("Incorrect\nMarks = " + str(marks))
            # if isStepIncorrect == false:
            #     incorrectStepNum = linenum + 1
            # isStepIncorrect = true

        if wronganswer != "":
            if sympify(str(solve(queslhs+"-("+quesrhs+")",anslhs)).replace("[", "").replace("]", "")) == sympify(ansrhs):
                if isPartiallyCorrect == false:
                    marks = marks2
                    partMarkLine = linenum
                    print("Partially correct \nMarks = " + str(marks))
                else:
                    print("Step is correct.\nAlready provided the marks for partial correctness in step "+str(partMarkLine+1))
                isPartiallyCorrect = true
            # elif simplify(sympify(ansrhs) + sympify(
            #                 str(solve(queslhs + "-(" + quesrhs + ")", stlhs)).replace("[", "").replace("]", ""))) == 0:
            #     print("RHS is negated")
            #     print("Incorrect\nMarks = " + str(marks))
            #     if isStepIncorrect == false:
            #         incorrectStepNum = linenum + 1
            #     isStepIncorrect = true
            elif simplify(sympify(ansrhs) + sympify(
                            str(solve(queslhs + "-(" + quesrhs + ")", anslhs)).replace("[", "").replace("]", ""))) == 0:
                print("RHS is negated")
                print("Incorrect\nMarks = " + str(marks))
                if isStepIncorrect == false:
                    incorrectStepNum = linenum + 1
                isStepIncorrect = true
            else :
                print("Incorrect\nMarks = " + str(marks))
                if isStepIncorrect == false:
                    incorrectStepNum = linenum + 1
                isStepIncorrect = true


        return int(marks)


Subject().get()
