#!/bin/bash

run_cmd="python3 parallel_1_benchmarking.py "
distro="Ubuntu"

# for i in {1..1}
for i in {1..50}
do
    echo "(1) Ubuntu Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd$distro; } 2>> parallel_1_benchmarking_ubuntu.txt
done

run_cmd="python3 parallel_1_benchmarking.py "
distro="Alpine"

# for i in {1..1}
for i in {1..50}
do
    echo "(1) Alpine Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd$distro; } 2>> parallel_1_benchmarking_alpine.txt
done

run_cmd="python3 parallel_1_benchmarking.py "
distro="Debian"

# for i in {1..1}
for i in {1..50}
do
    echo "(1) Debian Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd$distro; } 2>> parallel_1_benchmarking_debian.txt
done

run_cmd="python3 parallel_1_benchmarking.py "
distro="Fedora"

# for i in {1..1}
for i in {1..50}
do
    echo "(1) Fedora Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd$distro; } 2>> parallel_1_benchmarking_fedora.txt
done

