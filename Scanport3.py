import socket
def get_my_ip():
    try:
        csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        csock.connect(('8.8.8.8', 80))
        (addr, port) = csock.getsockname()
        csock.close()
    return addr,port
    except socket.error:
        return "127.0.0.1"
        def int_to_ip(int_ip):
            return socket.inet_ntoa(struct.pack('I', socket.htonl(int_ip)))
            def ip_to_int(ip):
                return socket.ntohl(struct.unpack("I", socket.inet_aton(str(ip)))[0])
                (ip,port)+get_my_ip()
                print "ip=%s port=%d" %(ip,port)
                