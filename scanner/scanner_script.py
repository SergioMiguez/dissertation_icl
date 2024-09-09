import os
import re
import sys
import json
import subprocess
import concurrent.futures

def raw_scan(subnetwork:str = None):
    """
    This is a fast scan to gather general information about the devices in the network
    """
    
    try:
        # Creating Nmap command
        nmap_cmd = f"sudo nmap -sn -n -T5 --host-timeout 15m --scan-delay 0 {subnetwork}"
        nmap_cmd = nmap_cmd.split(" ")
        # Running Nmap and capturing the output
        return subprocess.run(nmap_cmd, capture_output=True, text=True).stdout
        
    except Exception as e:
        print(f"Error: {e}")


def scan_ip_OS(ip:str = None):
    """
    Scanning the IP addresses with more detail information about the OS and version
    """
       
    print(f"Scanning {ip}")
    try:
        # Creating nmap command
        nmap_cmd = f"sudo nmap -F -O -T5 -n --max-retries 2 --host-timeout 15m --scan-delay 0 {ip} --version-light --osscan-limit --max-os-tries 1 -oN ./Scans/{ip}"
        nmap_cmd = nmap_cmd.split(" ")
        # Running Nmap
        subprocess.run(nmap_cmd, stdout=subprocess.DEVNULL)
        # subprocess.run(nmap_cmd)
        
    except Exception as e:
        print(f"Error: {e}")
        

def get_OS(file_path:str = None):
    """
    Parsing the scan results to get OS information
    """
    
    try:
        with open(file_path) as f:
            content = f.read()
            # Parsing aggressive OS guesses
            guesses = re.findall(r"Aggressive OS guesses: (.+)", content)
            if guesses:
                guesses = re.split(r"\%\)\,", guesses[0])
                os_list = []
                for guess in guesses:
                    os_info = re.split(r"\((?=\d)", guess)
                    # os_info = guess.split(" (")
                    os_name = os_info[0].strip()
                    probability = os_info[1].strip().replace("%)", "")
                    os_list.append({
                        "name": os_name,
                        "probability": probability
                    })
                return os_list
            else:
                return None
            
    except Exception as e:
        print(f"Error: {e}")


def main(subnetwork):
    print(f"Scanning subnetwork {subnetwork}")
    
    # Performing a fast ping scan to know which devices are in the network
    content = raw_scan(subnetwork)

    # regex to get IP addresses
    ip_addresses = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", content)

    # Using parallel processing to furthe scan the IP addresses and get OS information
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(scan_ip_OS, ip_addresses)

    # Create a results.json file to store the results
    # Create a dictionary to store the results
    results = {}

    # parsing scan results to get IP addresses with OS information 
    scan_dir = "./Scans"
    devices = []
    for file_name in os.listdir(scan_dir):
        file_path = os.path.join(scan_dir, file_name)
        if os.path.isfile(file_path):
            ip = file_name
            # os_list = check_file_OS(file_path)
            os_list = get_OS(file_path)
            if os_list:
                device = {
                    "ip": ip,
                    "os": []
                }
                for os_name in os_list:
                    os_info = {
                        "name": os_name.get("name"),
                        "probability": os_name.get("probability")
                    }
                    device["os"].append(os_info)
                devices.append(device)
            else:
                continue
            
    results = {
        "Devices": devices
    }
    
    # Write the results to data.json
    with open("data.json", "w") as f:
        json.dump(results, f)
   
   # Ensure that the data.json file is accessible to all users
    try:
        chmod_cmd = "chmod 666 data.json"
        subprocess.run(chmod_cmd.split(" "))
    except Exception as e:
        print(f"Error: {e}")


def cleanScans():
    """
    Clean the Scans directory
    """
    for file_name in os.listdir("./Scans"):
        file_path = os.path.join("./Scans", file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == "__main__":    
    # Getting the subnetwork and credential to execute scan
    try: 
        subnetwork = sys.argv[1] if len(sys.argv) > 1 else None
    except Exception as e:
        print(f"Subnetwork Error: {e}")
        sys.exit(1) 
    
    # Running script
    main(subnetwork)
    cleanScans()