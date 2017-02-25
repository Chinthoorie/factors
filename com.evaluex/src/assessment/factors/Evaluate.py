#solve question type 5
from _operator import ne
from pydoc import ispackage

from sympy import *
import re


class Evaluate:
    def solve(self):

        with open('questions/evaluate_3.txt') as filein:
            data = "\n".join(line.rstrip() for line in filein)

        filein.close()

        # listq = data.split(",")
        # answer = input("if " + listq[0] + " then find the value of " + listq[1] + "\n")



        with open('answers/evaluate_3_1.txt') as filein:
            answer = "\n".join(line.rstrip() for line in filein)

        filein.close()
        with open('marking scheme/evaluate_3.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        marks = 0
        listnames = ""

        listques = data.replace(" ","").split("\n")
        # print(listques)

        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        ms2 = listms[1]
        ms3 = listms[2]

        if ms1.find("marks") != -1:
            listms1 = ms1.split(",")
            listms11 = listms1[1].split("=")
            marks1 = listms11[1].replace(" ", "")
            step1 = listms1[0].split("->")
            operation1 = step1[0]
            exp1 = step1[1].replace(" ", "")
        else:
            marks1 = 0;
            step1 = ms1.split("->")
            operation1 = step1[0]
            exp1 = step1[1].replace(" ", "")


        listms2 = ms2.split(",")
        listms21 = listms2[1].split("=")
        marks2 = listms21[1].replace(" ", "")
        if marks2[0].find("->") != -1:
            step2 = listms2[0].split("->")
            operation2 = step2[0]
            exp2 = step2[1].replace(" ", "")
        else :
            operation2 = marks2[0]
        if ms3 != "":
            listms3 = ms3.split(",")
            listms31 = listms3[1].split("=")
            marks3 = listms31[1].replace(" ", "")
            step3 = listms3[0].split("->")
            operation3 = step3[0]
            exp3 = step3[1].replace(" ", "")

        #generate the answer on the own
        listgenans = []
        listgenansconcept = []


        # if operation1 == "expansion":
        #     listgenans.append(expand(sympify(exp1+"**2")))
        # print(listques[0])
        # listques0 = listques[0].split("=")
        # print("("+listques0[0]+")**2 = ("+listques0[1]+")**2")
        # print(str(expand(sympify("(" + listques0[0] + ")**2"))) + " = (" + listques0[1] + ")**2")
        # print(str(expand(sympify("("+listques0[0]+")**2")))+" = "+str(expand(sympify("("+listques0[1]+")**2"))))
        # print(str(listques[1]) + " = "+ str(expand(sympify("("+listques0[1]+")**2")))+"-(" +str(simplify(sympify(str((expand(sympify("("+str(listques0[0]).replace(" ","")+")**2"))))+"-("+str(listques[1])+")")))+")")
        # print(str(listques[1]) + " = " + str(simplify(sympify(str(expand(sympify("(" + listques0[1] + ")**2"))) + "-(" + str(simplify(
        #     sympify(str((expand(sympify("(" + str(listques0[0]).replace(" ", "") + ")**2")))) + "-(" + str(
        #         listques[1]) + ")"))) + ")"))))

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

        listgenanslhs = [None] * len(listgenans)
        listgenansrhs = [None] * len(listgenans)
        # listgenansconcept = [None] * len(listgenans)

        i = 0

        for x in listgenans:
            ans = x.replace(" ", "").split("=", 1)
            listgenanslhs[i] = ans[0]
            listgenansrhs[i] = ans[1]
            i = i + 1

        linearrdata = [[[] for i in range(len(listgenans))] for j in range(len(listgenans))]

        # for i in range(0, len(listgenanslhs) ):
        #     for j in range(0, len(listgenanslhs) ):
        #         if simplify(expand(sympify(listgenanslhs[i]))) == simplify(expand(sympify(listgenanslhs[j]))):
        #             # print(listlhs[i]+" = "+listlhs[i+1])
        #             if simplify(expand(sympify(listgenansrhs[i]))) == simplify(expand(sympify(listgenansrhs[j]))):
        #                 # print(listrhs[i]+" = "+listrhs[i+1])
        #                 print("line " + str(i + 1) + " is equal to line " + str(j + 1))
        #                 linearrdata[i][j] = linearrdata[j][i] = str(1)
        #             else:
        #                 linearrdata[i][j] = linearrdata[j][i] = str(0)
        #         else:
        #             linearrdata[i][j] = linearrdata[j][i] = str(0)
        #
        #
        #
        # for i in range(0, len(listgenans)):
        #     for j in range(0, len(listgenans)):
        #         print(linearrdata[i][j], end=" ")
        #     print()

        print(listgenans)
        print(listgenanslhs)
        print(listgenansrhs)
        print(listgenansconcept)


        expansion = expand(sympify(exp1))
        # print(expansion)

        print("\nQuestion : " + data + "\n")
        print("Student answer : \n" + answer + "\n")
        print("-----------------------------------------------")

        listans = answer.replace(" ","").split("\n")
        listlhs = [None]*len(listans)
        listrhs = [None]*len(listans)

        i = 0

        for x in listans:
            ans = x.replace(" ","").split("=",1)
            listlhs[i] = ans[0]
            listrhs[i] = ans[1]
            i = i+1

        print(listans)
        print(listlhs)
        print(listrhs)

        i = 0

        for y in listrhs:
            if y.find("=") != -1:
                i = listrhs.index(y)
                print("listrhs["+str(i)+"] = "+y)
                listtemp = y.split("=")
                if len(listtemp) == 2 :
                    if simplify(sympify(listtemp[0])) == simplify(sympify(listtemp[1])) :
                        print(true)

        linearr = [[[] for i in range(len(listans))] for j in range(len(listans))]
        # linearr = [[] for _ in range(len(listans))]


        # for i in range(0,len(listlhs)):
        #     for j in range(0, len(listlhs)):
        #         if simplify(expand(sympify(listlhs[i]))) == simplify(expand(sympify(listlhs[j]))):
        #             # print(listlhs[i]+" = "+listlhs[i+1])
        #             if simplify(expand(sympify(listrhs[i]))) == simplify(expand(sympify(listrhs[j]))):
        #                 # print(listrhs[i]+" = "+listrhs[i+1])
        #                 print("line "+str(i+1)+" is equal to line "+str(j+1))
        #                 linearr[i][j] = linearr[j][i] = str(1)
        #                 # print(linearr)
        #             else :
        #                 linearr[i][j] = linearr[j][i] = str(0)
        #         else:
        #             linearr[i][j] = linearr[j][i] = str(0)
        #     # else:
        #         # print(listlhs[i] + " !=  " + listlhs[i + 1])
        #
        # for i in range(0,len(listans)):
        #     for j in range(0, len(listans)):
        #         print(linearr[i][j],end=" ")
        #     print()





        print("-----------------------------------------------")


Evaluate().solve()
