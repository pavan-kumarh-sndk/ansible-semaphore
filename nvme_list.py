#!/usr/bin/env python3
import subprocess

cmd = 'nvme list'

try:
    p = subprocess.Popen('echo Auto_BGA_1234|sudo -S '+cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = [x.decode("utf-8") for x in p.stdout.readlines()]
    if '/dev/nvme0' in (result[2].split(' ')[0]):
        print('Pass')
    else:
        print('Fail')
except:
    print('Fail')
