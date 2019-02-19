#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import OrderedDict

def meminfo():
    '''
    get memory info from file /proc/meminfo
    :return: ordered dict mem_info
    '''
    mem_info = OrderedDict()
    with open('/proc/meminfo') as f:
        for line in f:
            mem_info[line.split(':')[0]] = line.split(':')[1].strip()
    return mem_info

def main():
    mem_info = meminfo()
    print(mem_info)
    print('Total memory：{}'.format(mem_info['MemTotal']))

if __name__ == '__main__':
    main()










