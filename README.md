# ServerScan

**Developer:** Munther Abdulaziz Al-Qurzai  
**Email:** 2220001172@iau.edu.sa

## Description
ServerScan1 is a Python tool designed to automate the process of identifying server types and versions. Once the server information is gathered, the tool proceeds to search for any known vulnerabilities associated with that specific server version. This aids in proactive security assessments and vulnerability management.

## Features
- **Server Identification:** Automatically detects the server and its version from a given URL.
- **Vulnerability Search:** Searches for exploits related to the identified server version using Exploit-DB.

## Usage
```bash
python serverscan1.py
```



## Requirements
- **Python 3.x**
- **Libraries:** http.client, urllib.parse, re, requests


##Installation
Clone the repository and install the required Python packages:

```bash
git clone https://github.com/CSC-IAU/ServerScan.git
cd ServerScan1
pip install -r requirements.txt
```
