#!/bin/bash

run_cmd="./lxc_with_start.sh Ubuntu 2005 1002 192.168.1.1 192.168.2.16 192.168.1.199 192.168.1.198 192.168.1.199"

for i in {1..24}
do
    echo "Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd; } 2>> single_benchmark_ubuntu
done

run_cmd="./lxc_with_start.sh Alpine 2005 1002 192.168.1.1 192.168.2.16 192.168.1.199 192.168.1.198 192.168.1.199"

for i in {1..50}
do
    echo "Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd; } 2>> single_benchmark_alpine
done

run_cmd="./lxc_with_start.sh Debian 2005 1002 192.168.1.1 192.168.2.16 192.168.1.199 192.168.1.198 192.168.1.199"

for i in {1..50}
do
    echo "Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd; } 2>> single_benchmark_debian
done

run_cmd="./lxc_with_start.sh Fedora 2005 1002 192.168.1.1 192.168.2.16 192.168.1.199 192.168.1.198 192.168.1.199"
for i in {1..50}
do
    echo "Iteration: $i"
    pct stop 2005
    pct destroy 2005
    { time $run_cmd; } 2>> single_benchmark_fedora
done