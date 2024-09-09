import sys
import sqlite3
import subprocess
import concurrent.futures

def get_all_devices_in_VLAN(db_path:str=None):
    try:
        
        if db_path is None:
            db_path = "networkDevices.db"
        
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Execute the query to get all devices
        sql_cmd = f"SELECT ip_address, operating_system, distribution FROM devices WHERE vlan = {vlan};"
        cursor.execute(sql_cmd)
        
        # Fetch all the rows
        rows = cursor.fetchall()
        
        # Close the cursor and connection
        cursor.close()
        conn.close()
        
        dict_rows = []
        for row in rows:
            
            ip = row[0]
            os = row[1]
            distro = row[2]
            
            # Those not supported or not identified, set to Alpine Linux
            if os != "Linux" and os != "Windows" or distro == "":
                os = "Linux"
                distro = "Alpine"
            
            # Only Windows 10 available
            elif os == "Windows" and distro != "10":
                distro = "10"
            
            dict_row = {
            'ip': ip,
            'os': os,
            'distro': distro
            }
            dict_rows.append(dict_row)
                    
        
        return dict_rows

    except Exception as e:
        print(f"Error: {e}")
        return []


def main():       
    if vlan == 0:
        print("VLAN is required")
        sys.exit(1)
        
    # Call the function to get all devices
    devices = get_all_devices_in_VLAN(db_path)

    linux_dict = {}
    windows_dict = {}
    other_dict = {}
    
    # Classify devices by distro
    for device in devices:
        # run launch script
               
        os = device.get('os')
        distro = device.get('distro')
        
        if os == "Linux":
            if distro == "Ubuntu":
                if 'Ubuntu' not in linux_dict:
                    linux_dict['Ubuntu'] = []
                linux_dict['Ubuntu'].append(device.get('ip'))
            elif distro == "Debian":
                if 'Debian' not in linux_dict:
                    linux_dict['Debian'] = []
                linux_dict['Debian'].append(device.get('ip'))
            elif distro == "Fedora":
                if 'Fedora' not in linux_dict:
                    linux_dict['Fedora'] = []
                linux_dict['Fedora'].append(device.get('ip'))
            elif distro == "Alpine":
                if 'Alpine' not in linux_dict:
                    linux_dict['Alpine'] = []
                linux_dict['Alpine'].append(device.get('ip'))
            else:
                if 'Other' not in linux_dict:
                    linux_dict['Other'] = []
                linux_dict['Other'].append(device.get('ip'))
        elif os == "Windows":
            if distro == "10":
                if 'Windows 10' not in windows_dict:
                    windows_dict['Windows 10'] = []
                windows_dict['Windows 10'].append(device.get('ip'))
            else:
                if 'Other' not in windows_dict:
                    linux_dict['Other'] = []
                windows_dict['Other'].append(device.get('ip'))
        else:
            if 'Other' not in other_dict:
                other_dict['Other']
            other_dict['Other'].append(device.get('ip'))

    # Set the CT IDs of the Templates for each distro
    distro_template = {
        "Alpine": "1001",
        "Ubuntu": "1002",
        "Debian": "1003",
        "Fedora": "1004"
    }
    
    ct_id = 2000
    ct_list = []
    gateway = "192.168.1.1"
    sdn_end = 11
    sdn_ip = "192.168.2."
    
    # Create the LXC containers
    # for i, distro in enumerate(linux_dict):
    #     ips = " ".join(linux_dict[distro])
    #     cmd = f"./launch_lxcs.sh {distro} {ct_id + i} {distro_template[distro]} {gateway} {sdn_ip}{sdn_end + i} {ips}"
    #     print(cmd)
    #     subprocess.run(cmd.split(" "), stdout=subprocess.DEVNULL)
    #     ct_list.append(ct_id + i)
    #     print(f"Created {distro} container")
    
    def create_container(distro, ct_id, distro_template, gateway, sdn_ip, sdn_end, ips):
        ips = " ".join(ips)
        cmd = f"./testingVersions/lxc_no_start.sh {distro} {ct_id} {distro_template[distro]} {gateway} {sdn_ip}{sdn_end} {ips}"
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
         
        
if __name__ == "__main__":    
    # Getting the subnetwork and credential to execute scan   
    try: 
        vlan = sys.argv[1] if len(sys.argv) > 1 else None
    except Exception as e:
        print(f"VLAN Error: {e}")
        sys.exit(1)
    
    try:
        db_path = sys.argv[2] if len(sys.argv) > 2 else None
    except Exception as e:
        print(f"DB Path Error: {e}")
        sys.exit(1)
        
    # Running script
    main()