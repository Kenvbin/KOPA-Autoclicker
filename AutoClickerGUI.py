import math, os
import tkinter as tk
from tkinter import DISABLED, NORMAL, TOP, Entry, Spinbox, StringVar, OptionMenu, ttk


root = tk.Tk()

root.title("Auto Clicker")
#Uncomment when compiling into an exe
# root.iconbitmap("AutoClickerGUI.exe")

#Makes it so window stays specific size
root.geometry("443x325")
root.minsize(443, 325)
root.maxsize(443, 325)

root.attributes('-topmost', True)

def SetKey():
    secondary_window = tk.Toplevel()
    secondary_window.title("Set Hotkey")
    secondary_window.geometry("300x200")
    secondary_window.minsize(300,200)
    secondary_window.maxsize(300,200)
    
    secondary_window.attributes('-topmost', True)
    secondary_window.grab_set()
    
    KeyFrame = tk.Frame(secondary_window)
    KeyFrame.columnconfigure(0, weight=1)
    KeyFrame.columnconfigure(1, weight=1)
    
    button_close = tk.Button(KeyFrame, text="Set Key",font=('Helvetica 20 bold'))
    button_close.grid(row=0,column=0,pady=20)        
    
    mystr = StringVar() 
    mystr.set('F6') 
    
    button_close = Entry(KeyFrame, justify='center', state=DISABLED,font=('Helvetica 30 bold'), textvariable=mystr, width=6)
    button_close.grid(row=0,column=1)        
    
    button_close = tk.Button(KeyFrame, text="Save",font=('Helvetica 20 bold'),width=7)
    button_close.grid(row=1,column=0)        
    
    button_close = tk.Button(KeyFrame, text="Close",font=('Helvetica 20 bold'), command=secondary_window.destroy,width=7)
    button_close.grid(row=1,column=1)
    
    KeyFrame.pack(fill="both")




def AlwaysThere():
    global row1, radio_var,radio_var2
    
    def toggle():
        if toggle_button.config('text')[-1] == 'CPS':
            toggle_button.config(relief="raised", text="Timer")
            ClicksPerSecondGUI()
        else:
            toggle_button.config(relief="raised", text="CPS")
            TimedClicks()

    row1 = tk.Frame(root)
    for i in range(5):
        row1.columnconfigure(i, weight=1)
    
    toggle_button = tk.Button(row1, text="CPS", width=10, relief="raised", command=toggle)
    toggle_button.grid(row=1, column=0, pady=10, padx=10)
    
    e_space = tk.Label(row1, text="")
    e_space.grid(row=1, column=1, padx=25)


    Click_type = tk.Label(row1, text="Type of Click: ", justify="left")
    Click_type.grid(row=1, column=2, pady=10, padx=10)
    OPTIONS = [
        "Left",
        "Right",
    ]

    variable = StringVar(root)
    variable.set(OPTIONS[0])  # default value

    click_dropdown = OptionMenu(row1, variable, *OPTIONS)
    click_dropdown.grid(row=1, column=3, pady=0, padx=0)

    row1.pack(pady=10)
    
    row2 = ttk.Frame(root)
    for i in range(5):
        row2.columnconfigure(i, weight=1)

    radio_var = tk.StringVar(value="repeat_until_stopped")
    
    repeat_diamond1 = ttk.Radiobutton(row2, text="Repeat", variable=radio_var, value="repeat")
    repeat_diamond1.grid(row=2,column=0)

    def validate_number(value):
        # Check if the value is empty or consists only of digits
        return value.isdigit() or value == ""
    
    row2.register(validate_number)

    times = Spinbox(row2,validate='key', validatecommand=(root.register(validate_number), '%P'), width=5, from_=1, to=math.inf, justify='center')
    times.grid(row=2, column=1)
    
    label = tk.Label(row2, text='time(s)')
    label.grid(row=2, column=2)
    
    e_space1 = tk.Label(row2, text="")
    e_space1.grid(row=2, column=3, padx=20)
    
    repeat_diamond2 = ttk.Radiobutton(row2, text="Repeat until stopped", variable=radio_var, value="repeat_until_stopped")
    repeat_diamond2.grid(row=2,column=4)
    
    row2.pack(pady=20)
    
    tk.Label(root, text='Cursor Position:',justify="left").pack(side= TOP, anchor="w", padx=10, pady=10)
    
    row4 = tk.Frame(root)
    for i in range(9):
        row4.columnconfigure(i, weight=1)
    
    radio_var2 = tk.StringVar(value="current_location")
    
    CurrentLoc_Diamond = ttk.Radiobutton(row4,text="Current location", variable=radio_var2, value="current_location")
    CurrentLoc_Diamond.grid(row=4,column=0)
    
    tk.Label(row4, text="").grid(row=4, column=1, padx=20)
    
    CustomLoc_Diamond = ttk.Radiobutton(row4,text="", variable=radio_var2, value="custom_location")
    CustomLoc_Diamond.grid(row=4,column=2)
    
    Picker_button = ttk.Button(row4, text="Pick location")
    Picker_button.grid(row=4,column=3)
    
    tk.Label(row4, text="X").grid(row=4, column=4, padx=5)

    x_val = Entry(row4, validate='key', validatecommand=(root.register(validate_number), '%P'), width=5, justify='right')
    x_val.grid(row=4, column=5, padx=0, pady=0, sticky="w") 
    
    tk.Label(row4, text="Y").grid(row=4, column=6, padx=5)

    y_val = Entry(row4, validate='key', validatecommand=(root.register(validate_number), '%P'), width=5, justify='right')
    y_val.grid(row=4, column=7, padx=0, pady=0, sticky="w") 

    row4.pack()

