# encoding: utf-8
import os
import datetime
import time

restore_log = open('restore_log.txt','a')
new_dir_path = '/var/lib/rpki-validator' # 处理日志使用
store_path = '/home/rpki/snapshot/store'
blank_dir = '/home/rpki/blank/'
target_path = '/home/rpki/test2'  # 存放整个仓库的目的地址
restore_datetime = '2021-12-24 15:00:00' # 要返回到的时间，先手动输入 格式：yyyy-mm-dd HH:MM:SS
tmp = restore_datetime.split(' ')
restore_date = tmp[0].split('-')[0]+tmp[0].split('-')[1]+tmp[0].split('-')[2] # yyyymmdd 日期
# restore_time = tmp[1] # HH:MM:SS
s2 = tmp[1].split(':')
#print(s2)
restore_time = datetime.time(int(s2[0]),int(s2[1]),int(s2[2])) # 时间
dir_path = store_path+'/'+restore_date # 备份目录
# print(os.path.exists(dir_path))
if os.path.exists(dir_path):
    change_path = dir_path+'/change'
    rsync_path = dir_path+'/rsync'
    log_path = dir_path+'/log.txt'
    if os.path.exists(rsync_path):
        # print('')
        # 使用rsync与一个空目录同步会更快
        if os.path.exists(target_path+'/rsync'):
            # with os.popen('rsync --delete-before -r --force '+blank_dir+' '+target_path) as p:
            #     p.read()
            # p.close()
            print(target_path+'/rsync')
            with os.popen('rm -rf '+target_path+'/rsync') as p:
                p.read()
            p.close()
        # with os.popen('rsync -r '+rsync_path+' '+target_path) as p:
        #     p.read()
        # p.close()
        with os.popen('cp -pr '+rsync_path+' '+target_path) as p:
            p.read()
        p.close()
    else:
        print('There is no rsync dir.Somethine wrong!!')
        # 退出
    # if os.path.exists(change_path):
    #     files = os.listdir(change_path)
    #     print(files)
    # 读当日日志，从文件末尾开始还原

    if os.path.exists(log_path):
        log = open(log_path,'r')
        lines = log.readlines()
        log.close()
        line_number = len(lines)
        # print(line_number)
        sum_cnt = 0
        cnt = 0
        time = ''
        # print(lines[10])
        for i in range(line_number):
            if lines[line_number-i-1].startswith('fff'):
                # info = lines[line_number-i-1].rstrip('\n').split(' ')
                # change_num = info[1].split(':')[1]
                # delete_num = info[2].split(':')[1]
                # add_num = info[3].split(':')[1]
                # time = lines[line_number-i-2].rstrip('\n').split(' ')[0] # 获取当前日志时间
                # tmp_time = datetime.time(int(time.split('-')[0]),int(time.split('-')[1]),int(time.split('-')[2]))
                # sum_cnt = change_num + delete_num + add_num
                continue
            else:
                time1 = lines[line_number-i-1].rstrip('\n').split(' ')[0]
                time_ = datetime.time(int(time1.split(':')[0]),int(time1.split(':')[1]),int(time1.split(':')[2]))
                action = lines[line_number-i-1].rstrip('\n').split(' ')[1]
                filename = lines[line_number-i-1].rstrip('\n').split(' ')[2]
                if time_.__ge__(restore_time):
                    if action=='add': # 删除文件
                        restore_log.write('rm -rf '+filename.replace(new_dir_path,target_path)+'\n')
                        with os.popen('rm -rf '+filename.replace(new_dir_path,target_path)) as p:
                            p.read()
                        p.close()
                    elif action=='delete': # 添加
                        restore_log.write('cp -pr '+change_path+'/'+time1+'/'+real_file+' '+filename.replace(dir_path,target_path)+'\n')
                        real_file = filename.rsplit("/",1)[1]
                        with os.popen('cp -pr '+change_path+'/'+time1+'/'+real_file+' '+filename.replace(dir_path,target_path)) as p:
                            p.read()
                        p.close()
                    elif action=='change': # 先删除，在添加
                        real_file = filename.rsplit("/",1)[1]
                        restore_log.write('rm -rf '+filename.replace(dir_path,target_path)+'\n')
                        restore_log.write('cp -pr '+change_path+'/'+time1+'/'+real_file+' '+filename.replace(dir_path,target_path)+'\n')
                        with os.popen('rm -rf '+filename.replace(dir_path,target_path)) as p:
                            p.read()
                        p.close()
                        with os.popen('cp -pr '+change_path+'/'+time1+'/'+real_file+' '+filename.replace(dir_path,target_path)) as p:
                            p.read()
                        p.close()
                    else:
                        print('log is wrong!!')
                else:
                    restore_log.close()
                    print('finish!')
                    break