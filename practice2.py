"""Q1 create a class called data, in it create class variable called file_name, file_type, date, size,,,,in it a function file_open, which will create file if not exist, in it write something
and another function file_read,which will read dat in the file asked,,,another function to append new data in same file and show
++exception handling and logger{{inside the class create a logging function then using that do the logging"""

import os
import logging
logging.basicConfig(filename="practice2.log", level = logging.DEBUG, format ="%(levelname)s %(asctime)s %(message)s")


class lg:
    def linfos(self,s):
        logging.info(f"execution of {s} function started")
    def linfod(self, s):
        logging.info(f"execution of {s} function done")
    def lerror(self, s):
        logging.error(f"error occured while executing the {s} function")
    def lexception(self, s):
        logging.exception(s)



class data():
    def __init__(self, file_name,file_type, date, size):
        self.file_name = file_name
        self.file_type = file_type
        self.date = date
        self.size = size

    def file_open(self,a):
        lg.linfos(self,"file_open")
        #logging.info("started")
        f = open(a,"w")                 ####f = open(self.file_name + "." + self.file_type,'w')  or f = open(f"{self.file_name}.txt","w") or f = open(f"{self.file_name}.{self.file_type}","w")    these are some other ways to write the file opening syntax with little modifications in rest of code as well to accomodate these syntaxes
        f.write("first time writing using oops concept")
        f.close()
        lg.linfod(self, "file opening")



    """def file_open(self):
        if os.path.isfile(self.file_name):
            with open(self.file_name) as f
                f.read()
        else:
            with open(self.file_name,'w+') as f
                f.write("writing in the file")
    other syntaxes to refer, to know other possibilities in which this code can be written"""



    def file_read(self,a):
        lg.linfos(self,"file_read")
        #logging.info("started")
        try:
            f = open(a, "r+")
            print(f.read())
            f.close()
            lg.linfod(self, "file reading")
        except Exception as e:
            lg.lexception(self,e)
            #logging.exception(e)


    def file_append(self,a):
        lg.linfos(self,"file_append")
        #logging.info("started")
        try:
            f = open(a, "a")
            f.write("appending the file")
            f.close()
            lg.linfod(self,"file appending")
        except Exception as e:
            lg.lexception(self,e)
            #logging.exception(e)



test1 = data("test1.txt", "text file", 2022, 10)
#test1.file_open(test1.file_name)
test1.file_read(test1.file_name)
test1.file_append(test1.file_name)















