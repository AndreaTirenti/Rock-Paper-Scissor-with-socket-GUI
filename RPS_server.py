from tkinter import *
from tkinter import messagebox
from socket import *
from threading import Thread
from PIL import Image

server_move = ""
client_move = ""

def check_win(client_move, server_move):
    print("controllo chi ha vinto")
    global conn
    if client_move == server_move:
        print("mando i risultati al client")
        send_move(server_move)
        if client_move == "rock":
            rock1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock1.png")      
            canvas.create_image(20,0, anchor=NW, image=rock1)
        
            rock2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock2.png")
            canvas.create_image(300,10, anchor=NW, image=rock2)
        elif client_move == "paper":
            paper1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper1.png")      
            canvas.create_image(20,0, anchor=NW, image=paper1)
        
            paper2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper2.png")
            canvas.create_image(300,10, anchor=NW, image=paper2)
        elif client_move == "scissor":
            scissor1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors1.png")      
            canvas.create_image(20,0, anchor=NW, image=scissor1)
            
            scissor2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors2.png")
            canvas.create_image(300,10, anchor=NW, image=scissor2)
        
        messagebox.showinfo(title = "OPS",message = "IT'S A TIE")
        window.destroy()
    
    elif client_move == "rock" and server_move == "paper":
        print("mando i risultati al client")
        send_move(server_move)
        paper1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper1.png")      
        canvas.create_image(20,0, anchor=NW, image=paper1)
        
        rock2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock2.png")
        canvas.create_image(300,10, anchor=NW, image=rock2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "SERVER WON")
        window.destroy()
        
    elif client_move == "rock" and server_move == "scissor":
        print("mando i risultati al client")
        send_move(server_move)
        scissor1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors1.png")      
        canvas.create_image(20,0, anchor=NW, image=scissor1)
        
        rock2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock2.png")
        canvas.create_image(300,10, anchor=NW, image=rock2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "CLIENT WON")
        window.destroy()
                
    elif client_move == "paper" and server_move == "rock":
        print("mando i risultati al client")
        send_move(server_move)
        rock1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock1.png")      
        canvas.create_image(20,0, anchor=NW, image=rock1)
        
        paper2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper2.png")
        canvas.create_image(300,10, anchor=NW, image=paper2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "CLIENT WON")
        window.destroy()
    
    elif client_move == "paper" and server_move == "scissor":
        print("mando i risultati al client")
        send_move(server_move)
        scissor1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors1.png")      
        canvas.create_image(20,0, anchor=NW, image=scissor1)
        
        paper2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper2.png")
        canvas.create_image(300,10, anchor=NW, image=paper2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "SERVER WON")
        window.destroy()
        
    elif client_move == "scissor" and server_move == "rock":
        print("mando i risultati al client")
        send_move(server_move)
        rock1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/rock1.png")      
        canvas.create_image(20,0, anchor=NW, image=rock1)
        
        scissor2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors2.png")
        canvas.create_image(300,10, anchor=NW, image=scissor2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "SERVER WON")
        window.destroy()

    elif client_move == "scissor" and server_move == "paper":
        print("mando i risultati al client")
        send_move(server_move)
        paper1 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/paper1.png")      
        canvas.create_image(20,0, anchor=NW, image=paper1)
        
        scissor2 = PhotoImage(file="socket/RockPaperScissor_GUI/assets/scissors2.png")
        canvas.create_image(300,10, anchor=NW, image=scissor2)
        
        messagebox.showinfo(title = "CONGRATULATIONS",message = "CLIENT WON")
        window.destroy()
    else:
        return None




def rock():
    global server_move
    global client_move
    server_move = "rock"
    check_win(client_move.decode(), server_move)

def paper():
    global server_move
    global client_move
    server_move = "paper"
    check_win(client_move.decode(), server_move)

def scissor():
    global server_move
    global client_move
    server_move = "scissor"
    check_win(client_move.decode(), server_move)
    
def send_move(move):
    move = str(move)
    move = move.encode() 
    conn.send(move)



window = Tk()

window.title("Server: Rock Paper Scissor")
window.geometry("450x450")
window.resizable(False, False)
window.config(bg = "green")

bt1 = Button(window, text = "Rock", bg = "red", width = 9, fg = "yellow", height = 2, font = ('Helvetica','20'), command = rock)
bt1.grid(row = 0, column = 0)

bt2 = Button(window, text = "Paper", bg = "yellow", fg = "blue", width = 9, height = 2, font = ('Helvetica','20'), command = paper)
bt2.grid(row = 0, column = 1)

bt3 = Button(window, text = "Scissor", bg = "blue", fg = "red", width = 9, height = 2, font = ('Helvetica','20'), command = scissor)
bt3.grid(row = 0, column = 2)



canvas = Canvas(window, width = 450, height = 150, bg = "green")      
canvas.place(rely= 0.35) 



my_sock = socket(AF_INET,SOCK_STREAM)


my_sock.bind(('127.0.0.1', 5001))
my_sock.listen(1)
conn=None

def handle_client():
    global conn
    conn,addr = my_sock.accept()
    receive = Thread(target = receive_message, args = [conn,])
    receive.start()
    
def receive_message(c):
    global client_move
    while True:
        client_move = conn.recv(32)
        print("ho ricevuto la mossa dal client")



acc = Thread(target=handle_client)
acc.start()


window.mainloop()