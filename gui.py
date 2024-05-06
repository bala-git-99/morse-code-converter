import tkinter
from tkinter import *
import converters


def display_output_1(event=None):
    input_str = e_input_1.get()
    output = converters.to_morse_code(input_str)
    l_output_1.delete(1.0, tkinter.END)
    l_output_1.insert(tkinter.END, output)


window = tkinter.Tk()
window.title("Morse Code Converter")
window.config(pady=50, padx=50)

canvas = tkinter.Canvas(width=200, height=200, )
morse_png = tkinter.PhotoImage(file="morse.png")
canvas.pack(expand=YES, fill=BOTH)
canvas.create_image(0, 0, image=morse_png, anchor=NW)
canvas.grid(row=0, column=0)

l_input_1 = tkinter.Label(text="Enter text to convert to Morse code:")
l_input_1.grid(row=1, column=0)

e_input_1 = tkinter.Entry()
e_input_1.grid(row=2, column=0, sticky="EW")
e_input_1.focus()

l_output_1 = tkinter.Text(wrap="word", width=40, height=3)
l_output_1.grid(row=3, column=0, sticky="ew")

e_input_1.bind("<Return>", display_output_1)


def flip():
    def display_output_2(event=None):
        input_str = e_input_2.get()
        output = converters.to_decode(input_str)
        l_output_2.delete(1.0, tkinter.END)
        l_output_2.insert(tkinter.END, output)

    global l_input_1, e_input_1, l_output_1

    if l_input_1 and e_input_1 and l_output_1:
        l_input_1.destroy()
        e_input_1.destroy()
        l_output_1.destroy()

        l_input_2 = tkinter.Label(text="Enter Morse code to decode:\n(Note-leave a space between letters and \n"
                                       "the words are separated by /)")
        l_input_2.grid(row=1, column=0)

        e_input_2 = tkinter.Entry()
        e_input_2.grid(row=2, column=0, sticky="EW")
        e_input_2.focus()

        l_output_2 = tkinter.Text(wrap="word", width=40, height=3)
        l_output_2.grid(row=3, column=0, sticky="ew")

        e_input_2.bind("<Return>", display_output_2)


create_button = tkinter.Button(text="Flip", command=flip)
create_button.grid(row=0, column=1, sticky="EW")

window.mainloop()
