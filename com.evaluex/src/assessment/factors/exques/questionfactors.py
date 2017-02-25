from bs4 import BeautifulSoup
from sympy import *


class Question():
    col_size = None
    row_size = None


    def __init__(self, mathml_file, logger):
        self.mathml_file = mathml_file
        self.logger = logger

    def readquestion(self):
        global col_size, row_size
        filein = open(self.mathml_file)  # open the mathml file
        self.logger.info('Reading mathml')
        lhs = self.read(filein)  # read and parse the question
        self.logger.info('Finish mathml reading')
        return lhs


    def read(self, filein):
        # parse the question
        global col_size, row_size
        i = 0
        isfoundcol = false  # check whether coloumn size has found
        isfoundrow = false  # check whether row size has found
        mtrilist = []  # store right hand side answer
        matri_name = []  # store left hand side answers
        question = ''  # store question
        count = 0  # check whether matrix expression has started
        lhs_dict = {}  # store question in a dictionary
        # parse the question
        for line in filein:
            soup = BeautifulSoup(line, "html.parser")
            if 'math_expression' in line :
                # self.logger.info(soup.text)
                # print(soup.text)
            if 'mrow' in line :
                tag = line.find('mrow')
                if tag is not None:
                    print(soup.text)
            # if 'mi' in line and 'mtd' not in line:
            #     temp = soup.text
            #     matri_name.insert(0, temp)
            #     count += 1
            # if 'mn' in line:
            #     mtrilist.insert(i, soup.text)
            # if 'mtd' in line and 'mi' in line:
            #     mtrilist.insert(i, soup.text)
            # if '/mtr' in line and not isfoundcol:
            #     col_size = len(mtrilist)
            #     isfoundcol = true
            # if 'mfenced' in line:
            #     count = 0
            # if '/mo' in line and count > 0:
            #     if '=' not in soup.text:
            #         matri_name.insert(0, soup.text)
            # if '/math' in line and len(matri_name) > 0:
            #     for d in range(0, len(matri_name)):
            #         question += matri_name.pop().strip()
            #     lhs_dict['ques'] = question
            # if '/mtable' in line:
            #     if not isfoundrow:
            #         siz = len(mtrilist)
            #         row_size = int(siz / col_size)
            #         isfoundrow = true
            #     length = len(matri_name)
            #     matrix_leftside = ''
            #     list = [mtrilist[x:x + col_size] for x in range(0, len(mtrilist), col_size)]
            #     m = Matrix(list)
            #     if length > 2:
            #         for d in range(0, length):
            #             matrix_leftside += matri_name.pop().strip()
            #         lhs_dict[matrix_leftside.strip()] = m
            #     else:
            #         lhs_dict[matri_name.pop().strip()] = m
            #     mtrilist.clear()
            # i += 1
        return lhs_dict