#!/usr/bin/python3
#-*- coding:utf-8 -*-

import argparse
import datetime
import os

LINUX_RED_COLOR = '\x1b[41m'
LINUX_GREEN_COLOR = '\x1b[42m'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--list', help='列出所有的todo list', action='store_true')
    parser.add_argument('-a', '--add', help='添加一条todo list')
    parser.add_argument('-f', '--finish', type=int, help='输入序号,完成一项todo')
    args = parser.parse_args()
    if args.add:
        add_todo(args.add)
    elif args.list:
        list_todo()
    elif args.finish:
        finish_todo(args.finish)

def add_todo(todo):
    today = datetime.date.today()
    with open(str(today) + '.txt', 'a+') as txt:
        txt.write(todo + 'TODO' + os.linesep)

def list_todo():
    today = datetime.date.today()
    num = 0
    try:
        with open(str(today)+'.txt','r') as txt:
            while True:
                line = txt.readline()
                if not line:
                    break
                num += 1
                if os.name == 'posix':
                    index = line.find('TODO')
                    if index != -1:
                        print(str(num) + '.' + LINUX_RED_COLOR + 'TODO' + '\x1b[0m '+line[0:index])
                    else:
                        print(str(num) + '.' + LINUX_GREEN_COLOR + 'FINISH' + '\x1b[0m '+line[0:index])
                elif os.name == 'nt':
                    index = line.find('TODO')
                    if index != -1:
                        print(str(num) + '. TODO' + line[0:index])
                    else:
                        print(str(num) + '. FINISH' + line[0:index])
                else:
                    pass
    except FileNotFoundError as err:
        print(err)

def finish_todo(num):
    today = datetime.date.today()
    lines_new = []
    with open(str(today)+'.txt','r') as txt:
        lines = txt.readlines()
        
        line_num = 0
        for line in lines:
            line_num += 1
            if line_num == num:
                line_new = line.replace('TODO','')
                lines_new.append(line_new)
            else:
                lines_new.append(line)
        
    with open(str(today)+'.txt','w') as txt:
        txt.writelines(lines_new)

if __name__ == '__main__':
    main()