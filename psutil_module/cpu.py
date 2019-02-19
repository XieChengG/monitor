#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import psutil

psutil.cpu_count()  # 逻辑cpu的核数
psutil.cpu_percent()  # cpu的使用率，interval=1, percpu=True 返回间隔一秒的每颗cpu使用率
psutil.cpu_freq()  # cpu的最大、最小、当前的频率
psutil.cpu_stats()  # cpu的状态包括，上下文切换、中断、软中断和系统调用次数
psutil.cpu_times()  # cpu消耗的时间
psutil.cpu_times_percent()  # cpu消耗的时间百分比










