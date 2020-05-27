#!/usr/bin/env python2

"""
Parse the output of `df` and return a json object of metrics for each disk used percentage.
Tested on CentOS which outputs following `df` format.

Filesystem                                       1K-blocks      Used   Available Use% Mounted on
devtmpfs                                          29288352         0    29288352   0% /dev
tmpfs                                             29300620     12904    29287716   1% /run
/dev/vda3                                        387570688 251326000   125728496  67% /
/dev/vda1                                           474712    107427      338255  25% /boot
"""

import subprocess
import sys
import json


# json data
data = []
# metric header
NAME = "disk.used_percent:{}"

df = subprocess.Popen(["df"], stdout=subprocess.PIPE)

# skip parse the first header line
df.stdout.readline()
for x in df.stdout:
    device, size, used, available, percent, mountpoint = x.split()
    # /dev/vda1 --> dev_vda1
    metric = {
        "name": NAME.format("_".join(mountpoint.split("/")[1:])),
        "value": percent[:-1],
    }
    data.append(metric)

print(json.dumps(data))

sys.exit(0)

## Outdated
output = df.communicate()[0]
for x in output.split("\n")[1:]:
    print(x)
    device, size, used, available, percent, mountpoint = x.split()
    print(device, size, used, available, percent, mountpoint)
