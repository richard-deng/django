# -*- coding: utf-8 -*-
import platform
print platform.uname()
print platform.system()
print platform.release()
print platform.linux_distribution()
print platform._supported_dists
print platform.architecture()

'''print out the /proc/cpuinfo file'''

with open('/proc/cpuinfo') as f:
    for line in f:
        print line.rstrip('n')

with open('/proc/cpuinfo') as f:
    for line in f:
        if line.strip():
            if line.rstrip('n').startswith('model name:'):
                model_name = line.rstrip('n').split(':')[1]
                print model_name

from collections import OrderedDict
def meminfo():
    meminfo = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()
        return meminfo

from collections import namedtuple
def netdevs():
    with open('/proc/net/dev') as f:
        net_dump = f.readlines()
    device_data={}
    data = namedtuple('data',['rx','tx'])
    for line in net_dump[2:]:
        line = line.split(':')
        if line[0].strip() != 'lo':
            device_data[line[0].strip()] = data(float(line[1].split()[0])/(1024.0*1024.0),\
                                                float(line[1].split()[8])/(1024.0*1024.0))
    return device_data

import os
def process_list():
    pids = []
    for subdir in os.listdir('/proc'):
        if subdir.isdigit():
            pids.append(subdir)
    return pids

import glob
import re
dev_pattern = ['sd.*','mmcblk*']
def size(device):
    nr_sectors = open(device+'/size').read().rstrip('n')
    sector_size = open(device+'/queue/hw_sector_size').read().rstrip('n')
    return float(nr_sectors)*float(sector_size)/(1024.0*1024.0*1024.0)

def detect_devs():
    for device in glob.glob('/sys/block/*'):
        for pattern in dev_pattern:
            if re.compile(pattern).match(os.path.basename(device)):
                print 'Device::{0}, Size::{1} GB'.format(device, size(device))

import pwd
def getusers():
    users = pwd.getpwall()
    for user in users:
        print '{0}:{1}'.format(user.pw_name, user.pw_shell)

if __name__ == '__main__':
    meminfo = meminfo()
    print 'Total memory:{0}'.format(meminfo['MemTotal'])
    print 'Free memory:{0}'.format(meminfo['MemFree'])
    netdevs = netdevs()
    for dev in netdevs.keys():
        print '{0}:{1} MB {2} MB'.format(dev, netdevs[dev].rx, netdevs[dev].tx)
    pids = process_list()
    print 'Total num of running process:: {0}'.format(len(pids))
    detect_devs()
    getusers()
