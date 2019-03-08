import socket,ssl,time
def client(url):
    if(url=='localhost' or url=='127.0.0.1'):
        localtime = time.asctime(time.localtime(time.time()))
        print("本地时间为 :", localtime)
        headers='''HTTP/1.1 200 OK
    Accept-Ranges: bytes
    Cache-Control: no-cache
    Content-Type: text/html
    Connection: close
    Server:Localhost
    Date:'''+localtime
        body='''<!DOCTYPE html><!--STATUS OK-->
    <html>
    <head>
    </head>
    <body>
    Localhost
    </body></html>'''
        return headers, body

    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #ipv4 协议，tcp 协议
    # sock = ssl.wrap_socket(socket.socket())
    try:
        sock.connect((url,80)) #http网站
    except:
        headers='error,请检查输入地址的有效性'
        body='NULL'
        return headers, body

    # try:
    #     sock.connect((url,443)) #https网站,sogou,bilibili等
    # except:
    #     headers='error,请检查输入地址的有效性'
    #     body='NULL'
    #     return headers, body

    request_text=b'GET / HTTP/1.1\r\nHost:'+url.encode('utf-8')+b'\r\nConnection: close\r\n\r\n'    #发送请求报文
    sock.sendall(request_text)

    data=[]
    while True:
        more=sock.recv(4096)    #4096byte
        if not more:
            break
        data.append(more)
    sock.close()

    reply=b''.join(data)    #得到的接收报文
    reply =reply.decode('utf-8')
    headers,body=reply.split('\r\n\r\n',1)  #headers和body之间有两个回车换行符间隔，用此特性分离
    return headers,body
