import math
from tkinter import*

list_NS=["1","2","3","4","5","6","7","8","9","0","-","+","/","*","**"]
list_NP=["SIS","COS","TAN"]
ecran=Tk()
ecran.geometry("600x600")
ecran.config(bg="white")
ecran.title("PROJET 1")
ecran.iconbitmap()
frame_entry=Frame(ecran)
frame_entry.grid(column=0,row=0)
frame_button=Frame(ecran)
frame_button.grid(column=0,row=2)
label=Label(frame_entry,text="THE CALCULATOR",font=("Courier",40),bg="lightblue",fg="red")
label.grid(column=0,row=0)
def saisie(nombre):
   recup=saisie_entry.get()
   saisie_entry.delete(0,END)
   saisie_entry.insert(0,recup+str(nombre))
def resultat():
  try:   
   recupe=saisie_entry.get()  
   resultat_entry.insert(0,str(eval(recupe)))
  except (SyntaxError,ValueError,NameError):
      resultat_entry.insert(0,"HA ERREUR")
      saisie_entry.insert(0,"HA ERROR")
def delete():
    saisie_entry.delete(0,END)
    resultat_entry.delete(0,END)
def calcule_spaciale():
 try:
    recuper=float(saisie_entry.get())
    resultat_entry.insert(0,(math.cos(recuper)))
    resultat_entry.insert(0,(math.tan(recuper)))
    resultat_entry.insert(0,(math.sin(recuper)))
 except(ValueError,NameError):
    resultat_entry.insert(0,"HA ERREUR")
    saisie_entry.insert(0,"HA ERROR")   
def calcule_TS():
   recupere=saisie_entry.get()
   resultat_entry.insert(0,math.sqrt(float(recupere)))
saisie_entry=Entry(frame_entry,font=("arial",30),width=40)
saisie_entry.grid(column=0,row=1)
resultat_entry=Entry(frame_entry,font=("arial",30),width=40)
resultat_entry.grid(column=1,row=1)
for x,z in enumerate(list_NS):
    for e,a in enumerate(list_NP):
      button_NS=Button(frame_button,text=f"{z}",font=("Courier",20),bg="black",fg="red",width=20,command=lambda z=z : saisie(f"{z}"))
      button_NP=Button(frame_button,text=f"{a}",font=("Courier",20),bg="black",fg="red",width=20,command= calcule_spaciale)
      column=(x%5)+1
      column1=(e%5)+1
      row=(x//5)+1
      row1=(e//5)+4
      button_NS.grid(column=column,row=row)
      button_NP.grid(column=column1,row=row1)    
button_resultat=Button(frame_button,text="=",font=("Courier",20),bg="black",fg="red",width=20,command= resultat)
button_resultat.grid(column=4,row=4)
button_delete=Button(frame_button,text="SUPP",font=("Courier",20),bg="black",fg="red",width=20,command=delete)
button_delete.grid(column=5,row=4)
button_CTS=Button(frame_button,text="RC",font=("Courier",20),bg="black",fg="red",width=20,command=calcule_TS)
button_CTS.grid(column=5,row=5)
menu=Menu()







ecran.mainloop()      



