# Dynamic Network Twins to Improve

Threat IntelligenceAuthor: Sergio Miguez Aparicio

The project's code has been gathered in this directory, however, in the real implementation it might run in separated hosts.

- env_creator: contains Proxmox scripts to create and configure automatically LXCs. These must be directly run inside Proxmox as it uses the Proxmox's API. Adding on, contains all the testing and benchmarks scripts + results for this part of the project.
- scanner: the scanner was run inside a Ubuntu LXC added  to the VLAN to gather the required data. This directory contains all the scripts required to gather data from the attackers network environment. It also includes the benchmark scripts + results related to scans.
- switch_auto: is the directory that runs directly in Proxmox and is used to change the switch's configuration automatically when required. The folder contains the YAML config files to set the TP-Link TL-SG105E with the desired configuration as explained in the writeup. It relies on Manawyrm's public project ([https://github.com/Manawyrm/switchconf](https://github.com/Manawyrm/switchconf)) and for testing, the repository should be cloned inside switch_auto repository. A Switch_Automation file gives more deail to run correctly the project.
