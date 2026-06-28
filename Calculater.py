import tkinter as tk

root = tk.Tk()


root.geometry("600x500")
root.title("Calculator")

lable = tk.Label(root,text="Calculator", font=('Arial',18))
lable.pack(padx=20 , pady=20)

textbox = tk.Text(root ,height=3, font=('Arial', 16))
textbox.pack(padx=10)


button = tk.Button(root, text="Click Me", font=('Arial',10))
button.pack(padx=20 , pady=20)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe , text="1" ,font=('Arial',18) )
btn1.pack(padx=20 , pady=20)
root.mainloop()