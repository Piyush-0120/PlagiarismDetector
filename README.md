# Plagiarism Detector

The earnest goal of this project is to help our users detect Plagiarisation in the quickest and most effective manner. With the help of ‘Plagiarisation Detector’ we aim to check for plagiarisation between two documents and also provide our users features like word count, line count, paragraph count and also spelling errors. All of this is mounted on a robust and user-friendly GUI. The algorithm for string matching is **KMP (Knuth Morris Pratt)** algorithm.

### Time Complexity of KMP
* Preprocessing time : **O(m)**
* Matching time : **O(n)**

Thus we can see that the total time complexity of KMP algorithm is **O(m+n)** which is a **linear time complexity** and where m is size of pattern string and n is size of main string.


## Flow of execution of Plagiarism Detector
![image](https://user-images.githubusercontent.com/65674133/119248748-f1c83480-bbb0-11eb-9f4e-e0e17bf174ca.png)

* Input document :
  * Input document is given for recognition the document can be any journal or paper. 
* Keyword extraction 
  * The keywords from that document have been extracted for comparing it with other document. 
* Algorithm :
  * Here we have used the KMP algorithm to find out any suspicious matter in the document. 
* Discovery of similarity :
  * After going through the algorithms any similarity can be judged or discovered.
* Plagiarism percent:
  * The plagiarism percentage is calculated by the formula below:
2* (count of similar words)*100/(parsed words of doc1 + parsed words of doc2)%


## Flow of execution of Special Features
![image](https://user-images.githubusercontent.com/65674133/119248774-16241100-bbb1-11eb-977b-767d2ebc9937.png)

* Input document :
  * Input document is given for analysis. 
* Preprocessing :
  * Document is broken down to paragraphs, sentences, words.
* Discovery of spell errors:
  * Using TextBlob library we discover the words with spelling mistakes 
* Output :
  * Displaying the word, paragraph and sentence count.

## How it Looks like

![image](https://user-images.githubusercontent.com/65674133/119249714-62268400-bbb8-11eb-820a-ace3743158e5.png)

![image](https://user-images.githubusercontent.com/65674133/119249720-6b175580-bbb8-11eb-8cec-3ce9530c8f09.png)

# Contribution
I would like to thank the collaborators
* [Sayantan-codes](https://github.com/Sayantan-codes)
* [GauravGupta](https://github.com/GauravGupta035)
* [sakar900](https://github.com/sakar900)

