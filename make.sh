#########################################################################
# File Name: make.sh
# Author: Qian Yuhui
# Email: yhqian1017@gmail.com
# Created Time: Sat 03 Aug 2019 12:13:58 CST
#########################################################################
#!/bin/bash
make LDFLAGS="-static" LINKFORSHARED=" " -j4
