# this class can solves matrix questions which have matrix with variables
from _operator import ne
from pydoc import ispackage

from sympy import *
import re


class Factorize:
    def solve(answer):

        with open('questions/factorization_2.txt') as filein:
            data = "\n".join(line.rstrip() for line in filein)

        filein.close()

        # answer = input("Find the factors of " + data + "\n")

        # with open('answers/factorization_2_3.txt') as filein:
        #     answer = "\n".join(line.rstrip() for line in filein)
        #
        # filein.close()

        with open('marking scheme/factorization_1.txt') as filein:
            ms = "\n".join(line.rstrip() for line in filein)

        filein.close()

        print("\nQuestion : " + data + "\n")
        print("Student answer : " + answer + "\n")
        print("-----------------------------------------------")

        marks = 0;
        wronganswer = ""

        # listms = ms.split("\n")
        #
        # ms1 = listms[0]
        #
        # listms1 = ms1.split("=")
        # marks1 = listms1[1]

        listms = ms.split("\n")
        # print(listms)
        ms1 = listms[0]
        ms2 = listms[1]
        # ms3 = listms[2]

        listms1 = ms1.split("=")
        marks1 = listms1[1].replace(" ", "")
        listms2 = ms2.split("=")
        marks2 = listms2[1].replace(" ", "")

        listans = answer.replace(" ", "").split("\n")
        linearr = [[[] for i in range(len(listans))] for j in range(len(listans))]
        # linearr = [[] for _ in range(len(listans))]


        for i in range(0, len(listans) - 1):
            if simplify(expand(sympify(listans[i]))) == simplify(expand(sympify(listans[i + 1]))):

                print("line " + str(i + 1) + " is equal to line " + str(i + 2))
                linearr[i][i + 1] = linearr[i + 1][i] = str(1)
                # print(linearr)
        for i in range(0, len(listans)):
            for j in range(0, len(listans)):
                print(linearr[i][j], end=" ")
            print()


        # (x-2),(x+5) or x-2,x+5
        # lista = answer.replace("+", " +").replace("-", " -").split(" ")
        # if re.fullmatch("[^0-9]?[0-9]?[a-z][-/+]?[0-9]?[a-z][^0-9]?[,][^0-9]?[0-9]?[a-z]?[-/+]?[0-9]?[a-z][^0-9]",answer):
        #     print(answer)

        if answer.find(',') != -1:
            #  x-2,x+5
            if answer.find('(') == -1:
                if sympify(str(answer.split(",")).replace(" ","").replace("','", ")*(").replace("['","(").replace("']",")")) == factor(sympify(listq[0])):
                    marks = marks1
                    print("Correct \nMarks = " + marks)

                else :
                    wronganswer = answer
                    # print("Incorrect\nMarks = " + str(marks))
            # (x-2),(x+5)
            else :
                if sympify(answer.replace(",", "*").replace("'","")) == factor(sympify(data)):
                    marks = marks1
                    print("Correct \nMarks = " + marks)
                else:
                    wronganswer = answer
                    # print("Incorrect\nMarks = " + str(marks))
        # (x-2)*(x+5)
        elif answer.find('*') != -1:
            if sympify(answer.replace(" ", "")) ==  factor(sympify(data)):
                marks = marks1
                print("Correct \nMarks = " + marks)
            else:
                wronganswer = answer
                # print("Incorrect\nMarks = " + str(marks))
        # (x-2)(x+5)
        elif answer.find(')(') != -1:
            if sympify(answer.replace(" ", "").replace(")(",")*(")) == factor(sympify(data)):
                marks = marks1
                print("Correct \nMarks = " + marks)
            else:
                wronganswer = answer
                # print("Incorrect\nMarks = " + str(marks))
        # x(x-2)
        elif answer.replace(" ", "").endswith(')'):
            if sympify(answer.replace(" ", "").replace("(", "*(")) == factor(sympify(data)):
                marks = marks1
                print("Correct \nMarks = " + marks)
            else:
                wronganswer = answer
                # print("Incorrect\nMarks = " + str(marks))
        # (x-2)x
        elif answer.replace(" ", "").startswith('('):
            if sympify(answer.replace(" ", "").replace(")", ")*")) == factor(sympify(data)):
                marks = marks1
                print("Correct \nMarks = " + marks)
            else:
                wronganswer = answer
                # print("Incorrect\nMarks = " + str(marks))

        elif {
            # lista = answer.replace("+"," +").replace("-"," -").split(" ")

        }:
            print("Incorrect\nMarks = " + str(marks))

        # answerb = "x**2+5*x-2*x-10"
        # # x**2 + 5*x - 2*x - 10
        # # x(x + 5) - 2(x + 5)
        # # x(x - 2) + 5(x - 2)

        check = 0

        if wronganswer != "":
            check = 1
            listq = str(factor(sympify(data))).replace("(", "").replace(")", "").split("*")
            listqq = []
            for ele in listq:
                if answer.find("(" + ele.replace(" ", "") + ")") != -1:
                    listqq.append(ele)
            for ele in listqq:
                if answer.find("("+ele.replace(" ", "")+")") != -1:
                    g = answer.replace(ele.replace(" ", ""),str(1))
                    g = simplify(sympify(g))
                    # print(g)
                    if listq.__contains__(str(g)):
                        # print(g)
                        marks = marks2
                        print(
                            "Answer is in a partially factorized form. It should be fully factorized to get full marks.")
                        print("Partially correct \nMarks = " + marks)
                    elif answer.find(ele.replace(" ", "")) != -1:
                        print("Partial factorization is incomplete. It should be fully factorized to get full marks.")
                        print("Incorrect\nMarks = " + str(marks))
                    # print("true")
                    # if simplify(expand(sympify(answer))) == simplify(sympify(data.replace(" ",""))):
                    #     marks = marks2
                    #     print("Answer is in a partially factorized form. It should be fully factorized to get full marks")
                    #     print("Partially correct \nMarks = " + marks)
                    else:
                        print("Partial factorization is wrong.")
                        print("Incorrect\nMarks = " + str(marks))
                else :
                    wronganswer = answer
                    check = 0



        if wronganswer != "" and check ==0 :
            answerb = wronganswer

            lista = answerb.replace("+", " +").replace("-", " -").split(" ")
            # print(lista)

            listq = str(factor(sympify(data))).replace("(", "").replace(")", "").split("*")
            # print(listq)

            if listq[0].find("-") == -1:
                listqf = listq[0].replace("'","").replace(" ","").split("+")
            elif listq[0].find("+") == -1:
                listqf = listq[0].replace("'", "").replace(" ","").split("-")

            # print(listqf)

            a1 = cancel(sympify((lista[0]+lista[1]))/sympify(listq[0]))
            # print(a1)
            b1 = cancel(sympify(sympify(lista[2]) + sympify(lista[3]))/sympify(listq[0]))
            # print(b1)
            c1 = ""
            c2 = ""

            if simplify(sympify(a1+b1)) == sympify(listq[1]):
                c1 = (str(a1 + b1).replace(" ", ""))
            # cc1=(str(a1 + b1).replace(" ", ""))
            # print(cc1)

            if listq[1].find("-") == -1:
                listqf = listq[1].replace("'", "").replace(" ", "").split("+")
            elif listq[0].find("+") == -1:
                listqf = listq[1].replace("'", "").replace(" ", "").split("-")

            # print(listqf)

            a2 = cancel(sympify((lista[0] + lista[1])) / sympify(listq[1]))
            # print(a2)
            b2 = cancel(sympify(sympify(lista[2]) + sympify(lista[3])) / sympify(listq[1]))
            # print(b2)

            if simplify(sympify(a2 + b2)) == sympify(listq[0]):
                c2 = (str(a2+b2).replace(" ", ""))
            # cc2=(str(a2+b2).replace(" ", ""))
            # print(cc2)

            # print(c1)
            # print(c2)
            # print(listq[0])

            # if simplify(sympify(c1)) == simplify(sympify(listq[0])) or simplify(sympify(c1)) == simplify(sympify(listq[1])):
            c3 = str("(" + c1 + ")*(" + str(listq[0]).replace(" ", "") + ")")
            # elif simplify(sympify(c2)) == simplify(sympify(listq[0])) or simplify(sympify(c2)) == simplify(sympify(listq[1])):
            c4 = str("("+c2 + ")*(" + str(listq[1]).replace(" ", "")+")")

            # print(c3)
            # print(c4)

            if c3.find("/") == -1:
                c = c3
            elif c4.find("/") == -1:
                c = c4
            # print(c)

            if c.find('*') != -1:
                if sympify(c.replace(" ", "")) == factor(sympify(data)):
                    marks = marks2
                    print("Answer is in an expanded form. It should be fully factorized to get full marks")
                    print("Partially correct \nMarks = " + marks)
                else:
                    wronganswer = answer

            # index = 0
            remainder = simplify(sympify(data)-sympify(answer))
            # print(remainder)
            remainder = remainder/2
            # print(remainder)
            # print(sympify(remainder)*(-1))

            # if lista.__contains__(str(sympify(remainder)*(-1))) == true:
            #     print("has")
            #     index=lista.index(remainder*-1)
            #     print(index)
            #     if simplify(sympify(lista[index]) +sympify(remainder)) == 0:
            #         print("Sign of "+str(remainder).replace("-","+")+" is negated ")
            #

            if wronganswer != "":
                for element in lista:
                    if sympify(element) == sympify(remainder)*(-1):
                        # print(element)
                        index = lista.index(element)
                        if simplify(sympify(lista[index]) + sympify(remainder)) == 0:
                            print("Sign of "+str(remainder).replace("-","+")+" is negated \n")
                            print("Incorrect\nMarks = " + str(marks))
                        else:
                            wronganswer = answer
                    else:
                        wronganswer = answer





        # if

        print("-----------------------------------------------")

Factorize().solve()
