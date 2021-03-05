#!/usr/bin/env python
import socket
import os
import sys


HOST = '127.0.0.1'
PORT = 10037

def file_client():
    ''' file Server 的 client 端 '''

    file_in = input('input > ')
    # win系统需要把\\字符进行处理替换
    file_in = file_in.replace("\\", "/")
    #print(file_in)
    # 判断上传文件是否存在
    if not os.path.isfile(file_in):
        print("该文件不存在")
        sys.exit()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    # 获取到文件名
    file_in_dirname = os.path.basename(file_in)
    # filename + 文件名 发送给服务端进行正则匹配处理
    file_in_name ="filename" + file_in_dirname.strip()
    # 发送文件名
    s.sendall(file_in_name.encode())
    # 传输文件
    with open(file_in, "rb") as f:
            datas = f.read()
            s.sendall(datas)
    f.close()
    s.close()


if __name__ == '__main__':
    file_client()