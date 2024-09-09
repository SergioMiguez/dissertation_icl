# Dynamic Network Twins to Improve Threat Intelligence

Threat IntelligenceAuthor: Sergio Miguez Aparicio

The project's code has been gathered in this directory; however, in the real implementation, it might run in separate hosts.

- env_creator: contains Proxmox scripts to automatically create and configure LXCs. These must be run directly inside Proxmox as they use the Proxmox API. Adding on, it contains all the testing and benchmark scripts and results for this part of the project.
- scanner: the scanner was run inside a Ubuntu LXC added  to the VLAN to gather the required data. This directory contains all the scripts required to gather data from the attacker's network environment. It also includes the benchmark scripts + results related to scans.
- switch_auto: is the directory that runs directly in Proxmox and changes the switch's configuration automatically when required. The folder contains the YAML config files to set the TP-Link TL-SG105E with the desired configuration as explained in the writeup. It relies on Manawyrm's public project ([https://github.com/Manawyrm/switchconf](https://github.com/Manawyrm/switchconf)) and for testing, the repository should be cloned inside the switch_auto directory. A Switch_Automation file gives more detail to run the project correctly.
