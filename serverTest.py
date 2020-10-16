# Reminder: This is a comment. The first line imports a default library "socket" into Python.
# You don’t install this. The second line is initialization to add TCP/IP protocol to the endpoint.
import socket
import cv2

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Assigns a port for the server that listens to clients connecting to this port.
host = socket.gethostname()
print(host)
serv.bind((host, 1234))
serv.listen(5)

while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print(from_client)
        conn.send("I am SERVER\n")
        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    conn.close()
    print('client disconnected')