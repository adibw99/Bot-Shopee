import tkinter as tk

def show_frame(frame):
    frame.tkraise()
    
window = tk.Tk()
window.geometry("600x400")
window.rowconfigure(12, weight=12)
window.columnconfigure(12, weight=12)

frame1 = tk.Frame(window)
frame2 = tk.Frame(window)


for frame in (frame1, frame2):
    frame.grid(row=2,column=0,sticky='nsew')
    
#==================Frame 1 code
frame1_title=  tk.Label(frame1)
frame1_title.pack(fill='both', expand=True)

# TextBox Creation
inputtxt = tk.Text(frame1,
                   height = 2,
                   width = 50)
  
inputtxt.pack()
  
# Button Creation
loginButton = tk.Button(frame1,
                        text = "Login Shopee", 
                        command = lambda:show_frame(frame2))
loginButton.pack()
  

#==================Frame 2 code
frame2_title=  tk.Label(frame2, text='Page 2', font='times 35', bg='yellow')
frame2_title.pack(fill='both', expand=True)


show_frame(frame1)

window.mainloop()