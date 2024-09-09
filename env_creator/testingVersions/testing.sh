#!/bin/bash

clean_cmd="./clean.sh"

run_cmd="python3 testingVersions/db_script_raw.py 2"

for i in {1..10}
do
    $clean_cmd > /dev/null
    { time $run_cmd; } 2>> raw_benchmark
done

run_cmd="python3 testingVersions/db_script_p_start.py 2"

for i in {1..8}
do
    $clean_cmd > /dev/null
    { time $run_cmd; } 2>> p_start_benchmark
done

run_cmd="python3 testingVersions/db_script_p_clone_start.py 2"

for i in {1..10}
do
    $clean_cmd > /dev/null
    { time $run_cmd; } 2>> p_clone_start_benchmark
done

