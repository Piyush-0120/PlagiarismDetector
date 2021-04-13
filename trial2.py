from tkinter import *
from tkinter import ttk
from KMP import engine
from count_and_suggest import WordSuggest,Counter
def save_info():
    originalText_info = originalText_entry.get(1.0,END)
    patternText_info = patternText_entry.get(1.0,END)
    #print(originalText_info, patternText_info)

    file = open("original.txt", "w")
    file.write(originalText_info)
    file.close()
    file = open("pattern.txt","w")
    file.write(patternText_info)
    file.close()
    print(" text has been registered successfully")
    e =engine()
    e.recieve_data()
    e.send_data()

    plagiarised_percent = e.process()
    space = 8 - len(plagiarised_percent) 
    if float(plagiarised_percent) < 50.0:
        color = "green"
    else : 
        color = "red"

    plag = Label(screen,text="The article is "+plagiarised_percent+"% plagiarised"+" "*space,font=("Tekton Pro",13),fg=color)
    plag.place(x=640,y=520)

    #originalText_entry.delete(1.0, END)
    #patternText_entry.delete(1.0, END)
    #analyzeText_entry.delete(1.0, END)
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
analyzeText_text.place(x=340,y=560)

originalText = StringVar()
patternText = StringVar()
analyzeText = StringVar()


originalText_entry = Text(screen,height="50",width="50")
patternText_entry = Text(screen,height="50",width="50")
analyzeText_entry = Text(screen,height="50",width="50")

originalText_entry.place(x = 150, y = 150, width=500, height=300)
patternText_entry.place(x = 850, y = 150, width=500, height=300)
analyzeText_entry.place(x=340,y=585, width = 800, height=100)

register = Button(screen,text = "Check for Plagiarism", width = "30", height = "2", command = save_info, bg = "grey")
register.place(x = 530, y = 470)


def reset():
    originalText_entry.delete(1.0,END)
    patternText_entry.delete(1.0,END)

reset = Button(screen,text="Reset",width="30",height="2",command=reset,bg="grey")
reset.place(x=770,y=470)

def popupmsg(msg,count):

    popup = Tk()
    popup.wm_title("Analysis")

    if not len(msg):
        msg= "\nNo incorrect words!\n"

    count_statements = "Words : "+str(count[0])+"\nLines : "+str(count[1])+"\nParagraphs : "+str(count[2]); 
    label = ttk.Label(popup, text=count_statements+"\n"+"\nIncorrect words:\n"+msg, font=("Verdana", 10))
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()

def count():
    analyzeText_info = analyzeText_entry.get(1.0,END)

    file = open("analyze.txt", "w")
    file.write(analyzeText_info)
    file.close()

    w = WordSuggest()
    w.recieve_data()
    incorrect_words = ','.join(w.suggestions())

    count = Counter.result(w)

    popupmsg(incorrect_words,count)
  
wordCount = Button(screen,text="Analyse Text",width="30",height="2",command=count,bg="grey")
wordCount.place(x=530,y=720)

def analyze_reset():
    analyzeText_entry.delete(1.0,END)
    count=[]
    incorrect_words=[]

spellCheck = Button(screen,text="Reset",width="30",height="2",command=analyze_reset,bg="grey")
spellCheck.place(x=770,y=720)

screen.mainloop()
