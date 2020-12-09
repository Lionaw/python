#lionaw
#coding:utf8 

import pickle as p 
import time 

date = time.strftime('%Y%m%d') 

def save_money(): 
    sav_count=int(raw_input('save money: ')) 
    sav_comment = raw_input('doing what: ') 

    with open('wallet.data') as f: 
        balance = p.load(f) 

    new_bal = balance + sav_count 
    with open('wallet.data','w') as f: 
        p.dump(new_bal,f) 

    content = '%-12s%-8s%-8s%-10s%-25s\n'%(date,'N/A',sav_count,new_bal,sav_comment) 
    with open('record.txt','a')as f: 
        f.write(content) 



def spend_money(): 
    spe_count=int(raw_input('spend money: ')) 
    spe_comment = raw_input('doing what: ') 

    with open('wallet.data') as f: 
        balance = p.load(f) 

    new_bal = balance - spe_count 
    with open('wallet.data','w') as f: 
        p.dump(new_bal,f) 

    with open('record.txt','a')as f: 
        content = '%-12s%-8s%-8s%-10s%-25s\n'%(date,spe_count,'N/A',new_bal,spe_comment) 
    f.write(content) 

def query_info(): 
    line = '='*63 
    content = '%s\n%-12s%-8s%-8s%-10s%-25s'%(line,'Date','Cost','Save','Balance','Comment') 

    with open('wallet.data') as f: 
        new_bal = p.load(f) 

    print ('new balance: ',new_bal) 

    print (content) 
    with open('record.txt') as f: 
        for line in f: 
            print (line) 

def show_menu(): 
    prompt = ''''' 
    '0':'spend_money' 
    '1':'save_money' 
    '2':'query_info' 
    '3':'quit' 
''' 
    while True: 
        CMDs={'0':spend_money,'1':save_money,'2':query_info} 
    choice = raw_input('which do you want to do ?%s: '%prompt) 
    while choice not in '012': 
        break 
    CMDs[choice]() 


if __name__=='__main__': 
    show_menu() 