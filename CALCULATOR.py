import tkinter as tk

calculation=""

def add_calculate(symbol):
    global calculation
    calculation+=str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)
def evaluate():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_feild()
        text_result.insert(1.0,"Error")
def clear_feild():
    text_result.delete(1.0,"end")


root=tk.Tk()
root.geometry("300x275")
text_result=tk.Text(root,height=2,width=16,font=('Arial',24))
text_result.grid(columnspan=5)
btn_1=tk.Button(root,text="1",width=5,command=lambda: add_calculate("1"),font=('Arial',14))
btn_1.grid(row=2,column=1)
btn_2=tk.Button(root,text="2",width=5,command=lambda: add_calculate("2"),font=('Arial',14))
btn_2.grid(row=2,column=2)
btn_3=tk.Button(root,text="3",width=5,command=lambda: add_calculate("3"),font=('Arial',14))
btn_3.grid(row=2,column=3)
btn_4=tk.Button(root,text="4",width=5,command=lambda: add_calculate("4"),font=('Arial',14))
btn_4.grid(row=3,column=1)
btn_5=tk.Button(root,text="5",width=5,command=lambda: add_calculate("5"),font=('Arial',14))
btn_5.grid(row=3,column=2)
btn_6=tk.Button(root,text="6",width=5,command=lambda: add_calculate("6"),font=('Arial',14))
btn_6.grid(row=3,column=3)
btn_7=tk.Button(root,text="7",width=5,command=lambda: add_calculate("7"),font=('Arial',14))
btn_7.grid(row=4,column=1)
btn_8=tk.Button(root,text="8",width=5,command=lambda: add_calculate("8"),font=('Arial',14))
btn_8.grid(row=4,column=2)
btn_9=tk.Button(root,text="9",width=5,command=lambda: add_calculate("9"),font=('Arial',14))
btn_9.grid(row=4,column=3)
btn_0=tk.Button(root,text="0",width=5,command=lambda: add_calculate("0"),font=('Arial',14))
btn_0.grid(row=5,column=2)
btn_plus=tk.Button(root,text="+",width=5,command=lambda: add_calculate("+"),font=('Arial',14))
btn_plus.grid(row=2,column=4)
btn_minus=tk.Button(root,text="-",width=5,command=lambda: add_calculate("-"),font=('Arial',14))
btn_minus.grid(row=3,column=4)
btn_mul=tk.Button(root,text="x",width=5,command=lambda: add_calculate("*"),font=('Arial',14))
btn_mul.grid(row=4,column=4)
btn_div=tk.Button(root,text="/",width=5,command=lambda: add_calculate("/"),font=('Arial',14))
btn_div.grid(row=5,column=4)
btn_lb=tk.Button(root,text="(",width=5,command=lambda: add_calculate("("),font=('Arial',14))
btn_lb.grid(row=5,column=1)
btn_rb=tk.Button(root,text=")",width=5,command=lambda: add_calculate(")"),font=('Arial',14))
btn_rb.grid(row=5,column=3)
btn_equal=tk.Button(root,text="=",width=11,command=lambda: evaluate(),font=('Arial',14))
btn_equal.grid(row=6,column=1,columnspan=1)
btn_div=tk.Button(root,text="AC",width=11,command=lambda: clear_feild(),font=('Arial',14))
btn_div.grid(row=6,column=3,columnspan=2)
root.mainloop()