#https://www.pythontutorial.net/tkinter/tkinter-grid/
from tkinter import *

root=Tk()  #assign tkinter to our root file
root.title("Login form ")   #root title
root.geometry("300x275")   # root size

#Submitting function
def submit():
    if (not nameentry.get()) or (not phoneentry.get()) or (not genderentry.get()) or (not emergencyentry.get()) or (not paymentmoodentry.get()):
        print("You have to fill all details here")
    else:
        print("Accepted")

#page title
Label(root, text="Customer Registration form",font="arial 15 bold",fg='brown').grid(row=0,column=2,columnspan=2,padx=5,pady=10)
root.columnconfigure(1, weight=1)
#feild name
name=Label(root, text="Name",font='bold 10')
phone=Label(root, text="Phone",font='bold 10')
gender=Label(root, text="Gender",font='bold 10')
emergency=Label(root, text="Emergency",font='bold 10')
paymentmood=Label(root, text="Payment mood",font='bold 10')

#packing feilds
name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmood.grid(row=5,column=2)

#variable for storing data
namevalue=StringVar
phonevalue=StringVar
gendervalue=StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar

#creating entry feild
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)
paymentmoodentry = Entry(root, textvariable = paymentmoodvalue)

#Packing entry feild
nameentry.grid(row=1,column=3,padx=10,pady=5,ipadx=30)
phoneentry.grid(row=2,column=3,padx=10,pady=5,ipadx=30)
genderentry.grid(row=3,column=3,padx=5,pady=5,ipadx=30)
emergencyentry.grid(row=4,column=3,padx=5,pady=5,ipadx=30)
paymentmoodentry.grid(row=5,column=3,padx=5,pady=5,ipadx=30)

#creating checkbox
checkbtn=Checkbutton(text="Rememder me?",variable=checkvalue)
checkbtn.grid(row=6,column=3,ipadx=5)

#creating submit
Button(text="Submit the form",font="bold 12 ",command=submit,bg='brown',fg='white').grid(row=9,column=3,ipadx=30)


root.mainloop()

#ipadx=incease the length of a textfeild
