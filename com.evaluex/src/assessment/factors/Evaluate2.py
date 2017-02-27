from xml.etree import ElementTree as ET

from sympy import *
import re

from sympy.core.compatibility import unicode
from sympy.parsing.sympy_parser import parse_expr


class Evaluate2:
    markingScheme = ""
    answer = ""
    question = ""

    def getMarks(self) :
        with open('evaluate_a1.xml') as filein:
            answer = " ".join(line.rstrip() for line in filein)

        filein.close()

        # listelements = []

        # print(answer)
        answer = answer.replace("<?xml version='1.0'?>","").replace("<math xmlns='http://www.w3.org/1998/Math/MathML'>","").replace("</math>","").replace("\t","").replace(" ","")
        listanswers = answer.split("<mspacelinebreak=\"newline\"/>")

        listelements = [None] * len(listanswers)
        # print(listanswers)

        for line in listanswers:
            file =  open('ex'+str(listanswers.index(line))+'.xml','w')
            file.write(line)
            file.close()

        for line in listanswers:
           file = open('student_answer.txt', 'w')
           for line in listanswers:
               exppy, symvars = parseMML('ex' + str(listanswers.index(line)) + '.xml')
               # print(exppy)
               exprlist = []
               for expr in exppy:
                   exprlist.append(parse_expr(expr, evaluate=False))

               # print(exprlist)
               element = str(exprlist).replace("[", "").replace("]", "").replace(",", "=")
               file.write(element)
               file.write("\n")
               # print(element)
               # exprlist = exprlist.remove(None)
               # filter(None,exprlist)
               # element = str(exprlist[0]) + "=" + str(exprlist[1])
               # listelements.insert(listanswers.index(line), element)
        file.close()




        # print(listelements)





def parseMML(mmlinput):
    exppy = ""  # this is the python expression
    symvars = []  # these are symbolic variables which can eventually take part in the expression
    events = ("start", "end")
    level = 0
    context = ET.iterparse(mmlinput, events=events)
    for action, elem in context:
        if (action == 'start') and (elem.tag == 'mfrac'):
            level += 1
            tree = ET.ElementTree(elem[0])
            tree.write('output.xml')
            (a, b) = parseMML('output.xml')
            symvars.append(b)
            for index in a:
                exppy += index
            exppy += '/'
            tree = ET.ElementTree(elem[1])
            tree.write('output.xml')
            (a, b) = parseMML('output.xml')
            symvars.append(b)
            for index in a:
                exppy += index
        if (action == 'end') and (elem.tag == 'mfrac'):
            level -= 1
        if level:
            continue
        if (action == 'start') and (elem.tag == 'mrow'):
            exppy += '('
        if (action == 'end') and (elem.tag == 'mrow'):
            exppy += ')'
        if action == 'start' and elem.tag == 'msub':  # this is a power
            # level += 1
            # tree = ET.ElementTree(elem[0])
            # tree.write('output.xml')
            # (a, b) = parseMML('output.xml')
            # symvars.append(b)
            # for index in a:
            #     exppy += '['
            #     exppy += index
            #     exppy += ']'
            # exppy += '**'
            # tree = ET.ElementTree(elem[1])
            # tree.write('output.xml')
            # (a, b) = parseMML('output.xml')
            # symvars.append(b)
            # for index in a:
            #     exppy += index
            level += 1
            tree = ET.ElementTree(elem[0])
            tree.write('output.xml')
            (a, b) = parseMML('output.xml')
            symvars.append(b)
            for index in a:
                exppy += '['
                exppy += index
                exppy += ']'
            exppy += '**'
            tree = ET.ElementTree(elem[1])
            tree.write('output.xml')
            (a, b) = parseMML('output.xml')
            symvars.append(b)
            for index in a:
                exppy += index
                # exppy += ''
        if action == 'start' and elem.tag == 'mn':  # this is a number
            exppy += elem.text
        if action == 'start' and elem.tag == 'mi':  # this is a variable
            exppy += elem.text
            symvars.append(elem.text)  # we'll return the variable, so sympy can sympify it afterwards
        if action == 'start' and elem.tag == 'mo':  # this is a operation
            exppy += elem.text

    if exppy.startswith('(') and exppy.endswith(')'):
        exppy = exppy[1:-1]

    exppyarray = exppy.split("=")

    # for exppy in exppyarray :
    #     print(exppy)

    return exppyarray, symvars

Evaluate2().getMarks()