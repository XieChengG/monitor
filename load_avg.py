#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
def load_stat():
    load_avg = {}
    f = open('/proc/loadavg')
    load_info = f.read().split()
    f.close()
    load_avg['lavg1'] = load_info[0]
    load_avg['lavg10'] = load_info[1]
    load_avg['lavg15'] = load_info[2]
    return load_avg

if __name__ == '__main__':
    load_stat = load_stat()
    print('------------system loadavg---------')
    print('1min: {}\n10min: {}\n15min: {}'.format(
        load_stat['lavg1'],
        load_stat['lavg10'],
        load_stat['lavg15']
    ))


