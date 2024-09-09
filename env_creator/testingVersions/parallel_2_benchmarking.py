import subprocess
import concurrent.futures


ct_id = 2005
ct_list = []
gateway = "192.168.1.1"
sdn_end = 11
sdn_ip = "192.168.2."

distro_template = {
        "Alpine": "1001",
        "Ubuntu": "1002",
        "Debian": "1003",
        "Fedora": "1004"
    }

linux_dict = {'Ubuntu': ['192.168.1.199'], 'Debian': ['192.168.1.198']}

def create_container(distro, ct_id, distro_template, gateway, sdn_ip, sdn_end, ips):
        ips = " ".join(ips)
        cmd = f"../launch_lxcs.sh {distro} {ct_id} {distro_template[distro]} {gateway} {sdn_ip}{sdn_end} {ips}"
        print(cmd)
        subprocess.run(cmd.split(" "), stdout=subprocess.DEVNULL)
        ct_list.append(ct_id)

# Create the LXC containers in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    # Submit the create_container function to the executor for each distro
    futures = [executor.submit(create_container, distro, ct_id + i, distro_template, gateway, sdn_ip, sdn_end + i, linux_dict[distro]) for i, distro in enumerate(linux_dict)]
    
    # Wait for all the futures to complete
    concurrent.futures.wait(futures)

def start_containers(ct):
    cmd = f"pct start {ct}"
    subprocess.run(cmd.split(" "), stdout=subprocess.DEVNULL)

# Create a ThreadPoolExecutor with maximum workers equal to the number of containers
with concurrent.futures.ThreadPoolExecutor(max_workers=len(ct_list)) as executor:
    # Submit the start_containers function to the executor for each container
    futures = [executor.submit(start_containers, ct) for ct in ct_list]
    
    # Wait for all the futures to complete
    concurrent.futures.wait(futures)

for ct in ct_list:
    # print(f"Waiting for container {ct} to start...")
    while True:
        cmd = f"pct status {ct}" 
        output = subprocess.run(cmd.split(" "), stdout=subprocess.PIPE, text=True).stdout
        if "running" in output:
            # print(f"Container {ct} is running.")
            break