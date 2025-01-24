![A futuristic cyber security command center](https://github.com/user-attachments/assets/d913ccf1-6e83-4a04-9188-1f2e1342439d)

## Support FOSS future development - Simping for donations here 👇

<a href="https://www.buymeacoffee.com/diatasso">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a cat&emoji=🐈&slug=notarealdev&button_colour=9123cd&font_colour=ffffff&font_family=Bree&outline_colour=ffffff&coffee_colour=FFDD00" />
</a>

---

# Enhanced Vulnerability Scanner

## Overview

This enhanced vulnerability scanner is designed to automate the process of identifying potential security issues in networked systems. It combines multiple techniques to detect vulnerabilities, including:

1. Network scanning using Nmap
2. Vulners API integration
3. Nmap scripting engine
4. Common Platform Enumeration (CPE) checks

## Installation

Make file executable:
```
sudo chmod +x enhancedscanner.py
```
To use this tool, ensure you have the following dependencies installed:

```
pip install python-nmap requests beautifulsoup4
```

Also, make sure you have Nmap installed on your system.

## Usage

Run the scanner using the following command:

```
python3 enhancedscanner.py -r <ip_range> [-p <ports>] [-o <output_file>] [-v]
```

Example:
```
python3 enhancedscanner.py -r 192.168.1.0/24 -p 80,443,22,23 -o scan_results.json -v
```

## Features

1. **Comprehensive Scanning**: 
   - Scans IP ranges and specific ports
   - Detects open services and versions

2. **Multi-source Vulnerability Detection**:
   - Uses Vulners API for known vulnerabilities
   - Leverages Nmap scripts for advanced checks
   - Checks CPE database for software matches

3. **Detailed Reporting**:
   - Generates JSON reports with vulnerability details
   - Includes CVE numbers, descriptions, and severity levels

4. **Flexible Output Options**:
   - Saves results to a specified JSON file
   - Provides verbose console output

5. **Performance Tracking**:
   - Displays total scan duration

## Security Considerations

1. **Permission Required**: Only scan networks you own or have explicit permission to test.
2. **Rate Limiting**: Be aware of API rate limits when using external services.
3. **False Positives**: Verify critical findings manually, as automated scans can produce false positives.

## Future Enhancements

1. Add more vulnerability databases
2. Implement parallel processing for faster scans
3. Include remediation suggestions in reports

## License

This software is released under the MIT License. See LICENSE.txt for details.

## Contributing

Contributions are welcome! Please submit pull requests with clear explanations of changes.


Please ensure you've met all the prerequisites for your operating system before running the installation scripts.


## Contributing

We welcome contributions! Please follow these steps to contribute:

1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the Branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.

## Feedback and Support

For support, feedback, or suggestions, please open an issue in the GitHub repository. Your input helps make BashBuddy better for everyone.

### Final Steps

- Ensure you replace `https://github.com/username/blank.git` with the actual URL of your GitHub repository.
- Adjust any specific instructions or descriptions as needed based on your project's setup or requirements.
- If you have not already, consider adding a `LICENSE` file to clearly communicate how others can use or contribute to your project.

This README provides a comprehensive guide for users to get started, understand its features, and know how to contribute.

---

As always = TY 😊 

<a href="https://www.buymeacoffee.com/diatasso">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a cat&emoji=🐈&slug=notarealdev&button_colour=9123cd&font_colour=ffffff&font_family=Bree&outline_colour=ffffff&coffee_colour=FFDD00" />
</a>
