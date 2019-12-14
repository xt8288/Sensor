#!/usr/bin/python3
import time

import LeCmd

LeCmd.cmd_i001([500, 2, 6, 600, 7, 600])
time.sleep(0.5)
LeCmd.cmd_i001([500, 2, 6, 500, 7, 500])
time.sleep(0.5)
