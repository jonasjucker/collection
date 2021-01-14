import os
import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-d', dest = 'subdir')
args = parser.parse_args() 
subdir = args.subdir

model2 = 'SOCOL-AERv2_demo'
model1 = 'SOCOLv3.1'

dir_1 = os.path.join(model1,subdir)
dir_2 = os.path.join(model2,subdir)

list_1 = os.listdir(dir_1)
list_2 = os.listdir(dir_2)

unique = []
identical = []
different = []

for file_1 in list_1:
    try:
        index  = list_2.index(file_1)
    except ValueError:
        unique.append(file_1)

    file_1_p = os.path.join(dir_1,file_1)
    file_2_p= os.path.join(dir_2,list_2[index])
    cmd = 'diff {} {}'.format(file_1_p, file_2_p)
    p = subprocess.Popen(cmd, shell=True,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    out, err = p.communicate()
    if p.returncode != 0:
        different.append(file_1)
    else:
        identical.append(file_1)

print('')
print('')
print('')
print('unique')
for un in unique:
    print(un)

print('')
print('')
print('')
print('identical')
for id in identical:
    print(id)

print('')
print('')
print('')
print('different')
for dif in different:
    print(dif)

print('')
print('*****')
print('{}/{} files identical'.format(len(identical),(len(identical) + len(different))))
print('*****')
print('')
