# encoding: utf-8
import os
import datetime
import time
import re

# old_dir_path 之前文件夹所在绝对路径
# new_dir_path 之后文件夹所在绝对路径
# diff_dir 绝对路径
def first_make_md5(old_dir_path,new_dir_path,diff_dir):
    order1 = 'find ./rsync -type f -exec md5sum {} \; | sort -k 2  >' +diff_dir+'/old_dir.txt' # 命令里的rsync可以改，按实际的来；但两个都要相同
    order2 = 'find ./rsync -type f -exec md5sum {} \; | sort -k 2  >' +diff_dir+'/new_dir.txt'
    os.chdir(old_dir_path)
    with os.popen(order1) as p:
        p.read()
    p.close()
    os.chdir(new_dir_path)
    with os.popen(order2) as p:
        p.read()
    p.close()

def make_md5(new_dir_path,diff_dir):
    order = 'find ./rsync -type f -exec md5sum {} \; | sort -k 2  >' +diff_dir+'/new_dir.txt'
    os.chdir(new_dir_path)
    with os.popen(order) as p:
        p.read()
    p.close()

# diff_dir 采用绝对路径
def diff_md5(diff_dir):
    # filename = datetime.datetime.now().strftime('%Y%m%d_%H%M') + '.txt'
    os.chdir(diff_dir)
    order = 'diff old_dir.txt new_dir.txt > diff.txt'
    # order = 'diff -r '+src_path+' '+dst_path+' | grep roa'
    # print(order)
    with os.popen(order) as p:
        p.read()
    p.close()

def file_diff(old_dir_path,new_dir_path,diff_dir):
    order = 'diff -qr '+old_dir_path+'/rsync/ '+new_dir_path+'/rsync/ > '+diff_dir+'/diff.txt'
    with os.popen(order) as p:
        p.read()
    p.close()


def log_diff(old_dir_path,new_dir_path,diff_dir,change_dir,log_path,change_time):
    file_path = diff_dir+'/diff.txt'
    # log_path = log_dir+'/log.txt'
    f = open(file_path, 'r')
    lines = f.readlines()
    f.close()
    #cnt = 0
    # change_time = time.time()
    log = open(log_path,'a')
    os.chdir(change_dir)
    with os.popen('mkdir '+str(change_time)) as p:
        p.read()
    p.close()
    change_num = 0
    add_num = 0
    delete_num = 0
    for line in lines:
        if line.startswith('Files'): # 改变，备份原来的，添加新的
            tmp_path1 = line.rstrip('\n').split(' ')[1] # 老的文件路径
            tmp_path2 = line.rstrip('\n').split(' ')[3] # 新的文件路径
            with os.popen('cp -pr '+tmp_path1+' '+change_dir+'/'+str(change_time)) as p:
                p.read()
            p.close()
            with os.popen('rm -rf '+tmp_path1) as p:
                p.read()
            p.close()
            with os.popen('cp -pr '+tmp_path2+' '+tmp_path1) as p:
                p.read()
            p.close()
            log.write(str(change_time)+' '+'change'+' '+tmp_path1+'\n')
            change_num += 1
        else:
            infos = line.rstrip('\n').split(' ')
            if old_dir_path in line: # 只在旧文件夹出现，删除;在change中备份，删除原来的文件
                log.write(str(change_time)+' '+'delete'+' '+infos[2].rstrip(':')+'/'+infos[3]+'\n')
                with os.popen('cp -pr '+infos[2].rstrip(':')+'/'+infos[3]+' '+change_dir+'/'+str(change_time)) as p:
                    p.read()
                p.close()
                with os.popen('rm -rf '+infos[2].rstrip(':')+'/'+infos[3]) as p:
                    p.read()
                p.close()
                delete_num += 1
            elif new_dir_path in line: # 只在新的文件夹出现，增加；在原文件夹中直接添加
                log.write(str(change_time)+' '+'add'+' '+infos[2].rstrip(':')+'/'+infos[3]+'\n')
                with os.popen('cp -pr '+infos[2].rstrip(':')+'/'+infos[3]+' '+infos[2].rstrip(':').replace(new_dir_path,old_dir_path)+'/'+infos[3]) as p:
                    p.read()
                p.close()
                add_num += 1
        #cnt += 1
    #log.write('number:'+str(cnt)+'\n')
    log.write('fff change:'+str(change_num)+' delete:'+str(delete_num)+' add:'+str(add_num)+'\n')
    log.close()

