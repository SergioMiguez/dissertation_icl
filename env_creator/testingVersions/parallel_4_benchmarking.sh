#!/bin/bash

run_cmd="python3 parallel_4_benchmarking.py"

# for i in {1..1}
for i in {1..50}
do
    echo "(4) Iteration: $i"
    pct stop 2005
    pct destroy 2005
    pct stop 2006
    pct destroy 2006
    pct stop 2007
    pct destroy 2007
    pct stop 2008
    pct destroy 2008
    { time $run_cmd; } 2>> parallel_4_benchmarking.txt
done


