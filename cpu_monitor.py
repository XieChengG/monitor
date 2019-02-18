#!/usr/bin/env python3
from collections import OrderedDict

def cpu_info():
    cpu_info = OrderedDict()
    proc_info = OrderedDict()

    nprocs = 0
    with open("/proc/cpuinfo", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                cpu_info["proc%s" % nprocs] = proc_info
                nprocs = nprocs + 1
                proc_info = OrderedDict()
            else:
                if len(line.split(':')) == 2:
                    proc_info[line.split(':')[0].strip()] = line.split(':')[1].strip()
                else:
                    proc_info[line.split(':')[0].strip()] = ''

    return cpu_info

if __name__ == '__main__':
    cpu_info = cpu_info()
    for processor in cpu_info.keys():
        print(cpu_info[processor]['processor'])

