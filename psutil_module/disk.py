#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import psutil

psutil.disk_usage('/')  # 磁盘使用量
psutil.disk_partitions()  # 磁盘分区情况
psutil.disk_io_counters()  # 磁盘io情况








