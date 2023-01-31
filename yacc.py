# -- coding: UTF-8 --
import ply.yacc as yacc
import pyarabic.araby as araby
import pyarabic.number as number
import sys
import arabic_reshaper
import bidi.algorithm
from bidi.algorithm import get_display
from awesometkinter.bidirender import add_bidi_support, render_text
from tkinter import *
from lex import tokens
from tkinter import filedialog
from tkinter.ttk import Button


#def p_FI3L(p):
#        'FI3L :قل'
#        p[0]=p[1]
#def p_DAMIR(p):
#        'DAMIR :هو'
#        p[0]=p[1]
#def p_ISM(p):
#        'ISM : أحد'
#        p[0]=p[1]
#def p_ISMJ(p):
#        'ISM : الله '
#        p[0]=p[1]
def p_ikhlas(p):
    'ikhlas : bassmala issmj1 sifa sifa2 fi3lamr damir issmj2 issm INT issmj2 moubtada2 INT 7arfjazm moudari32 7arf3atf 7arfjazm mad INT 7arf3atf 7arfjazm moudari31 7arfjar4 khabar issm INT'
    print('Surat al ikhlas est correcte')
    f= open("resultat.txt","w+")
    f.write('Surat al ikhlass est correcte\n')
    f.write('\n')
    f.close() 

def p_fala9(p):
    'ikhlas : bassmala issmj1 sifa sifa2 fi3lamr a3oudou 7arfjar1 rabi moudafilayh INT 7arfjar2 ismmbm ismmawsoul fi3lmad INT 7arf3atf 7arfjar2 ismmbm modaf1 darfzaman fi3l2 INT 7arf3atf 7arfjar2 ismmbm modaf22 7arfjar3 ismajrour2 INT 7arf3atf 7arfjar2 ismmbm modaf2 darfzaman modaf3 INT'
    print('Surat al falaq est correcte')
    f= open("resultat.txt","w+")
    f.write('Surat al falaq est correcte\n')
    f.write('\n')
    f.close() 
def p_error(p):
    print("Le verset coranique est erroné essayez encore une fois")
    f= open("resultat.txt","w+")
    f.write('Le verset coranique est erroné essayez encore une fois')
    f.write('\n')
    f.close() 


parser =yacc.yacc()



#path = r'C:\Users\ikram\Desktop\Compil\Compil\surat_alikhlas.txt'
path = r'C:\Users\ikram\Desktop\Compil\Compil\suratalfalaq.txt'

file = open(path, 'r',encoding='utf-8')
data = file.read()

parser.parse(data)

ws = Tk()
ws.title("Quran Checker")
ws.geometry('400x300')
ws['bg'] = '#A6CFD5'

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)
#quran_input = Entry(ws)
#quran_input.pack(pady=30)
#add_bidi_support(ws)

#data = quran_input.get()

def openFile1():
    tf = filedialog.askopenfilename(
        initialdir="C:/Users/MainFrame/Desktop/", 
        title="Ouvrir un fichier", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf, 'r',encoding='utf-8')  # or tf = open(tf, 'r')
    rd = tf.read()
    
    data=txtarea.insert(END, parser.parse(rd))

    tf.close()

Button(
    ws, 
    text="Open File", 
    command=openFile1
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)


def parse():
    parser.parse(data)
txtarea = Text(ws, width=60, height=8)
txtarea.pack(pady=20)


def openFile2():
    tf = open('resultat.txt')
    file_cont = tf.read()
    txtarea.insert(END, file_cont)
    tf.close()
Button(
    ws,
    text="Vérifier verset", 
    #padx=10, 
    #pady=5,
    #bg='#ffffff',
    command=lambda: [parse(), openFile2()]
    ).pack()

ws.mainloop()


