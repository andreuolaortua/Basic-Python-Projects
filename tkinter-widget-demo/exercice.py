from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    km_result.config(text=f"{km}")

#Creating a new window and configuration
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

#Labels
label = Label(text="is equal to")
label.config(text="is equal to")
label.grid(column=0, row=1)

label2 = Label(text="Miles")
label2.config(text="Miles")
label2.grid(column=2, row=0)

label3 = Label(text="Km")
label3.config(text="Km")
label3.grid(column=2, row=1)

#calls action() when pressed
button = Button(text="Calculate")
button.grid(column=1, row=2)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

miles_to_km()


window.mainloop()