from socket import *

def main():
    ip_add = "192.168.1.3"
    port = 80
    print("[+] honeypot start ..... ")
    try:
        get_socket_con = socket(AF_INET,SOCK_STREAM)
        get_socket_con.bind((ip_add,port))
        get_socket_con.listen(10)
        while 1:
            client_con,client_addr = get_socket_con.accept()
            print("Visister found ! - [{}]".format(client_addr[0]))
            client_con.send(b"<h1> you Have been hacked ! </h1>")
            date =client_con.recv(2048)
            print(data)
    except error as identifier:
        print("[+] unspecified  error [{}]".format(indentifier))
    except KeyboardInterrupt:
        print("[-] process stoped ! ")
    finally:
        get_socket_con.close()
    get_socket_con.close()


if __name__ == "__main__":
    main()