# return old_line 表示读到了第几行
# return time_list 因为日志会打印好几条'the xxx .... '，但是都是同一次改变的，读的时候可能两次分开了，为了记录这一点。发现重复只记录，不再执行
def read_syslog(old_line,old_time_list): # return old_line
    time_list = [] # 记录发现本次发现更改的时间，不是执行任务
    mission_list = [] # 记录发现更改的时间，上次出现过（执行过的）就不再被添加；用来执行
    cnt = 0
    print('old_line is '+str(old_line))
    r=os.popen('wc -l '+syslog_path)
    number = int(r.read().split(' ')[0])
    # print(number)
    r.close()
    print(number)
    if number < old_line: #到每天6.25左右会将syslog变为syslog.1
        r = os.popen('tail -n +'+str(old_line+1)+' '+syslog1_path)
        lines = r.readlines()
        r.close()
        print('log start :'+str(old_line))
        if len(lines)==0:
            return 1,old_time_list,mission_list
        for line in lines:
            cnt += 1
            if re.search(pattern_1,line) is None and re.search(pattern_2,line) is None: # 没有匹配到，直接忽略
                continue
            else: # 匹配到了，提取时间信息；并建立一个list
                #c_date  = line.split(' ')[5] # 日期 yyyy-mm-dd
                c_time = line.split(' ')[2] # 时间 HH:MM:SS
                #c_time = line.split(' ')[5] + ' ' + line.split(' ')[2]
                if c_time not in old_time_list: # 未添加过快照
                    if c_time not in time_list: # 避免重复
                        time_list.append(c_time)
                    if c_time not in mission_list: # 避免重复
                        mission_list.append(c_time)
                else: # 添加过快照的只进行记录，方便下一次区分
                    if c_time not in time_list:
                        time_list.append(c_time)
        print('anaylse '+str(cnt)+' logs!')
        return 1,time_list,mission_list # old_line变为1，从新的syslog开始
    else: # 还是syslog
        r = os.popen('tail -n +'+str(old_line+1)+' '+syslog_path)
        lines = r.readlines()
        r.close()
        if len(lines)==0:
            return old_line,old_time_list,mission_list
        for line in lines:
            cnt += 1
            if re.search(pattern_1,line) is None and re.search(pattern_2,line) is None: # 没有匹配到，直接忽略
                continue
            else: # 匹配到了，提取时间信息；并建立一个list
                #c_date  = line.split(' ')[5] # 日期 yyyy-mm-dd
                c_time = line.split(' ')[2] # 时间 HH:MM:SS
                #c_time = line.split(' ')[5] + ' ' + line.split(' ')[2]
                if c_time not in old_time_list: # 未添加过快照
                    if c_time not in time_list: # 避免重复
                        time_list.append(c_time)
                    if c_time not in mission_list: # 避免重复
                        mission_list.append(c_time)
                else: # 添加过快照的只进行记录，方便下一次区分
                    if c_time not in time_list:
                        time_list.append(c_time)
        print('anaylse '+str(cnt)+' logs!')
        return old_line+cnt,time_list,mission_list
# 标志符
init_flag = 0 # 0表示未初始化；用来记录每天更换目录的初始化
# is_changed = 0 # 用来记录今日的备份是否进行过一次更新；0表示否；此处决定first_make_md5还是make_md5

# 文件目录 参数
new_dir_path = '/var/lib/rpki-validator' # 最新的repo目录，一般为validator下的rsync目录，固定不变
diff_dir = '/home/rpki/snapshot/diff'   # 用来存放差异文件的目录，一般不变
stores = '/home/rpki/snapshot/store'  #备份总目录，不变

