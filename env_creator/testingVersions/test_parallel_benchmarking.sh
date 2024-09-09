#!/bin/bash

# ./parallel_1_benchmarking.sh
./parallel_2_benchmarking.sh
./parallel_3_benchmarking.sh
./parallel_4_benchmarking.sh


pct stop 2005
pct destroy 2005
pct stop 2006
pct destroy 2006
pct stop 2007
pct destroy 2007
pct stop 2008
pct destroy 2008

python3 times_lxc_benchmarks.py 
