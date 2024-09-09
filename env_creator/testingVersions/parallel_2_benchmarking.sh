#!/bin/bash

run_cmd="python3 parallel_2_benchmarking.py"

# for i in {1..1}
for i in {1..19}
do
    echo "(2) Iteration: $i"
    pct stop 2005
    pct destroy 2005
    pct stop 2006
    pct destroy 2006
    { time $run_cmd; } 2>> parallel_2_benchmarking.txt
done


