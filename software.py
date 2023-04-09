import tkinter as tk
  
def show_frame(frame):
    frame.tkraise()

root = tk.Tk()

# Top level window
# root.rowconfigure(0,weight=1)
# root.columnconfigure(0,weight=1)
frame1 = tk.Frame(root, bg='gold')
# frame1.grid(row=12,column=12,sticky='nsew')
frame2 = tk.Frame(root, bg='green')

root.title("Bot Shopee")
root.geometry('600x400')
# Function for getting Input
# from textbox and printing it 
# at label widget


  
def loginSuccess():
    root.title("Bot Shopee")
    root.geometry('600x400')
  
# TextBox Creation
inputtxt = tk.Text(root,
                   height = 2,
                   width = 50)
  
inputtxt.pack()
  
# Button Creation
loginButton = tk.Button(root,
                        text = "Login Shopee", 
                        command = loginSuccess())
loginButton.pack()
  
# Label Creation
lbl = tk.Label(root, text = "")
lbl.pack()
root.mainloop()

