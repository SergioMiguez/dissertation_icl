#!/bin/bash

# Template name
TEMPLATE=Crucial:vztmpl/alpine-3.19-default_20240207_amd64.tar.xz
#  pct create 108 Crucial:vztmpl/alpine-3.19-default_20240207_amd64.tar.xz --rootfs local-zfs:2
# TEMPLATE=105

# Container configurations
declare -a IPS=("192.168.1.108" "192.168.1.109" "192.168.1.110")
# declare -a HOSTNAMES=("108" "CT109" "CT110")
declare -a CT_IDS=("108" "109" "110")  # Change these to your desired container IDs


# Create containers
for i in {0..2}; do
    pct create ${CT_IDS[$i]} $TEMPLATE --rootfs Crucial:2 --arch amd64 --cores 1 --cpulimit 2 --hostname CT${CT_IDS[$i]} --password Aparicio1 --net0 name=eth0,bridge=vmbr0,firewall=1,gw=192.168.1.1,ip=${IPS[$i]}/24,type=veth --unprivileged 1 --ostype alpine --memory 512 --swap 512
 
    pct start ${CT_IDS[$i]}
done