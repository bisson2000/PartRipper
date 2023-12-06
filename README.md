# PartRipper

Cornell Tech5900 Fall2023 - PartRipper - Proof of concept


### Description

This repository is a proof of concept for the PartRipper idea proposed in Tech5900 Fall2023. The main goal of this repository is to showcase that it is possible to obtain the necessary information for making part suggestions.


### Quick start guide:

Requirements:

Python3, pip


1. Clone the repository
2. `cd` in the repository
3. Create a virtual environment ```python -m venv venv```
4. Activate the virtual environment
    1. For Windows, use ```source venv/Scripts/activate```
    2. For Unix systems (Mac, Linux), use ```source venv/bin/activate```
5. Install the requirements ```python -m pip install -r requirements.txt```
6. Run the main file ```python src/main.py```

Notes: The database used in this repository is not public. In other words, [./src/data_fetch.py](./src/data_fetch.py) needs to be customized for the program to work.

Sample output:

```
$ python src/main.py 
======================================== System Information ========================================
System: Windows
Node Name: 
Release: 10
Version: 10.0.19045
Machine: AMD64
Processor: Intel64 Family 6 Model 158 Stepping 9, GenuineIntel
======================================== Boot Time ========================================
Boot Time: 2023/12/5 10:54:29
======================================== CPU Info ========================================
Physical cores: 4
Total cores: 4
Max Frequency: 2496.00Mhz
Min Frequency: 0.00Mhz
Current Frequency: 2496.00Mhz
CPU Usage Per Core:
Core 0: 6.2%
Core 1: 15.6%
Core 2: 9.4%
Core 3: 6.2%
Total CPU Usage: 27.4%
======================================== Memory Information ========================================
Total: 31.87GB
Available: 18.34GB
Used: 13.53GB
Percentage: 42.5%
==================== SWAP ====================
Total: 4.75GB
Free: 4.54GB
Used: 216.73MB
Percentage: 4.5%
======================================== Disk Information ========================================
Partitions and Usage:
=== Device: A:\ ===
  Mountpoint: A:\
  File system type: NTFS
  Total Size: 1.82TB
  Used: 465.60GB
  Free: 1.36TB
  Percentage: 25.0%
=== Device: B:\ ===
  Mountpoint: B:\
  File system type: NTFS
  Total Size: 931.51GB
  Used: 491.62GB
  Free: 439.89GB
  Percentage: 52.8%
Total read: 26.06GB
Total write: 22.18GB
======================================== GPU Details ========================================
  id  name                        load    free memory    used memory    total memory    temperature    uuid
----  --------------------------  ------  -------------  -------------  --------------  -------------  ----------------------------------------
   0  NVIDIA GeForce GTX 1050 Ti  1.0%    4017.0MB       0.0MB          4096.0MB        48.0 °C        GPU-XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
suggestion CPU:  {'Brand': 'Intel', 'Name': 'Core m3-8114Y', 'Codename': 'Cannon Lake-Y', 'Cores': '2  / 4', 'Clock': '1.5 to 2.2 GHz', 'Socket': 'BGA 1440', 'Process': '10 nm', 'L3 Cache': '4 MB', 'TDP': '5 W', 'Released': 'May 5th, 2018'}
suggestion FREQ (GHz):  2.2
suggestion TDP:  5.0

```


