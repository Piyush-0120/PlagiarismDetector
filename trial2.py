from tkinter import *
from tkinter import ttk

def save_info():
  originalText_info = originalText_entry.get(1.0,END)
  patternText_info = patternText_entry.get(1.0,END)
  print(originalText_info, patternText_info)

  file = open("original.txt", "w")
  file.write(originalText_info)
  file.close()
  file = open("pattern.txt","w")
  file.write(patternText_info)
  file.close()
  print(" text has been registered successfully")
  plag = Label(screen,text="The plagiarism percentage is: ",font=("Tekton Pro",13))
  plag.place(x=420,y=520)

  originalText_entry.delete(1.0, END)
  patternText_entry.delete(1.0, END)
  #return originalText_info, patternText_info

  
screen = Tk()
screen.geometry("1920x1080")
screen.title("PLAGIARISM DETECTOR")
heading = Label(text = "PLAGIARISM DETECTOR", font=("Tekton Pro",14),bg = "black", fg = "white", width = "1500", height = "5")
heading.pack()

 
originalText_text = Label(text = "Orignal Text ")
patternText_text = Label(text = "Suspected Text ")
originalText_text.place(x = 150, y = 120)
patternText_text.place(x = 850, y = 120)
analyzeText_text = Label(text = "Analyze Text")
analyzeText_text.place(x=90,y=530)

originalText = StringVar()
patternText = StringVar()
analyzeText = StringVar()


originalText_entry = Text(screen,height="50",width="50")
patternText_entry = Text(screen,height="50",width="50")
analyzeText_entry = Text(screen,height="50",width="50")

originalText_entry.place(x = 150, y = 150, width=500, height=300)
patternText_entry.place(x = 850, y = 150, width=500, height=300)
analyzeText_entry.place(x=100,y=550, width = 800, height=100)

register = Button(screen,text = "Check for Plagiarism", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 530, y = 470)


def reset():
  originalText_entry.delete(1.0,END)
  patternText_entry.delete(1.0,END)

reset = Button(screen,text="Reset",width="30",height="2",command=reset,bg="grey")
reset.place(x=770,y=470)

def count():
  wcount = Label(screen, text="The Word count of the article is : ", font=("Tekton Pro",13))
  wcount.place(x=940,y=550)
  lcount = Label(screen, text="The Line count of the article is : ", font=("Tekton Pro",13))
  lcount.place(x=940,y=600)
  pcount = Label(screen, text="The Paragraph count of the article is : ", font=("Tekton Pro",13))
  pcount.place(x=940,y=650)
  spellcheck = Label(screen, text="The Incorrect words in the article is : ", font=("Tekton Pro",13))
  spellcheck.place(x=940,y=700)
  
wordCount = Button(screen,text="Analyse Text",width="30",height="2",command=count,bg="grey")
wordCount.place(x=220,y=700)

def analyze_reset():
  analyzeText_entry.delete(1.0,END)

spellCheck = Button(screen,text="Reset",width="30",height="2",command=analyze_reset,bg="grey")
spellCheck.place(x=450,y=700)

screen.mainloop()
