#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from collections import namedtuple

Disk = namedtuple('Disk', 'major_number minor_number device_number'
                  'read_count read_merged_count read_sections'
                  'time_spend_reading write_count write_merged_count'
                  'write_sections time_spent_write io_request'
                  'time_spend_doing_io weighted_time_spend_doing_io')

def get_disk_info(device):
    with open('/proc/diskstats') as f:
        for line in f:
            if line.split()[2] == device:
                return Disk(*(line.split()))
    raise RuntimeError('device {} not found !'.format(device))

def main():
    disk_info = get_disk_info('vdc')
    print(disk_info)
    print('磁盘写次数：{}'.format(disk_info.write_count))
    print('磁盘写字节数:{}'.format(long(disk_info.write_sections) * 512))
    print('磁盘写延时：{}'.format(disk_info.time_spent_write))

if __name__ == '__main__':
    main()
