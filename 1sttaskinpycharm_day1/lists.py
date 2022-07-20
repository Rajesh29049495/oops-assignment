import logging
logging.basicConfig(filename="lists.log", level=logging.DEBUG,format="%(levelname)s %(asctime)s %(message)s")


class list1:
    logging.info("log for list class")

    ###reversing the list
    def reverse1(self,l_rev):
        logging.info("we are about to reverse list")
        self.l_rev=l_rev
        try:
            if len(l_rev)==0:
                raise Exception("list is empty")
            else:
                l_rev.reverse()
                logging.info("reverse list is %s ", l_rev)
                return l_rev
        except Exception as e:
            logging.exception(e)

    ##extract number from list
    def call1(self,l1,a):
        logging.info("we about to find the number")
        self.l1=l1
        try:
            if len(l1)==0:
                raise Exception("empty list")
            else:
                l4=[]
                for i in l1:
                    if i==a:
                        l4.append(i)
                    if type(i)==tuple or type(i)==set or type(i)==list:
                        for j in i:
                            if j==a:
                                l4.append(j)
                    if type(i)==dict:
                        for k in i.keys():
                            if k ==a:
                                 l4.append(k)
            return l4
        except Exception as e:
            logging.exception(e)


    ###extract list from the list
    def extractl(self,l1):
        logging.info("we are bout to extract lists from the list")
        self.l1=l1
        try:
            if len(l1)==0:
                raise Exception("empty list")
            else:
                l2=[]
                for i in self.l1:
                    if type(i)==list:
                        l2.append(i)
            return l2
        except Exception as e:
            logging.exception(e)


###extract string from the list
    def extracts(self,l1,a):
        logging.info("we are about to extract string from the list")
        self.l1=l1
        try:
            if len(l1)==0:
                raise Exception("empty list")
            else:
                l3=[]
                for i in self.l1:
                    if type(i)==dict:
                        for k in i.values():
                            if k ==a:
                                l3.append(k)
            return l3
        except Exception as e:
            logging.exception(e)







l8 =list1()
l0=[3,4,5,6,7 , [23,456,67,8,78,78] , [345,56,87,8,98,9] , (234,6657,6) , {"key1" :"sudh" , 234:[23,45,656]}]
logging.info("list on which list operations about to be perfprmed has been entered ")
try:
    print(l8.reverse1(l0))
    print(l8.call1(l0,234))
    print(l8.call1(l0,456))
    print(l8.extractl(l0))
    print(l8.extracts(l0,'sudh'))
    logging.info("sucessfully all list operations performed")
except Exception as e:
    print(e)