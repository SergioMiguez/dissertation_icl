#!/bin/bash

run_cmd="python3 switchconf/switchconf.py --config "
file1="join_prox_attacker.yaml"
raw="raw.yaml"

cd ..

for i in {1..10}
do
    echo "Benchmark $i"
    echo $file1
    { time $run_cmd$file1; } 2>> benchmarks/join_prox_attacker_benchmark.txt
    echo $raw
    { time $run_cmd$raw; } 2>> benchmarks/raw_benchmark.txt
done