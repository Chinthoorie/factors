#solve question type 5
from _operator import ne
from pydoc import ispackage

from sympy import *
import re
# from schemeread import Scheme


class Evaluate:
    totmarks = 0
    isPartiallyCorrect = false
    isFinalAnswerCorrect = false
    isStepIncorrect = false
    incorrectStepNum = 0
    isData = false
    isSquare = false
    isExpansion = false
    isSubject = false
    expansionStepNum = 0
    lines = 0
    expansionMarks = 0
    squareMarks = 0
    subjectMarks = 0
    operation1 = ""
    gotFinalAnswer = false
    finAnsLine = 0
    totalmarks = 0

    def get(self):
        with open('questions/evaluate_3.txt') as filein:
            data = "\n".join(line.rstrip() for line in filein)

        filein.close()

        with open('student_answer.txt') as filein:
            answer = "\n".join(line.rstrip() for line in filein)

        filein.close()
        with open('markingschemetext.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum
        global isData
        global isSquare
        global isExpansion
        global isSubject
        global expansionStepNum
        global lines
        global expansionMarks
        global squareMarks
        global subjectMarks
        global operation1
        global gotFinalAnswer
        global finAnsLine,totalmarks
        global totmarks

        finAnsLine = 0
        expansionMarks = 0
        squareMarks = 0
        subjectMarks = 0
        isPartiallyCorrect = false
        isFinalAnswerCorrect = false
        isStepIncorrect = false
        incorrectStepNum = 0
        isData = false
        isSquare = false
        isExpansion = false
        isSubject = false
        expansionStepNum = 0
        lines = 0
        gotFinalAnswer = false
        totmarks =0

        marks = 0;
        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[1]
        ms2 = listms[2]
        ms3 = listms[3]
        ms4 = listms[0].replace(" ","").split("=")

        listms1 = ms1.split(",")
        listms11 = listms1[1].split("=")
        marks1 = listms11[1].replace(" ", "")
        step1 = ms1.split("->")
        if step1[0].find("square") != -1:
            operation1 = "square"
            squareMarks = int(marks1)
        elif step1[0].find("expansion") != -1:
            operation1 = "expansion"
            expansionMarks = int(marks1)
        elif step1[0].find("subject") != -1:
            operation1 = "subject"
            subjectMarks = int(marks1)
        else:
            operation1 = step1[0]
        operation1 = step1[0]
        exp1 = step1[1].replace(" ", "")

        listms2 = ms2.split(",")
        listms21 = listms2[1].split("=")
        marks2 = listms21[1].replace(" ", "")
        if listms2[0].find("square") != -1:
            operation2 = "square"
            squareMarks = int(marks2)
        elif listms2[0].find("expansion") != -1:
            operation2 = "expansion"
            expansionMarks = int(marks2)
        elif listms2[0].find("subject") != -1:
            operation2 = "subject"
            subjectMarks = int(marks2)
        else:
            operation2 = listms2[0]

        if ms3 != "":
            listms3 = ms3.split(",")
            listms31 = listms3[1].split("=")
            marks3 = listms31[1].replace(" ", "")
            step3 = listms3[0].split("->")
            if step3[0].find("square") != -1:
                operation3 = "square"
                squareMarks = int(marks2)
            elif step3[0].find("expansion") != -1:
                operation3 = "expansion"
                expansionMarks = int(marks3)
            elif step3[0].find("subject") != -1:
                operation3 = "subject"
                subjectMarks = int(marks3)
            else:
                operation3 = step3[0]
            exp3 = step3[1].replace(" ", "")

        totalmarks = int(ms4[1])


        listans = answer.replace(" ", "").split("\n")
        lines = len(listans)
        # print(isPartiallyCorrect)

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")


        for line in listans:
            gotmarks = solveQ(data, line, ms, listans.index(line))
            totmarks = gotmarks + totmarks

        # if totmarks>int(marks1):
        #     totmarks = int(marks1)
        print("\n\nTotal marks = " + str(totmarks) + " out of " + str(totalmarks))
        print("-----------------------------------------------")

def solveQ(data,answer,ms,linenum):
        print("\nStep " + str(linenum + 1) + " :")
        global isPartiallyCorrect
        global isFinalAnswerCorrect
        global isStepIncorrect
        global incorrectStepNum
        global isData
        global isSquare
        global isExpansion
        global isSubject
        global expansionStepNum
        global lines
        global expansionMarks
        global squareMarks
        global subjectMarks
        global operation1
        global gotFinalAnswer
        global finAnsLine,totalmarks
        global totmarks

        marks = 0
        wronganswer = ""
        listnames = ""

        listques = data.replace(" ","").split("\n")
        # print(listques)

        #generate the answer on the own
        listgenans = []
        listgenansconcept = []


        if operation1.find("square") != -1 :
            listgenans.append(listques[0])
            listgenansconcept.append("data")
            listques0 = listques[0].split("=")
            listgenans.append("("+listques0[0]+")**2=("+listques0[1]+")**2")
            listgenansconcept.append("square")
            listgenans.append(str(expand(sympify("(" + listques0[0] + ")**2"))).replace(" ", "") + "=(" + listques0[1] + ")**2")
            listgenansconcept.append("expansion")
            listgenans.append(str(expand(sympify("("+listques0[0]+")**2"))).replace(" ", "")+"="+str(expand(sympify("("+listques0[1]+")**2"))))
            listgenansconcept.append("expansion")
            listgenans.append(str(listques[1]) + "="+ str(expand(sympify("("+listques0[1]+")**2")))+"-(" +str(simplify(sympify(str((expand(sympify("("+str(listques0[0]).replace(" ","")+")**2"))))+"-("+str(listques[1])+")")))+")")
            listgenansconcept.append("subject")
            listgenans.append(str(listques[1]) + "=" + str(simplify(sympify(str(expand(sympify("(" + listques0[1] + ")**2"))) + "-(" + str(simplify(
                sympify(str((expand(sympify("(" + str(listques0[0]).replace(" ", "") + ")**2")))) + "-(" + str(
                    listques[1]) + ")"))) + ")"))))
            listgenansconcept.append("subject")
        # elif operation1.find("square") != -1 :


        # print(listgenans)
        opprhs = simplify(sympify(str(expand(sympify("("+listques0[1]+")**2")))+"+(" +str(simplify(sympify(str((expand(sympify("("+str(listques0[0]).replace(" ","")+")**2"))))+"-("+str(listques[1])+")")))+")"))
        diff = simplify(sympify(simplify(sympify(str((expand(sympify("("+str(listques0[0]).replace(" ","")+")**2"))))+"-("+str(listques[1])+")"))))

        listgenanslhs = [None] * len(listgenans)
        listgenansrhs = [None] * len(listgenans)
        # listgenansconcept = [None] * len(listgenans)

        i = 0

        for x in listgenans:
            ans = x.replace(" ", "").split("=", 1)
            listgenanslhs[i] = ans[0]
            listgenansrhs[i] = ans[1]
            i = i + 1

        listans = answer.replace(" ", "").split("=")
        anslhs = listans[0]
        ansrhs = listans[1]

        anslhs = anslhs.replace(" ","")
        not_in_gen_ans = true

        if isStepIncorrect ==  true:
            not_in_gen_ans = false
            print("Error : This step is not marked due to the error in step " + str(incorrectStepNum) + "\nMarks = 0")
        elif listgenanslhs.__contains__(anslhs):
            not_in_gen_ans = false
            if sympify(ansrhs) == sympify(listgenansrhs[listgenanslhs.index(anslhs)]):
                if listgenansconcept[listgenanslhs.index(anslhs)] == "data":
                    isData = true
                    print("Re-written the expression")
                elif listgenansconcept[listgenanslhs.index(anslhs)] == "square":
                    isSquare = true
                    print("Step is correct")
                    # print("bb")
                elif listgenansconcept[listgenanslhs.index(anslhs)] == "subject":
                    if linenum + 1 == lines and ansrhs == listgenansrhs[len(listgenansrhs) - 1]:
                        if gotFinalAnswer == true:
                            print("Already obtained the final answer in step " + str(finAnsLine))
                        else:
                            marks  = subjectMarks
                            print("Final answer is Correct.\nMarks = "+ str(marks))
                            gotFinalAnswer = true
                            finAnsLine = linenum + 1
                    elif linenum + 1 == lines and ansrhs != listgenansrhs[len(listgenansrhs) - 1]:
                        if gotFinalAnswer == true:
                            print("Already obtained the final answer in step " + str(finAnsLine))
                        else:
                            print("Final answer is not simplified")
                    elif linenum + 1 != lines and ansrhs == listgenansrhs[len(listgenansrhs) - 1]:
                        if gotFinalAnswer == true:
                            print("Already obtained the final answer in step " + str(finAnsLine))
                        else:
                            print("Final answer is correct")
                            gotFinalAnswer = true
                            finAnsLine = linenum + 1
                    else:
                        if gotFinalAnswer == true:
                            print("Already obtained the final answer in step " + str(finAnsLine))
                        else:
                            print("Answer can be further simplified")
                    # print("dd")
                elif listgenansconcept[listgenanslhs.index(anslhs)] == "expansion":
                    if isExpansion == false:
                        isExpansion = true
                        expansionStepNum = linenum + 1
                        marks = expansionMarks
                        print("Expansion is correct.\nMarks = " + str(marks))
                    else:
                        if gotFinalAnswer == true:
                            print("Step is correct")
                            print("Already obtained the final answer in step " + str(finAnsLine))
                        else:
                            print("Step is correct")
                            print("Marks for expansion of terms has been provided in step " + str(expansionStepNum))
                    wronganswer = ""
                    # print("cc")
                else:
                    wronganswer = anslhs
            else :
                if sympify(ansrhs) == sympify(opprhs):
                    if sympify(listgenansrhs[len(listgenansrhs)-1]) > sympify(ansrhs):
                        print("Error : You have subtracted " +str(diff).replace("-","")+ " from the RHS. But it should be added to RHS.")
                    else:
                        print("Error : You have added " + str(diff).replace("-","")+ " to the RHS. But it should be subtracted from RHS.")
                else:
                    print("Error : RHS of the equation is wrong")
                if isStepIncorrect == false:
                    isStepIncorrect = true
                    incorrectStepNum = linenum + 1
                    # print("Error : Step is incorrect")
                wronganswer = ""
        else:
            for x in listgenanslhs:

                if simplify(sympify(anslhs)) == simplify(sympify(x)) :
                    not_in_gen_ans = false
                    # and len(anslhs.replace("(","").replace(")","")) == len(x.replace("(","").replace(")",""))
                    # simplify(sympify(anslhs)) == simplify(sympify(x))
                    if sympify(ansrhs) == sympify(listgenansrhs[listgenanslhs.index(x)]):
                        if listgenansconcept[listgenanslhs.index(x)] == "data":
                            isData = true
                            if len(anslhs.replace(" ","")) == len(x) :
                                print("Re-written the expression")
                            else:
                                print("Unnecessary grouping of expressions")
                            # print("aa2")
                        elif listgenansconcept[listgenanslhs.index(x)] == "square":
                            if len(anslhs.replace("(","").replace(")","")) != len(x.replace("(","").replace(")","")):
                                print("Unnecessary grouping of expressions")
                            else:
                                print("Step is correct")
                            isSquare = true
                            # print("bb2")
                        elif listgenansconcept[listgenanslhs.index(x)] == "subject":
                            isSubject = true
                            if linenum + 1 == lines and ansrhs == listgenansrhs[len(listgenansrhs)-1] :
                                #isExpanded ?
                                marks = subjectMarks
                                print("Final answer is Correct.\nMarks = "+ str(marks))
                                gotFinalAnswer = true
                                finAnsLine = linenum + 1
                            elif sympify(ansrhs) == simplify(sympify(listgenansrhs[listgenansconcept.index("subject")])):
                                if len(ansrhs) != len(listgenansrhs[len(listgenansrhs)-1]):
                                    print("Answer can be further simplified")
                            # print("dd2")
                        elif listgenansconcept[listgenanslhs.index(x)] == "expansion":
                            if isExpansion  == false:
                                isExpansion = true
                                expansionStepNum = linenum +1
                                marks = expansionMarks
                                print("Expansion is correct.\nMarks = "+ str(marks))
                            else:
                                if gotFinalAnswer ==  true :
                                    print("Step is correct")
                                    print("Already obtained the final answer in step "+str(finAnsLine))
                                else :
                                    print("Step is correct")
                                    print("Marks for expansion of terms has been provided in step "+ str(expansionStepNum))
                            # print("cc2")
                        break
                    else :
                        if sympify(ansrhs) == sympify(opprhs):
                            if sympify(listgenansrhs[len(listgenansrhs)-1]) > sympify(opprhs):
                                print("Error : You have subtracted " + str(diff).replace("-","")+ " from the RHS. But it should be added to RHS.")
                            else :
                                print("Error : You have added " + str(diff).replace("-","") + " to the RHS. But it should be subtracted from RHS.")
                        else:
                            print("Error : RHS of the equation is wrong")
                        if isStepIncorrect == false:
                            isStepIncorrect = true
                            incorrectStepNum = linenum + 1
                            # print("Error : Step is incorrect")
                        wronganswer = ""
                        break

        if not_in_gen_ans == true :
            anslhstemp = anslhs.replace("+"," +").replace("-"," -")
            listanslhs = anslhstemp.split(" ")
            signerror = false
            for x in listgenanslhs:
                # val = solve(str(anslhs.replace("-","+")+"-("+x+")"),x.replace("-","+"))
                if simplify(sympify(str(anslhs.replace("-","+")+"-("+x+")"))) == 0:
                    signerror = true
            if signerror == true:
                print("Error : Mistake in the sign of the expression")
                if isStepIncorrect == false:
                    isStepIncorrect = true
                    incorrectStepNum = linenum + 1
                    # print("Error : Step is incorrect")
                wronganswer = ""
            else :
                print("Error : Expression is incorrect")
                if isStepIncorrect == false:
                    isStepIncorrect = true
                    incorrectStepNum = linenum + 1
                    # print("Error : Step is incorrect")
                wronganswer = ""



        if wronganswer == anslhs :

            if isStepIncorrect == false :
                isStepIncorrect =true
                incorrectStepNum = linenum + 1
                print("Error : Step is incorrect")
            else:
                print("Error : This step is not marked due to the error in step " + str(incorrectStepNum) + "\nMarks = 0")

        # if gotFinalAnswer and (isSquare or isExpansion) and totmarks == totalmarks -(expansionMarks+subjectMarks):
        #     marks = marks + expansionMarks
        # elif gotFinalAnswer and not (isSquare or isExpansion) :
        #     print("no")

        if gotFinalAnswer and (isStepIncorrect != true) and totmarks == 0:
            # totmarks == totalmarks
            marks = totalmarks
        elif (gotFinalAnswer == false) and (linenum+1 == lines) and (isExpansion == false) and (isSubject == false) and (isStepIncorrect != true):
            print("\n\nImportant steps are missing")
            print("Expand the equation and simplify it to get marks")


        return int(marks)


Evaluate().get()
