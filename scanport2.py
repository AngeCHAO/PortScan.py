import socket
if __name__=='__main__':
    port=3389
    s=socket.socket()
    for cnt in range(253,2,-1):
        address='192.168.0.0' str(cnt)
    try:
        s.connect((address,port))
        print address
        except socket.error,e:
            print 'Error or Port Not Opened'
        