old_dir_path = '' # 每日定期备份的目录
day_log_path = '' # 每日日志目录 log
day_change_path ='' # 存储每天变化的总目录路径，下面会按照更新的时间有小的文件夹 change
day_store_path = '' # 备份 rsync
# ---old_dir_path
#        |--day_store (例如：20211213) # 一天建立一个文件夹
#               |-----log.txt # 日志
#               |-----rsync  #同步
#               |-----change # 增量存储
#                         |----change_store # 一个改变时间点建立一个文件夹，存放变化的文件

# 系统日志增量分析 参数
global syslog_path
syslog_path= '/var/log/syslog' # 系统日志位置
global syslog1_path
syslog1_path = '/var/log/syslog.1'
global pattern_1
pattern_1= r'The following trust anchor was affected' # 模式串1
# pattern_1 = r'Stored'
global pattern_2
pattern_2= r'Re-validating the CA tree for TA'# 模式串2
r=os.popen('wc -l '+syslog_path)
number = int(r.read().split(' ')[0])
r.close()
old_line = number-20 # 上一次日志读到的行数
# old_line = 8888
time_list = [] # 上一次
mission_list = [] # 快照任务

# 定期同步整天
old_day =  datetime.datetime.now().strftime('%Y%m%d')

##################
while(True):
    #初始化,仅刚开始运行一次
    if init_flag == 0:
        old_dir_path = stores+'/'+old_day
        day_log_path = old_dir_path+'/log.txt'
        day_store_path = old_dir_path+'/rsync'
        day_change_path = old_dir_path+'/change'
        if os.path.exists(old_dir_path):
            init_flag = 1
            continue
        os.popen('mkdir '+old_dir_path) # 可以加一下判断
        os.popen('mkdir '+day_store_path)
        os.popen('mkdir '+day_change_path)
        with os.popen('cp -pr '+new_dir_path+'/rsync '+old_dir_path,'r') as p: # 通过cp备份
            p.read()
        p.close()
        print('init finished!!')
        init_flag = 1
    # 变天
    now_day = datetime.datetime.now().strftime('%Y%m%d')
    if now_day != old_day:
        old_day = now_day
        old_dir_path = stores+'/'+old_day
        day_log_path = old_dir_path+'/log.txt'
        day_store_path = old_dir_path+'/rsync'
        day_change_path = old_dir_path+'/change'
        os.popen('mkdir '+old_dir_path)
        os.popen('mkdir '+day_store_path)
        os.popen('mkdir '+day_change_path)
        with os.popen('cp -pr '+new_dir_path+'/rsync '+old_dir_path) as p: # 通过cp备份
            p.read()
        p.close()
        # is_changed = 0 # 今日未进行改变
        print('change to day:',now_day)
    old_line,time_list,mission_list = read_syslog(old_line,time_list)
    if len(mission_list)!=0: # 有任务
        print('find missions!!')
        print(mission_list)
        begin = time.time()
        last_mission = 'no'
        for mission in mission_list: # 一般情况下都是1个
            if last_mission == 'no':
                print('')
                last_mission = mission
            else:
                last_mission_time = datetime.datetime.strptime('2000-01-01 '+last_mission,'%Y-%m-%d %H:%M:%S')
                this_mission_time = datetime.datetime.strptime('2000-01-01 '+mission,'%Y-%m-%d %H:%M:%S')
                seconds = (this_mission_time-last_mission_time).seconds
                if seconds < 300:
                    continue
                else:
                    last_mission = mission
            print('mission begin')
            begin1 = time.time()
            file_diff(old_dir_path,new_dir_path,diff_dir)
            end1 = time.time()
            print('file_diff finish:',end1-begin1)
            begin1 = time.time()
            log_diff(old_dir_path,new_dir_path,diff_dir,day_change_path,day_log_path,mission)
            end1 = time.time()
            print('log_diff finish:',end1-begin1)
            print('finish a mission!!!')
        end = time.time()
        print('spend time:',end-begin)
    else:
        print('no missions!!!')
        time.sleep(60)