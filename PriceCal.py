import tkinter as tk
from functools import partial

#this is the main in which the program logic is calculated
def call_result(mil, comp, reg):
   #if the mileage is more than 1200, the price will increase by $20,000, else the price will increase by $10,000
   if(int(mil.get())>=1200):
      cr1=20000
   else:
      cr1=10000
   #if the company of the car is Mercedes, Ford or Porsche, the price will increase by $50,000, else the price will increase by $30,000
   if(comp.get()=="Mercedes" or comp.get()=="Ford" or comp.get()=="Porsche"):
      cr2=50000
   else:
      cr2=30000
   #if the registration is older than 10 years, the price will increase by $10,000, else the price will increase by $20,000
   if(int(reg.get())>10):
      cr3=10000
   else:
      cr3=20000
   #The total price is the sum of the above 3 critereas and the base price of $40,000
   result=40000+int(cr1)+int(cr2)+int(cr3)
   resultLabel.config(text="Final Price is %d" %result)
   return

root=tk.Tk()
root.geometry('400x200+100+200')
root.title('Second Hand Car Price Calculator')

m=tk.StringVar()
c=tk.StringVar()
r=tk.StringVar()

mileageLabel=tk.Label(root, text="Mileage")
mileageLabel.grid(row=0, column=0)

mileageEntry=tk.Entry(root, textvariable=m)
mileageEntry.grid(row=0, column=2)

companyLabel=tk.Label(root, text="Company")
companyLabel.grid(row=1, column=0)

companyEntry=tk.Entry(root, textvariable=c)
companyEntry.grid(row=1, column=2)

registrationLabel=tk.Label(root, text="Registration")
registrationLabel.grid(row=2, column=0)

registrationEntry=tk.Entry(root, textvariable=r)
registrationEntry.grid(row=2, column=2)

resultLabel=tk.Label(root)
resultLabel.grid(row=4, column=2)

call_result=partial(call_result, m, c, r)
buttonCal=tk.Button(root, text="Calculate", command=call_result)
buttonCal.grid(row=4, column=0)

root.mainloop()