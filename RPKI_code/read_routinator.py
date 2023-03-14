fp = open('./routinator_2022-05-23_ripencc.txt', 'r')
lines = fp.readlines()
# print(line)
for line in lines:
    if 'Found' in line:
        print(line.split('\n')[0])
    if 'rsync' in line:
        print(line.split('\n')[0])
    if '   ' in line:
        print(line.split('\n')[0])
fp.close()