
import socket, time, thread
socket.setdefaulttimeout(3)
def socket_port(ip,port):
    """
    輸入IP和端口,掃描判斷端口是否開放
    """

try:
    if port>=65535:
        print u'端口掃描結束'
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result=s.connect_ex((ip,port))
    if result==0
    lock.acquire()
    print ip,u':',port,u'端口開放'
    lock.release()
    s.close()
    except:
        print u'端口掃描異常'
        def ip_scan(ip):
            """
            輸入IP,掃描IP的0-65534端口情況
            """
try:
    print u'開始掃描 %s' % ip
    start_time=time.time()
    for i in range(0,65534)
    thread.start_new_thread(socket_port,(ip,int(i)))
    print u'掃描端口完成，總共用時 :%.2f' %(time.time()-start_time)
    raw_input("Press Enter to Exit")
    except:
        print u'掃描IP出錯'
        if__name__=='__main__':
        url=raw_input('Input the ip you want to scan:\n')
        lock=thread.allocate_lock()
        ip_scan(url)

