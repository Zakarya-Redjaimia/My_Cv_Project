import socket
from pywebio.input import input
from pywebio.output import put_buttons , put_text, put_html
from pywebio import start_server

def send_commands(msg):
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as zakarya_socket :
        zakarya_socket.connect(('localhost',12345))
        zakarya_socket.sendall(msg.encode('utf-8'))

def main():
    put_html("<h1 style='text-align:center;'>Cyber Security Learn</h1>")
    command = input('Write Commands : ',type='text')
    def send_command(e):
        send_commands(command)
        put_text(f"Sended : {command}")
    put_buttons(['send'],onclick=send_command)

if __name__ == '__main__':
    start_server(main ,port=8080)