def BottomRow():
        
    row5 = tk.Frame(root)
    row5.columnconfigure(0, weight=1)
    row5.columnconfigure(1, weight=1)
    
    Hotkey_Button = tk.Button(row5, text="Set Hotkey",command=SetKey)
    Hotkey_Button.grid(row=5,column=0,sticky=tk.W+tk.E)
    
    Minimise = tk.Button(row5, text="Minimal Mode", command=Minimalistic)

    
    Minimise.grid(row=5,column=1, sticky=tk.W+tk.E)
    
    def toggle():
        if Start.config('relief')[-1] == 'raised':
            Start.config(state=DISABLED, relief="sunken")
            Stop.config(state=NORMAL, relief="raised")
        else:
            Start.config(state=NORMAL, relief="raised")
            Stop.config(state=DISABLED, relief="sunken")
    
    
    Start = tk.Button(row5, text="Start (F6)",state=NORMAL, command=toggle)
    Start.grid(row=6,column=0,sticky=tk.W+tk.E)
    
    Stop = tk.Button(row5, text="Stop (F6)", state=DISABLED, command=toggle,relief="sunken")
    Stop.grid(row=6,column=1, sticky=tk.W+tk.E)    
    
    row5.pack(fill="both", pady=20)
    
    



def ClicksPerSecondGUI():
    global CPS_frame

    try:
        Timer_frame.pack_forget()
    except:
        pass

    CPS_frame = tk.Frame(root)
    CPS_frame.columnconfigure(0, weight=1)
    CPS_frame.columnconfigure(1, weight=1)
    
    #Following code ensures that it is numbers being inputted
    def validate(u_input):  # callback function
        return u_input.isdigit()

    my_valid = root.register(validate)  # register 
    
    cps_num = Entry(CPS_frame, validate='key', validatecommand=(my_valid, '%S'), width=10, justify='center')
    cps_num.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
    text = tk.Label(CPS_frame, text='Enter Desired Clicks Per Second')
    text.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    
    CPS_frame.pack(before=row1)

