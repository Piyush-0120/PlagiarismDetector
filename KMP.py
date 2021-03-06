from database_interactor import readData
from parser2_v2 import Parser2
def transition_function(P):
    '''
    A utility function that creates a PI table needed to
    avoid back-tracking on 'Text' array.
    :param P:
    :return a:
    '''
    m = len(P)
    k=0
    a=[0]*m
    for i in range(1,m):
        while k>0 and P[k]!=P[i]:
            k=a[k-1]
        if P[k]==P[i]:
            k += 1
            a[i]=k
    return a
def KnuthMorrisPratt(T,P):
    '''
    The main algorithmic implementation of KMP Algorithm to search against
    plagiarisation in given two texts. We return count of matched patterns.
    :param T:
    :param P:
    :return count:
    '''
    k=0
    m=len(P)
    n=len(T)
    flag=0
    count = 0
    a = transition_function(P)
    for i in range(n):
        while k>0 and T[i]!=P[k]:
            k=a[k-1]
        if T[i]==P[k]:
            if k == m - 1:
                #print("Shift found at ", i - m + 1)
                count+=1
                flag = 1
                k = a[k]
            else:
                k+=1

    return count


class engine:
    def recieve_data(self):
        '''
        Collects data from database
        :return None :
        '''
        p1 = readData("original.txt")
        p1.parse_data()
        self.data1 = p1.send_data()
        p2 = readData("pattern.txt")
        p2.parse_data()
        self.data2 = p2.send_data()
    def send_data(self):
        '''
        Sends the required data to whatever file asks for it
        :return None:
        '''
        ob1 = Parser2(self.data1)
        ob2 = Parser2(self.data2)
        self.text = set(ob1.parsed_words())
        self.patt = set(ob2.parsed_words())
        self.total_words1 = len(self.text)
        self.total_words2 = len(self.patt)

    def process(self):
        '''
        A utility function that processes the obtained data and returns the percentage
        of plagiarisation bw the original text and suspected text!
        :return String type data:
        '''
        c = 0
        for i in self.patt:
            for j in self.text:
                if len(i) == len(j):
                    c += KnuthMorrisPratt(j, i)
                    #print(i,j,c)

        if not c:
            print("No Plagiarism")
            return str(0.00)
        else:
            print("count:",c)
            plag_percent = (2 * c) /(self.total_words1+self.total_words2) 
            print("The article is %f %% plagiarised" %( plag_percent * 100))
            return str(plag_percent * 100)[0:6]
'''
To instantiate the class, the following calls need to be made       
ob = engine()
ob.recieve_data()
ob.send_data()
print(ob.process())
'''

