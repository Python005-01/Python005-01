#!/usr/bin/env python3.7
## -*- coding: utf-8 -*-
import os
import logging
import time

def logsfile():

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    file_path = "/var/log/python-" + time.strftime('%Y%m%d', time.localtime(time.time())) + "/"
    file_path_log = file_path + "access.log"
    logformat = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    if os.access("/var/log", os.W_OK):
        if not os.path.isdir(file_path):
            os.makedirs(file_path)
        fileout = logging.FileHandler(file_path_log, mode = 'a')
        fileout.setLevel(logging.INFO)
        fileout.setFormatter(logformat)
        logger.addHandler(fileout)
        logger.debug('这是debug')
        logger.info('这是info')
        logger.warning('这是warning')
        logger.error('这是error')
        logger.critical('这是critical')
    else:
        conout = logging.StreamHandler()
        conout.setLevel(logging.WARNING)
        conout.setFormatter(logformat)
        logger.addHandler(conout)
        logger.error('目录没有写权限')

if __name__ == '__main__':
    logsfile()