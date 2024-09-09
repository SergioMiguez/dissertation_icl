#!/bin/bash
# This script creates the LXCs and configures them, but does not start them

# ./launch_lxcs.sh Alpine 111 1001 192.168.1.1 192.168.2.11 192.168.1.202 192.168.1.203 192.168.1.204 192.168.1.205 192.168.1.206
# The first ADDITIONAL_IP is used to set the SDN IP

# ./launch_lxcs.sh Ubuntu 112 1002 192.168.1.1 192.168.2.12 192.168.1.207 192.168.1.208 192.168.1.209 192.168.1.210 192.168.1.211

# ./launch_lxcs.sh Debian 113 1003 192.168.1.1 192.168.2.13 192.168.1.212 192.168.1.213 192.168.1.214

# ./launch_lxcs.sh Fedora 114 1004 192.168.1.1 192.168.2.14 192.168.1.215 192.168.1.216 192.168.1.217


DISTRO="$1"
CT_ID="$2"
TEMPLATE_ID="$3"
GW="$4"
SDN_IP="$5"

# Additional IPs
shift 5
ADDITIONAL_IPS="$@"

# echo "Distro: $DISTRO"
# echo "CT: $CT_ID"
# echo "Template ID: $TEMPLATE_ID"
# echo "Gateway: $GW"

# Cloning the LXC container
pct clone $TEMPLATE_ID $CT_ID 
# echo "Clone DONE"


pct set $CT_ID --hostname $DISTRO --cores 1 --cpulimit 2 --memory 512 --swap 512
# echo "Initial Config DONE"

index=1
# Adding to SDN network 
pct set $CT_ID -net$index name=eth$index,bridge=vnetsdn,firewall=1,gw=192.168.2.1,ip=$SDN_IP/24,type=veth
index=$((index+1)) 
# echo "Adding to SDN DONE"

# Setting up additional IPs
for ip in $ADDITIONAL_IPS; do
    # echo "Adding: $ip"
    pct set $CT_ID -net$index name=eth$index,bridge=vmbr0,firewall=1,gw=$GW,ip=$ip/24,type=veth
    index=$((index+1)) 
done
# echo "Additional IPs DONE"


# Starting the container
# pct start $CT_ID
# echo "Start DONE"