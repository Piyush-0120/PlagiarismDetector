import re
from textblob import TextBlob
from database_interactor import readData

text = '''Sorting lists of basic Python objects is generally pretty efficient. The sort method for lists takes an optional comparison function as an argument that can be used to change the sorting behavior. This is quite convenient, though it can significantly slow down your sorts, as the comparison function will be called many times. In Python 2.4, you should use the key argument to the built-in sort instead, which should be the fastest way to sort.

Only if you are using older versions of Python (before 2.4) does the following advice from Guido van Rossum apply:

An alternative way to speed up sorts is to construct a list of tuples whose first element is a sort key that will sort properly using the default comparison, and whose second element is the original list element. This is the so-called Schwartzian Transform, also known as DecorateSortUndecorate (DSU).'''

class Counter:
    
    def result(self):
        word_count = 0
        line_count = 0
        para_count = 0
        counts = list()

        # print(words)
        words = self.text.split()
        word_count = len(words)
        # print('Word Count: ', word_count)
        counts.append(word_count)
        
        lines = self.text.split('.')
        # print(lines)
        for i in lines:
            if (len(i) < 1):
                lines.remove(i)
        
        line_count = len(lines)
        # print('Line Count: ', line_count)
        counts.append(line_count)

        paras = self.text.split('\n')
        # print(paras)
        for i in paras:
            if (len(i) < 1):
                paras.remove(i)

        para_count = len(paras)
        # print('Para Count: ', para_count)
        counts.append(para_count)

        return counts

count = Counter()
# print(count.result(text))

class WordSuggest:

    def recieve_data(self):
        p1 = readData("analyze.txt")
        p1.parse_data()
        self.text = p1.send_data()

    def suggestions(self):
        x=[]
        words = self.text.split()
        punctuation = re.compile(r'[-.?!,:;()|0-9]')
        for word in words:
            s = punctuation.sub('',word)
            x.append(s)
        words = x

        l = list()

        for i in words:
            suggest = TextBlob(i)

            if (i != str(suggest.correct())):
                # print(i + ' -> ' + str(suggest.correct()))
                l.append(i)

        return l


sugg = WordSuggest()
sugg.recieve_data()
print(sugg.suggestions())
print(Counter.result(sugg))
