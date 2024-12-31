import http.client
from urllib.parse import urlparse
import re
import requests

def get_server_info(website_url):
    try:
        parsed_url = urlparse(website_url)
        host = parsed_url.netloc if parsed_url.netloc else parsed_url.path
        port = 443 if parsed_url.scheme == "https" else 80
        
        if parsed_url.scheme == "https":
            connection = http.client.HTTPSConnection(host, port, timeout=10)
        else:
            connection = http.client.HTTPConnection(host, port, timeout=10)
        
        connection.request("HEAD", "/")
        response = connection.getresponse()
        server_info = response.getheader("Server", "Unknown")
        
        server_name, server_version = "Unknown", "Unknown"
        if server_info != "Unknown":
            match = re.match(r"([a-zA-Z\-\/]+)[/\s]?([\d.]+)?", server_info)
            if match:
                server_name = match.group(1) if match.group(1) else "Unknown"
                server_version = match.group(2) if match.group(2) else "Unknown"

        print(f"Website: {website_url}")
        print(f"Server Name: {server_name}")
        print(f"Server Version: {server_version}")
        return server_name, server_version
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'connection' in locals():
            connection.close()
    return None, None

def search_exploit_db(server_name, server_version):
    try:
        query = f"{server_name} {server_version}"
        print(f"Searching Exploit-DB for '{query}'...")
        response = requests.get(f"https://www.exploit-db.com/search?q={query}")
        
        if response.status_code == 200:
            print("Exploits found:")
            print(response.text[:1000])
        else:
            print(f"Failed to fetch exploits. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error while searching Exploit-DB: {e}")

website = input("Enter a website URL (e.g., https://example.com): ").strip()
server_name, server_version = get_server_info(website)

if server_name != "Unknown":
    search_exploit_db(server_name, server_version)
else:
    print("Server information could not be determined.")
