import logging
logging.basicConfig(filename="strings.log", level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")



class string1:
    logging.info("we are accessing class string1")


###string jump function
    def jump3(self,j_string):
        logging.info("we are about to extract string from 1 to 300 with a jump of 3")
        self.j_string = j_string
        try:
            if len(j_string)==0:
                raise Exception("empty string")
            else:
                str=j_string[::3]
                logging.info("extracted string is %s:", str)
                return str
        except Exception as e:
            logging.exception(e)

 ###string reverse

    def reverse1(self,r_string):
        logging.info("we are about to reverse string")
        self.r_string= r_string
        try:
            if len(r_string)==0:
                raise Exception("empty string")
            else:
                str =r_string[::-1]
                logging.info("reversed string is %s", str)
                return str
        except Exception as e:
            logging.exception(e)


###upper and split of string
    def upsp(self,us_string):
        logging.info("e are about to write the string in upper letter then split")
        self.us_string = us_string
        try:
            if len(us_string)==0:
                raise Exception("empty string")
            else:
                str= us_string.upper()
                str1=str.split(' ')
                logging.info("changing string into upper letter and then splitting them has been done")
                return str1
        except Exception as e:
            logging.exception(e)


 ###loeering the letters of the string
    def lower1(self,l_string):
        logging.info("we will lower the letters of the string")
        self.l_string =l_string
        try:
            if len(l_string)==0:
                raise Exception("empty string")
            else:
                str =l_string.lower()
                logging.info("the string's alphabets has been lowered")
                return str
        except Exception as e:
            logging.exception(e)


### lowering the string

    def replace1(self,re_string,a,b,c):
        logging.info("in this we will replace the string")
        self.re_string =re_string
        try:
            if len(re_string)==0:
                raise Exception("empty string")
            else:
                str= re_string.replace(a,b,c)
                logging.info("replaced string")
                return str
        except Exception as e:
            logging.exception(e)


try:

    a=string1()
    b =string1()
    s1="rajesh singh"
    s2 = "coincidece"
    logging.info("calling the functions from the strin1 class")
    print(a.jump3(s1))
    print(a.reverse1(s1))
    print(a.upsp(s1))
    print(a.lower1(s1))
    print(b.replace1(s2,'c','l',-1))

except TypeError as q:
    print(q)
    logging.exception(q)
except AttributeError as t:
    print(t)
    logging.exception(t)
except Exception as e:
    print(e)



