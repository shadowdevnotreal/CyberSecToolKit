import nmap
import requests
from bs4 import BeautifulSoup
import argparse
from datetime import datetime
import json
import os

class VulnerabilityScanner:
    def __init__(self):
        self.nm = nmap.PortScanner()
        self.vulners_api_url = "https://vulners.com/api/v3/burp/collection/"

    def scan_network(self, ip_range, ports):
        self.nm.scan(hosts=ip_range, arguments=f'-p{ports}')
        
        vulnerable_hosts = {}
        
        for host in self.nm.all_hosts():
            if self.nm[host].state() == 'up':
                vulnerable_hosts[host] = {'services': {}}
                
                for proto in self.nm[host].all_protocols():
                    lport = self.nm[host][proto].keys()
                    sorted(lport)
                    
                    for port in lport:
                        if self.nm[host][proto][port]['state'] == 'open':
                            service = self.nm[host][proto][port]['name']
                            version = self.nm[host][proto][port].get('version', 'Unknown')
                            vulnerabilities = self.check_vulnerabilities(service, version)
                            
                            vulnerable_hosts[host]['services'][port] = {
                                'service': service,
                                'version': version,
                                'vulnerabilities': vulnerabilities
                            }
        
        return vulnerable_hosts

    def check_vulnerabilities(self, service, version):
        vulnerabilities = []

        # Check using Vulners API
        try:
            response = requests.get(self.vulners_api_url + service.lower(), params={"type": "software"})
            if response.status_code == 200:
                data = response.json()
                for item in data["data"]["documents"]:
                    if version in item["description"] or version.split()[0] in item["description"]:
                        vulnerabilities.append({
                            'CVE': item.get('id', 'N/A'),
                            'Description': item.get('title', 'N/A'),
                            'Severity': item.get('cvss', {}).get('score', 'N/A')
                        })
        except Exception as e:
            print(f"Error querying Vulners API: {str(e)}")

        # Check using Nmap scripts
        try:
            self.nm.scan('127.0.0.1', arguments=f'-p 80 --script vuln')
            for host in self.nm.all_hosts():
                for proto in self.nm[host].all_protocols():
                    lport = self.nm[host][proto].keys()
                    sorted(lport)
                    for port in lport:
                        if self.nm[host][proto][port]['state'] == 'open':
                            service_info = self.nm[host][proto][port]
                            if 'script' in service_info:
                                for script_id, output in service_info['script'].items():
                                    if script_id.startswith('vuln'):
                                        vulnerabilities.append({
                                            'CVE': script_id.split('_')[-1],
                                            'Description': output.strip(),
                                            'Severity': 'Unknown'
                                        })
        except Exception as e:
            print(f"Error running Nmap vulnerability scripts: {str(e)}")

        # Check using CPE (Common Platform Enumeration)
        try:
            cpe_url = f"https://cve.mitre.org/data/cpes/2.0/{service.lower()}.html"
            response = requests.get(cpe_url)
            soup = BeautifulSoup(response.text, 'html.parser')
            cpe_elements = soup.find_all('div', class_='cpe-item')
            for element in cpe_elements:
                cpe_string = element.find('span', class_='cpe23Uri').text.strip()
                if version in cpe_string:
                    vulnerabilities.append({
                        'CVE': 'N/A',
                        'Description': f"CPE Match: {cpe_string}",
                        'Severity': 'Unknown'
                    })
        except Exception as e:
            print(f"Error querying CPE database: {str(e)}")

        return vulnerabilities

    def save_report(self, report_data, output_file):
        with open(output_file, 'w') as f:
            json.dump(report_data, f, indent=2)
        print(f"Report saved to {output_file}")

def main():
    parser = argparse.ArgumentParser(description='Enhanced Vulnerability Scanner')
    parser.add_argument('-r', '--range', help='IP range to scan', required=True)
    parser.add_argument('-p', '--ports', help='Ports to scan (comma-separated)', default='80,443,22,23')
    parser.add_argument('-o', '--output', help='Output file for report', default='scan_report.json')
    parser.add_argument('-v', '--verbose', action='store_true', help='Increase verbosity')
    args = parser.parse_args()
    
    scanner = VulnerabilityScanner()
    
    start_time = datetime.now()
    print(f"Starting scan at {start_time}")
    
    vulnerabilities = scanner.scan_network(args.range, args.ports)
    
    end_time = datetime.now()
    elapsed_time = end_time - start_time
    
    print("\nScan completed.")
    print(f"Total time taken: {elapsed_time}")
    
    if vulnerabilities:
        print("\nVulnerabilities found:")
        for host, services in vulnerabilities.items():
            print(f"{host}:")
            for port, details in services['services'].items():
                print(f"  Port {port}/{details['service']} v{details['version']}:")
                for vuln in details['vulnerabilities']:
                    print(f"    CVE: {vuln['CVE']}, Severity: {vuln['Severity']}")
                    print(f"      Description: {vuln['Description']}")
    else:
        print("No vulnerabilities detected.")

    scanner.save_report(vulnerabilities, args.output)

if __name__ == "__main__":
    main()
