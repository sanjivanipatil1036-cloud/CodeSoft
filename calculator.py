import tkinter as tkr


root = tkr.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)


entry = tkr.Entry(root, width=20, borderwidth=5, font=('Arial', 18), justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def click(symbol):
    current = entry.get()
    entry.delete(0, tkr.END)
    entry.insert(tkr.END, current + str(symbol))

def clear():
    entry.delete(0, tkr.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tkr.END)
        entry.insert(tkr.END, str(result))
    except:
        entry.delete(0, tkr.END)
        entry.insert(tkr.END, "Error")
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
]

for (text, row, col) in buttons:
    if text == '=':
        btn = tkr.Button(root, text=text, width=5, height=2, bg="#90EE90", command=calculate)
    else:
        btn = tkr.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    btn.grid(row=row, column=col, padx=5, pady=5)

tkr.Button(root, text="C", width=23, height=2, bg="#FF7F7F", command=clear).grid(row=5, column=0, columnspan=4, padx=5, pady=5)

root.mainloop()
