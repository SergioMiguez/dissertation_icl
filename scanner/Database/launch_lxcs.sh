#!/bin/bash

DISTRO="$1"
CT_ID="$2"
PASSWORD="$3"
TEMPLATE_ID="$4"
IP="$5"
GW="$6"

# Additional IPs
shift 6
ADDITIONAL_IPS="$@"


# Cloning the LXC container
pct clone $TEMPLATE_ID $CT_ID --hostname CT$CT_ID \\
    --rootfs Crucial:2 --cores 1 --cpulimit 2 --password $PASSWORD \\
    --net0 name=eth0,bridge=vmbr0,firewall=1,gw=$GW,ip=$IP/24,type=veth \\
    --unprivileged 1 --memory 512 --swap 512

# Setting up additional IPs
index=1
for ip in $ADDITIONAL_IPS; do
    pct set $CT_ID -net$index name=eth$index,bridge=vmbr0,ip=$ip/24,type=veth,tag=13
    index=$((index+1)) 
done

# Starting the container
pct start $CT_ID