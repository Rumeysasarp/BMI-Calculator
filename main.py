from tkinter import *


window=Tk()
window.minsize(250,200)
window.title("BMI Calculator")

#Label weight
my_label=Label(text="Enter Your Weight(kg)")
my_label.config(fg="purple")
my_label.config(padx=30,pady=10)
my_label.pack()

#Entry
my_entry=Entry(width=15)
my_entry.pack()

#Label height
my_label1=Label(text="Enter Your Height(cm)")
my_label1.config(fg="purple")
my_label1.config(padx=30,pady=10)
my_label1.pack()

#Entry
my_entry1=Entry(width=15)
my_entry1.pack()

# result label
result_label=Label(text="",fg="purple")
result_label.pack()
#Button
def hesapla():
    try:
        kilo = float(my_entry.get())
        boy = float(my_entry1.get())
        ortalama=float( kilo/ boy**2)
        if ortalama<18.5:
          print("Your BMI is Underweight")
        elif 18.5<=ortalama>=24.9 :
          print("Your BMI is Normal")
        elif 25<=ortalama>=29.9 :
          print("Your BMI is Over Weight")
        elif 30<=ortalama>=34.9 :
          print("Your BMI is Obesity(Class 1)")
        elif 35<=ortalama>=39.9:
          print("Your BMI is Obesity (Class 2)")
        else:
          print("Your BMI is Extreme Obesity")
    except ValueError:
        result_label.config(text="Please enter valid numbers!")


my_button=Button(text="Calculate",fg="purple",width=15,command=hesapla)
my_button.pack(pady=10)
window.mainloop()