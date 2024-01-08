import model
from tkinter import *
import tkinter as tk
import yargy_services as ys

def showAllInfo():
     text = entry.get()

     result = model.classifier(text) #Обработка названия
     orgName = model.findTegOrg(result)
     showOrgName = tk.Label(window, text=orgName)
     showOrgName.pack()

     addres = model.findAddr(text) #Обработка адреса
     showAddres = tk.Label(window, text=addres)
     showAddres.pack()

     email = model.findEmail(text) #Обработка имейла
     showEmail = tk.Label(window, text=email)
     showEmail.pack()

     number = model.findNumber(text) #Обработка номера
     showNumber = tk.Label(window, text=number)
     showNumber.pack()

     dopInfo = model.findDopInfo(result) #обработка дополнительной информации
     showDopInfo = tk.Label(window, text=dopInfo)
     showDopInfo.pack()

     services = ys.findServices(text) #Обработка услуг лпу
     showServices = tk.Label(window, text=services)
     showServices.pack()

     string1 = '***********'
     string2 = tk.Label(window, text=string1)
     string2.pack()

     scrollbar = tk.Scrollbar(window, orient='vertical', command=text.yview)
     scrollbar.grid(row=0, column=1, sticky=tk.NS)
     showAllInfo['yscrollcommand'] = scrollbar.set

     # mylist = Listbox(window,
     #                  yscrollcommand=scroll_bar.set)
     # mylist.pack(side=RIGHT, fill=BOTH)
     # scroll_bar.config(command=mylist.yview)

window = tk.Tk()
window.geometry("1240x600")

label = tk.Label(text="Имя")
entry = tk.Entry()

label.pack()
entry.pack(anchor=NW, ipadx=500, padx=200, pady=6)

btn = tk.Button(text="Ввод", command=showAllInfo)
btn.place(x=850, y=25, width=75, height=25)
btn.pack(anchor=NW, padx=620, pady=150)

# listbox = Listbox()
# # вертикальная прокрутка
# scrollbar = tk.Scrollbar(orient="vertical", command = listbox.yview)
#
# scrollbar = tk.Scrollbar(orient="vertical", command=listbox.yview)
# scrollbar.pack(side=RIGHT, fill=Y)
# #listbox["yscrollcommand"] = scrollbar.set

# scroll_bar = Scrollbar(command = window.yview)
#
# scroll_bar.pack(side=RIGHT,
#                 fill=Y)



window.mainloop()