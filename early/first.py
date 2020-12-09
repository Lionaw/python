#!/usr/bin/env python
#coding:utf8

import os,sys
import time
'''
1.运行该脚本会生成一个balance.txt文件，并设置初始账户余额：￥10000
2.运行该脚本会生成一个account.txt文件，并记录账户消费信息详情。
'''

def save():
    date = time.strftime("%Y-%m-%d")
    cost = 0

    while 1:
        try:
            save = int(raw_input("请输入存款金额: ").strip())
        except ValueError:
            print "\033[31m请输入数值类型，重新输入！\033[0m"
            continue
        except (KeyboardInterrupt,EOFError):
            sys.exit("\n\033[31m程序退出\033[0m")

        if save <= 0:
            print "\033[31m请输入一个大于0的存款金额：\033[0m"
            continue


        while 1:
            try:
                comment = str(raw_input("请输入存款信息: "))
            except (KeyboardInterrupt,EOFError):
                sys.exit("\n\033[31m程序退出\033[0m")
            if not comment:
                continue
            break
        break
    balance = rekcon_balance(save,cost)
    a.write('%-12s%-12s%-12s%-12s%-12s\n' %(date, cost, save, balance, comment))
    a.flush()
    with open('balance.txt', 'w') as b:
        balance = str(balance)
        b.write(balance)

def cost():
    save = 0
    date = time.strftime("%Y-%m-%d")
    while 1:
        try:
            cost = int(raw_input("请输入消费金额: ").strip())
        except ValueError:
            print "\033[31m请输入数值类型，重新输入!!!\033[0m"
            continue
        except (KeyboardInterrupt,EOFError):
            sys.exit("\n\033[31m程序退出\033[0m")

        if cost <= 0:
            print "\033[31m请输入一个大于0的消费金额：\033[0m"
            continue
        break

    balance = rekcon_balance(save,cost)
    while balance == -1:
        print "\033[31m余额不足，请充值或进行其他操作!!!\033[0m"
        break
    else:
        while 1:
            try:
                comment = str(raw_input("请输入消费信息: "))
            except (KeyboardInterrupt,EOFError):
                sys.exit("\n\033[31m程序退出\033[0m")
            if not comment:
                continue
            break
        a.write('%-12s%-12s%-12s%-12s%-12s\n' %(date, cost, save, balance, comment))
        with open('balance.txt', 'w') as b:
            balance = str(balance)
            b.write(balance)
    a.flush()


def rekcon_balance(save,cost):
    try:
        with open('balance.txt', 'r') as b:
            balance = b.readline()
            balance = int(balance)
    except IOError:
        balance = 10000

    balance += save
    if cost > balance:
        balance = -1
        return balance

    balance -= cost

    # with open('balance.txt', 'w') as f:
    #     balance = str(balance)
    #     f.write(balance)
    return balance

def balance():
    try:
        with open('balance.txt', 'r') as b:
            balance = b.readline()
    except IOError,e:
        balance = 10000
        print "\033[31m初始账户余额:\033[0m￥%s" % balance
    else:
        print "\033[31m当前账户余额:\033[0m￥%s" % balance


def view():
    print '账户金额详细信息'.center(78,'*')
    print "%-12s%-12s%-12s%-12s%-12s\n" %('Date', 'Cost', 'Save', 'Balance', 'Comment'),
    with open('account.txt','r') as b:
        for line in b.readlines():
            print line,
    print '*'.center(70,'*')
def show_menu():
    cmds = {
    '0': save, '1': cost, '2': balance, '3': view, '4': quit
    }
    prompt = """\033[32m-----------------------------
(0): save money
(1): cost money
(2): balance 
(3): view detail
(4): quit
-----------------------------\033[0m
Please Input Your Choice: """
    while 1:
        try:
            choice = raw_input(prompt).strip()[0]
        except (KeyboardInterrupt,EOFError):
            sys.exit("\n\033[31m程序退出\033[0m")
        except IndexError:
            print "\033[31m无效输入，请重新输入!!!\033[0m"
            continue

        if choice not in '01234':
            print "\033[31m无效输入，请重新输入!!!\033[0m"
            continue

        if choice == 4:
            break

        cmds[choice]()


if __name__ == '__main__':
    a = open('account.txt','a')
    print show_menu()
    a.close()