from bs4 import BeautifulSoup
from sympy import *


class Question():

    # mathml_file = simplifya.html
    #
    # def readquestion(self):
    #     global col_size, row_size
    #     filein = open(self.mathml_file)  # open the mathml file
    #     # self.logger.info('Reading mathml')
    #     lhs = self.read(filein)  # read and parse the question
    #     # self.logger.info('Finish mathml reading')
    #     return lhs

    def readQFile(self):

        with open('simplifya.html') as filein:
            data = "\n".join(line.rstrip() for line in filein)
        filein.close()

        mathmlfile = data.split("\n")
        # print(mathmlfile)
        mathmlfile = [x.strip(' ').replace('\t','') for x in mathmlfile]
        for x in mathmlfile:
            print(x)
        # print(mathmlfile)

        # print(mathmlfile.__contains__("<math_expression>"))
        starti = mathmlfile.index("<math_expression>")
        # print(mathmlfile.index("<math_expression>"))
        endi = mathmlfile.index("</math_expression>")
        # print(mathmlfile.index("</math_expression>"))

        mrowcount = 0
        mrowlist = []
        expressionlist = []
        lastmrowindex = None
        lastnmrowindex = None
        temp = ""
        temp1 =""
        curr_list = mathmlfile

        for i in range(starti+1, endi):
            # print(mathmlfile[i])
            if mathmlfile[i] == "<mrow>":
                mrowlist.append(i)
                lastmrowindex  = i
                mrowcount = mrowcount + 1
            if mathmlfile[i] == "</mrow>":
                lastnmrowindex = i
                print(str(lastnmrowindex)+" "+str(len(mrowlist)-2))
                for k in range(lastnmrowindex+1,lastmrowindex):
                    print("k="+k)
                    temp1 = temp1 + curr_list[k]
                    curr_list[j] = ""
                curr_list[lastnmrowindex] = ""
                curr_list[i] = ""
                for j in range(lastmrowindex + 1, i):
                    temp = temp + curr_list[j]
                    curr_list[j] = ""
                curr_list[lastmrowindex] = ""
                curr_list[i] = ""

                expressionlist.append(temp)
                print("\n"+temp1+temp+"\n")
                print(curr_list)
                mrowlist.pop()


        for i in range(0, len(mathmlfile)):
            soup = BeautifulSoup(mathmlfile[i], "html.parser")
            if 'math_expression' in mathmlfile[i]:
                # self.logger.info(soup.text)
                print(soup.text)
            if 'mrow' in mathmlfile[i]:
                print(soup.text)

        # for line in mathmlfile:
        #     soup = BeautifulSoup(line, "html.parser")
        #     if 'math_expression' in line:
        #     # self.logger.info(soup.text)
        #         print(soup.text)
        #     if 'mrow' in line:
        #         print(soup.text)

            # if 'mi' in line and 'mtd' not in line:
            #     temp = soup.text
            #     print(soup.text)
            #     # matri_name.insert(0, temp)
            #     # count += 1
            # if 'mn' in line:
            #     print(soup.text)
            #     # mtrilist.insert(i, soup.text)
            # if 'mtd' in line and 'mi' in line:
            #     print(soup.text)

                # mtrilist.insert(i, soup.text)
        #     if '/mtr' in line and not isfoundcol:
        #         col_size = len(mtrilist)
        #         isfoundcol = true
        #     if 'mfenced' in line:
        #         count = 0
        #     if '/mo' in line and count > 0:
        #         if '=' not in soup.text:
        #             matri_name.insert(0, soup.text)
        #     if '/math' in line and len(matri_name) > 0:
        #         for d in range(0, len(matri_name)):
        #             question += matri_name.pop().strip()
        #         lhs_dict['ques'] = question
        #     if '/mtable' in line:
        #         if not isfoundrow:
        #             siz = len(mtrilist)
        #             row_size = int(siz / col_size)
        #             isfoundrow = true
        #         length = len(matri_name)
        #         matrix_leftside = ''
        #         list = [mtrilist[x:x + col_size] for x in range(0, len(mtrilist), col_size)]
        #         m = Matrix(list)
        #         if length > 2:
        #             for d in range(0, length):
        #                 matrix_leftside += matri_name.pop().strip()
        #             lhs_dict[matrix_leftside.strip()] = m
        #         else:
        #             lhs_dict[matri_name.pop().strip()] = m
        #         mtrilist.clear()
        #     i += 1
        # return lhs_dict

Question().readQFile()