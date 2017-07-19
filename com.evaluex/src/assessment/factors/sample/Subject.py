#solve type 4
from _operator import ne
from pydoc import ispackage

from sympy import *
import re
from sympy.abc import v,u,a,s
# v,u,a,s = Symbol('v,u,a,s')

class Subject:
    
    def solve(self):

        with open('questions/subject_1.txt') as filein:
            data = "".join(line.rstrip() for line in filein)

        filein.close()

        # listq = data.split(",")
        # answer = input("Change " + listq[1] + " the subject of " + listq[0] + "\n")

        with open('answers/subject_1_1.txt') as filein:
            answer = "\n".join(line.rstrip() for line in filein)

        filein.close()

        with open('marking scheme/subject_1.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

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

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")

        # lista = answer.split("=")
        # listq0 = listq[0].split("=")

        question = data.split(",")
        qequation = question[0].replace(" ","")
        listequ = qequation.split("=")
        stlhs = question[1].replace(" ","")

        answers = answer.split("=")
        anslhs = answers[0].replace(" ","")
        ansrhs = answers[1].replace(" ","")

        # qequation.subs(anslhs,ansrhs)
        # print(simplify(sympify(listequ[1].replace(str(anslhs),str(ansrhs)))))

        # sympify(qequation.replace(str(anslhs), str(ansrhs)))

        # print(str(simplify(sympify(listq0[1].replace(listq[1],lista[1])))))

        if anslhs  == stlhs  :
            # if str(simplify(sympify(listq0[1].replace(listq[1],lista[1]).replace(" ","")))) == listq0[0].replace(" ","") :
            exp = str(simplify(sympify(sympify(listequ[1]).subs(stlhs,ansrhs))))
            if exp == listequ[0].replace(" ",""):
                marks = marks1
                print("Correct \nMarks = " + marks)
            # else:
            #     print("Incorrect\nMarks = " + str(marks))
            elif anslhs  != listequ[0] :
                if listequ[0].find(str("-"+stlhs)) != -1:
                    if sympify(ansrhs) == sympify(str(solve(listequ[0] + "-(" + listequ[1] +")", stlhs)).replace("[","").replace("]","")):
                        marks = marks1
                        print("Correct \nMarks = " + marks)
                    else:
                        print("Incorrect\nMarks = " + str(marks))
                elif listequ[1].find(str("-"+stlhs)) != -1:
                    if sympify(ansrhs) == sympify(str(solve(listequ[1] + "-(" + listequ[0] +")", stlhs)).replace("[","").replace("]","")):
                        marks = marks1
                        print("Correct \nMarks = " + marks)
                    else:
                        print("Incorrect\nMarks = " + str(marks))
                else:
                    print("Incorrect\nMarks = " + str(marks))
            else:
                print("Incorrect\nMarks = " + str(marks))


        #  listqf = listq[0].replace("'","").replace(" ","").split("+")
        # else:
        #     listqf = listq[0].replace("'", "").replace(" ","").split("-")
        #

        # print(solve(listequ[1]+"-"+listequ[0],stlhs))

        print("-----------------------------------------------")

Subject().solve()
