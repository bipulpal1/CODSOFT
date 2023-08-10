import tkinter as tk

user_interface = tk.Tk()
user_interface.geometry("400x350")

calculation = ""

def input_element(element):
    global calculation
    calculation +=str(element)
    result.delete(1.0,tk.END)
    result.insert(1.0,calculation)


def calculate_value():
    global calculation
    try:
        calculation = str(eval(calculation))
        result.delete(1.0,tk.END)
        result.insert(1.0,calculation)
    except:
        clear()
        result.insert(1.0,"ERROR")


def clear():
    global calculation
    calculation = ""
    result.delete(1.0,tk.END)


result = tk.Text(user_interface,height=4,width=47,font = (30))
result.grid(columnspan=5)

btn_openpara = tk.Button(user_interface,text="(",command=lambda:input_element("("),width=5,font=("Arial",15))
btn_openpara.grid(row=5,column=0,padx=5, pady=5)
btn_0 = tk.Button(user_interface,text="0",command=lambda:input_element(0),width=5,font=("Arial",15))
btn_0.grid(row=5,column=1,padx=5, pady=5)
btn_closepara = tk.Button(user_interface,text=")",command=lambda:input_element(")"),width=5,font=("Arial",15))
btn_closepara.grid(row=5,column=2,padx=5, pady=5)
btn_enter = tk.Button(user_interface,text="=",command=calculate_value,width=5,font=("Arial",15))
btn_enter.grid(row=5,column=3,padx=5, pady=5)


btn_1 = tk.Button(user_interface,text="1",command=lambda:input_element(1),width=5,font=("Arial",15))
btn_1.grid(row=4,column=0,padx=5, pady=5)
btn_2 = tk.Button(user_interface,text="2",command=lambda:input_element(2),width=5,font=("Arial",15))
btn_2.grid(row=4,column=1,padx=5, pady=5)
btn_3 = tk.Button(user_interface,text="3",command=lambda:input_element(3),width=5,font=("Arial",15))
btn_3.grid(row=4,column=2,padx=5, pady=5)
btn_add = tk.Button(user_interface,text="+",command=lambda:input_element("+"),width=5,font=("Arial",15))
btn_add.grid(row=4,column=3,padx=5, pady=5)

btn_4 = tk.Button(user_interface,text="4",command=lambda:input_element(4),width=5,font=("Arial",15))
btn_4.grid(row=3,column=0,padx=5, pady=5)
btn_5 = tk.Button(user_interface,text="5",command=lambda:input_element(5),width=5,font=("Arial",15))
btn_5.grid(row=3,column=1,padx=5, pady=5)
btn_6 = tk.Button(user_interface,text="6",command=lambda:input_element(6),width=5,font=("Arial",15))
btn_6.grid(row=3,column=2,padx=5, pady=5)
btn_subtract = tk.Button(user_interface,text="-",command=lambda:input_element("-"),width=5,font=("Arial",15))
btn_subtract.grid(row=3,column=3,padx=5, pady=5)

btn_7 = tk.Button(user_interface,text="7",command=lambda:input_element(7),width=5,font=("Arial",15))
btn_7.grid(row=2,column=0,padx=5, pady=5)
btn_8 = tk.Button(user_interface,text="8",command=lambda:input_element(8),width=5,font=("Arial",15))
btn_8.grid(row=2,column=1,padx=5, pady=5)
btn_9 = tk.Button(user_interface,text="9",command=lambda:input_element(9),width=5,font=("Arial",15))
btn_9.grid(row=2,column=2,padx=5, pady=5)
btn_multiply = tk.Button(user_interface,text="*",command=lambda:input_element("*"),width=5,font=("Arial",15))
btn_multiply.grid(row=2,column=3,padx=5, pady=5)

btn_clear = tk.Button(user_interface,text="AC",command=clear,width=5,font=("Arial",15))
btn_clear.grid(row=1,column=0,padx=5, pady=5)
btn_DEL = tk.Button(user_interface,text="Del",command=lambda:input_element("Del"),width=5,font=("Arial",15))
btn_DEL.grid(row=1,column=1,padx=5, pady=5)
btn_decimal = tk.Button(user_interface,text=".",command=lambda:input_element("."),width=5,font=("Arial",15))
btn_decimal.grid(row=1,column=2,padx=5, pady=5)
btn_divide = tk.Button(user_interface,text="/",command=lambda:input_element("/"),width=5,font=("Arial",15))
btn_divide.grid(row=1,column=3,padx=5, pady=5)


user_interface.mainloop()