class readData:
    def __init__(self,filename):
        self.fname = filename
    def parse_data(self):
        '''
        reading from the locally saved files and storing the data dynamically
        for the program
        :return None:
        '''
        self.st=''
        f = open(self.fname,'r')
        for i in f.read().split('\n'):
            self.st += i+'\n'
    def send_data(self):
        '''
        The parsed data is sent to the calling function/file
        :return A string type data:
        '''
        return self.st

'''
Instantiate the class in the following manner:- 
p1 = readData("file1.txt")
p1.parse_data()
data1 = p1.send_data()
p2=readData("file2.txt")
p2.parse_data()
data2 = p2.send_data()
'''
