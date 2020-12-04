#!/usr/bin/env python
import socket
import re
import sys

HOST = '127.0.0.1'
PORT = 10037

def file_server():
    ''' file Server 的 Server 端 '''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 对象s绑定到指定的主机和端口上
    s.bind((HOST, PORT))
    # 只接受1个连接
    s.listen(1)
    while True:
        # accept表示接受用户端的连接
        conn, addr = s.accept()
        # 输出客户端地址
        print(f'Connected by {addr}')
        file = conn.recv(1024)
        # 接收到字符转码
        file = file.decode()
        # 正则匹配接收文件名 格式filename+文件名
        file_re = re.compile("filename+")
        # 正则匹配到filename+文件名 就替换掉filename为空，否则就结束进程
        if file_re.search(file):
            filepath = str(file).replace("filename", "")
        else:
            sys.exit()

        print(f"正在传输文件{filepath}!!!")
        # 接收到文件写入文件
        with open("new"+filepath, "wb") as f:
            while True:
                data = conn.recv(8196)
                if not data:
                    break
                f.write(data)
        f.close()
        print(f"传输文件{filepath}已完成!!!")
        conn.close()
    #s.close()


if __name__ == '__main__':
    file_server()
