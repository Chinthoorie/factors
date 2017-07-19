# this class can solves matrix questions which have matrix with variables
from _operator import ne
from pydoc import ispackage

from sympy import *
import re


class Solver:
    def solve(self):

        # with open('full questions/simplifya_1.txt') as filein:
        #     data = "\n".join(line.rstrip() for line in filein)
        # filein.close()

        # with open('full questions/simplifyb_1.txt') as filein:
        #     data = "\n".join(line.rstrip() for line in filein)
        # filein.close()

        # with open('full questions/factorization_1.txt') as filein:
        #     data = "\n".join(line.rstrip() for line in filein)
        # filein.close()
        #
        # with open('full questions/LCM_1.txt') as filein:
        #     data = "\n".join(line.rstrip() for line in filein)
        # filein.close()
        #
        with open('full questions/subject_1.txt') as filein:
            data = "\n".join(line.rstrip() for line in filein)
        filein.close()



        # a = str('இன் காரணிகளைக் காண்க.')
        # data = "பின்வரும் கோவைகளிடையே விடையாக 4y கிடைக்கும் எல்லாக் கோவைகளையும் தெரிந்தெடுத்து எழுதுக"
        print(data)
        if data.find('சுருக்குக') != -1:
            value = 1
        elif data.find('எல்லா') != -1 and data.find('கோவை')  != -1 :
            value = 2
        elif data.find('எழுவா') != -1:
            value = 3
        elif data.find('காரணி') != -1:
            value = 4
        elif data.find('பொது மடங்குகளு ') != -1:
            value = 5
        elif data.find('எனின் இன் பெருமானத்தைக் கா') != -1:
            value = 6

        # value = "u\""+data+"\""
        # check = a.rsplit(" ")
        print(value)
        # print(check)

#
#       write a switch case to evoke the respective method
#
       # if(valu)



Solver().solve()