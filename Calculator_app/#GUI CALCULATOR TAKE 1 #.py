#GUI CALCULATOR TAKE 1    #YOU CAN DO THIS

#IMPORT MODULES
import customtkinter as ctk
import tkinter as tk


#GLOBAL VARIABLES
global calculation
calculation = ""


def update_calculation(symbol):
    global calculation
    
    calculation += str(symbol)

    display_widget.insert(ctk.END, text=calculation)

    calculation = ""
    
def evaluate_calculation():
    global calculation
    current_calc = display_widget.get("1.0",ctk.END).strip()
    try:
        result = eval(current_calc)
        display_widget.delete('1.0',ctk.END)
        display_widget.insert(ctk.END,text=result)
    except Exception as e:
        display_widget.delete("1.0",ctk.END)
        display_widget.insert(ctk.END,text="Error")

def clear_screen():
    global calculation
    try:
        display_widget.delete("1.0",ctk.END)
        calculation = ""
    except Exception as e:
        display_widget.insert(ctk.END,text="Fatal Error")


#STEP1. SIMPLE GUI--------------------------------------------------------------------------------------------------------------

# MAIN  WINDOW

root = ctk.CTk()
root.title("CALCULATOR GUI BY DTG")
root.geometry("500X500")

#CALCULATION DISPLAY

display_widget = ctk.CTkTextbox(root,width=300,height=50,corner_radius=5,fg_color="grey",)
display_widget.grid(rowspan=5,padx=10,pady=10)


#BUTTON FRAMES

button_frames = ctk.CTkFrame(root,height=300,width=500,fg_color="peachpuff4")
button_frames.grid(padx=10,columnspan=10,column=0,rowspan=10,)

#MAIN BUTTONS #  1,2,3,+

button1 = ctk.CTkButton(button_frames,width=50,height=50,text="1", command= lambda : update_calculation("1"))
button1.grid(row=1,column=0,padx=10,pady=10)

button2 = ctk.CTkButton(button_frames,width=50,height=50,text="2",command= lambda : update_calculation("2"))
button2.grid(row=1,column=1,padx=10,pady=10)

button3 = ctk.CTkButton(button_frames,width=50,height=50,text="3",command= lambda : update_calculation("3"))
button3.grid(row=1,column=2,padx=10,pady=10)

button4 = ctk.CTkButton(button_frames,width=50,height=50,text="+",command= lambda : update_calculation("+"))
button4.grid(row=1,column=3,padx=10,pady=10)

#SECONDARY BUTTONS # 4 5 6 -

button5 = ctk.CTkButton(button_frames,width=50,height=50,text="4",command= lambda : update_calculation("4"))
button5.grid(row=2,column=0,padx=10,pady=10)

button6 = ctk.CTkButton(button_frames,width=50,height=50,text="5",command= lambda : update_calculation("5"))
button6.grid(row=2,column=1,padx=10,pady=10)

button7 = ctk.CTkButton(button_frames,width=50,height=50,text="6",command= lambda : update_calculation("6"))
button7.grid(row=2,column=2,padx=10,pady=10)

button8 = ctk.CTkButton(button_frames,width=50,height=50,text="-",command= lambda : update_calculation("-"))
button8.grid(row=2,column=3,padx=10,pady=10)

#THIRD ROW BUTTONS # 7 8 9 *

button9 = ctk.CTkButton(button_frames,width=50,height=50,text="7",command= lambda : update_calculation("7"))
button9.grid(row=3,column=0,padx=10,pady=10)

button10 = ctk.CTkButton(button_frames,width=50,height=50,text="8",command= lambda : update_calculation("8"))
button10.grid(row=3,column=1,padx=10,pady=10)

button11 = ctk.CTkButton(button_frames,width=50,height=50,text="9",command= lambda : update_calculation("9"))
button11.grid(row=3,column=2,padx=10,pady=10)

button12 = ctk.CTkButton(button_frames,width=50,height=50,text="*",command= lambda : update_calculation("*"))
button12.grid(row=3,column=3,padx=10,pady=10)

#SPECIAL BUTTONS # = 0 CLEAR /

button13 = ctk.CTkButton(button_frames,width=50,height=50,text="=",command=evaluate_calculation)
button13.grid(row=4,column=0,padx=10,pady=10)

button14 = ctk.CTkButton(button_frames,width=50,height=50,text="0",command= lambda : update_calculation("0"))
button14.grid(row=4,column=1,padx=10,pady=10)

button15 = ctk.CTkButton(button_frames,width=50,height=50,text="C",command=clear_screen)
button15.grid(row=4,column=2,padx=10,pady=10)

button16 = ctk.CTkButton(button_frames,width=50,height=50,text="/",command= lambda : update_calculation("/"))
button16.grid(row=4,column=3,padx=10,pady=10)

#GUI COMPLETE--------------------------------------------------------------------------------------------------------------------------

root.mainloop()