def TimedClicks():
    global Timer_frame
    
    try:
        CPS_frame.pack_forget()
    except:
        pass
    
    Timer_frame = tk.Frame(root)
    for i in range(11):
        Timer_frame.columnconfigure(i, weight=1)
    
    def validate(u_input):  # callback function
        return u_input.isdigit()

    my_valid = root.register(validate)  # register 
    
    hours_val = Entry(Timer_frame, validate='key', validatecommand=(my_valid, '%S'), width=5, justify='center')
    hours_val.grid(row=0, column=0, padx=0, pady=10, sticky="w")    
    hours = tk.Label(Timer_frame, text='hours')
    hours.grid(row=0, column=1, padx=3, pady=0, sticky="w")

    space1 = tk.Label(Timer_frame, text="")
    space1.grid(row=0, column=2, padx=10)
    
    mins_val = Entry(Timer_frame, validate='key', validatecommand=(my_valid, '%S'), width=5, justify='center')
    mins_val.grid(row=0, column=3, padx=0, pady=0, sticky="w")    
    mins = tk.Label(Timer_frame, text='mins')
    mins.grid(row=0, column=4, padx=3, pady=0, sticky="w")

    space2 = tk.Label(Timer_frame, text="")
    space2.grid(row=0, column=5, padx=10)

    secs_val = Entry(Timer_frame, validate='key', validatecommand=(my_valid, '%S'), width=5, justify='center')
    secs_val.grid(row=0, column=6, padx=0, pady=0, sticky="w")    
    secs = tk.Label(Timer_frame, text='secs')
    secs.grid(row=0, column=7, padx=3, pady=0, sticky="w")

    space3 = tk.Label(Timer_frame, text="")
    space3.grid(row=0, column=8, padx=10)

    milliseconds_val = Entry(Timer_frame, validate='key', validatecommand=(my_valid, '%S'), width=5, justify='center')
    milliseconds_val.grid(row=0, column=9, padx=0, pady=0, sticky="w")    
    milliseconds = tk.Label(Timer_frame, text='milliseconds')
    milliseconds.grid(row=0, column=10, padx=3, pady=0, sticky="w")
    
    Timer_frame.pack(before=row1)


def Minimalistic():
    root.geometry("443x95")
    root.minsize(443, 95)
    root.maxsize(443, 95)
    
    for widget in root.winfo_children():
        widget.forget()
    
    row5 = tk.Frame(root)
    row5.columnconfigure(0, weight=1)
    row5.columnconfigure(1, weight=1)
    
    
    Hotkey_Button = tk.Button(row5, text="Set Hotkey", command=SetKey)
    Hotkey_Button.grid(row=5,column=0,sticky=tk.W+tk.E)
    
    def ReturnToNormal():
        row5.forget()
        root.geometry("443x325")
        root.minsize(443, 325)
        root.maxsize(443, 325)
        AlwaysThere()
        TimedClicks()
        BottomRow()
    
    Minimise = tk.Button(row5, text="Normal Mode", command=ReturnToNormal)
    
    
    Minimise.grid(row=5,column=1, sticky=tk.W+tk.E)
    
    def StartnStop():
        if Start.config('relief')[-1] == 'raised':
            Start.config(state=DISABLED, relief="sunken")
            Stop.config(state=NORMAL, relief="raised")
        else:
            Start.config(state=NORMAL, relief="raised")
            Stop.config(state=DISABLED, relief="sunken")
    
    
    Start = tk.Button(row5, text="Start (F6)",state=NORMAL, command=StartnStop)
    Start.grid(row=6,column=0,sticky=tk.W+tk.E)
    
    Stop = tk.Button(row5, text="Stop (F6)", state=DISABLED, command=StartnStop,relief="sunken")
    Stop.grid(row=6,column=1, sticky=tk.W+tk.E)    
    
    row5.pack(fill="both", pady=20)
    
    


AlwaysThere()
TimedClicks()
BottomRow()

root.mainloop()