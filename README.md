
<p align="center">
  <img width="357" alt="2025-01-23_23-14-50" src="https://github.com/user-attachments/assets/e88122b4-ccbf-4876-8640-ee088722d033">
</p>


## Support FOSS future development 👇- Simping for donations here:

<a href="https://www.buymeacoffee.com/diatasso" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Book" style="height: 40px !important;width: 145px !important;" ></a>

---

# Cybersecurity Toolkit
​
## Overview
​
A comprehensive cybersecurity toolkit designed for threat simulations, vulnerability scans, anomaly detection, stress testing, and real-time monitoring with a web interface. Supports multi-cloud deployment across AWS, GCP, and Azure.
​
## Features
​
- **Reconnaissance Tests**: Gather information about target systems using Nmap.
- **Vulnerability Scans**: Identify vulnerabilities using Nmap NSE scripts.
- **Threat Simulations**: Simulate SQL Injection and DDoS attacks.
- **Stress Testing**: Conduct adaptive stress tests with machine learning feedback loops.
- **Anomaly Detection**: Detect unusual patterns using Isolation Forest.
- **Threat Classification**: Classify threats using Random Forest.
- **Real-Time Monitoring**: Monitor system metrics via a web dashboard.
- **Generate Reports**: Compile test results into comprehensive HTML reports.
- **Deployment Automation**: Deploy the toolkit across AWS, GCP, and Azure using Terraform and Docker.

### Tree
```
​cyber_toolkit/
├── modules/
│   ├── aws/
│   │   └── main.tf
│   ├── gcp/
│   │   └── main.tf
│   └── azure/
│       └── main.tf
├── scripts/
│   ├── analysis/
│   │   ├── anomaly_detection.py
│   │   ├── threat_classification.py
│   │   ├── data_aggregator.py
│   │   └── generate_graphs.py
│   ├── tests/
│   │   ├── sql_injection_test.py
│   │   ├── ddos_simulation.py
│   │   ├── reconnaissance_tests.py
│   │   └── vulnerability_scans.py
│   ├── reporting/
│   │   ├── generate_reports.py
│   │   └── deploy_toolkit.sh
│   └── controllers/
│       └── distributed_controller.py
├── web/
│   ├── gui_server.py
│   └── templates/
│       ├── index.html
│       ├── login.html
│       ├── dashboard.html
│       ├── graphs.html
│       └── reports.html
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── terraform/
│   └── main.tf
├── logs/
│   ├── centralized.log
│   ├── sql_injection_results.log
│   ├── ddos_results.json
│   ├── distributed_results_node_<id>.json
│   ├── stress_test_graph.png
│   ├── reconnaissance_results.log
│   ├── vulnerability_scan_results.log
│   └── reports/
│       └── report_<date>.html
├── requirements.txt
├── cyber_toolkit.sh
├── .gitignore
├── .env.example
└── README.md
```

## Installation
​
### Prerequisites
​
- **Python 3.9+**
- **Docker & Docker Compose**
- **Terraform**
- **Git**
- **Nmap**

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/example/cyber-toolkit.git
    cd cyber_toolkit
    ```

2. **Install Python Dependencies**

    ```bash
    pip3 install --no-cache-dir -r requirements.txt
    ```

3. **Setup Docker**

    - **Build the Docker Image**

        ```bash
        docker build -t cyber-toolkit .
        ```

    - **Run Multiple Instances Locally**

        ```bash
        docker-compose up --scale node=3
        ```

4. **Setup Terraform**

    1. **Configure Providers**

        Update `terraform/main.tf` with your cloud provider credentials and project details.

    2. **Initialize Terraform**

        ```bash
        terraform init
        ```

    3. **Apply Configuration**

        ```bash
        terraform apply -auto-approve
        ```

    4. **Retrieve Public IPs**

        ```bash
        terraform output
        ```

5. **Deploy Toolkit to Cloud**

    ```bash
    ./scripts/deploy_toolkit.sh
    ```

    ## Usage

### Running the CLI

Start the CLI:

```
./cyber_toolkit.sh
Main Menu Options:

Run Reconnaissance Tests
Gathers information about the target using Nmap.
Run Vulnerability Scans
Identifies vulnerabilities using Nmap NSE scripts.
Simulate Threats
a. SQL Injection Test
b. DDoS Simulation
Run Stress Tests
a. Adaptive Stress Test
Generate Reports
Compiles test results into an HTML report.
Run Anomaly Detection
Detects anomalies using Isolation Forest.
Run Threat Classification
Classifies threats using Random Forest.
Aggregate Data for ML
Aggregates logs for machine learning models.
Deploy Toolkit to Cloud
Automates deployment across AWS, GCP, and Azure.
View Centralized Logs
Displays all logs in a unified location.
Exit
Example: Running a Reconnaissance Test

Select option 1.
Enter the target IP when prompted.
Verify that reconnaissance_results.log is generated with Nmap scan results.
Accessing the Web Interface
Start the Web Server

bash
Copy code
python3 web/gui_server.py
Access via Browser

Navigate to http://localhost:5000/login and log in with:

Username: admin
Password: password123
Dashboard Features

Live Metrics: Real-time updates for latency, bandwidth, CPU usage, and memory usage.
View Logs: Access centralized logs.
View Graphs: Visual representations of stress test results.
View Reports: Access generated HTML reports.
Troubleshooting
Common Issues
SSH Connection Failures

Solution:
Ensure SSH keys are correctly configured.
Verify that the security groups/firewalls allow SSH access (port 22).
Docker Errors

Solution:
Check Docker installation and service status.
Ensure that ports 5000, 5001, 5002, etc., are not in use.
Terraform Errors

Solution:
Verify cloud provider credentials and permissions.
Ensure that the specified regions and resources are available.
Web Interface Not Loading

Solution:
Ensure the Flask server is running.
Check firewall settings to allow access to port 5000.
Python Dependency Issues

Solution:
Run pip3 install --no-cache-dir -r requirements.txt to install all dependencies.
Testing Recommendations
Simulated Testing
SQL Injection Test

Setup: Use a locally hosted vulnerable application (e.g., DVWA).
Action: Run the SQL injection test against the DVWA login page.
Expected Result: Detection of vulnerabilities if present.
DDoS Simulation

Setup: Use a controlled test server to prevent actual service disruption.
Action: Execute the DDoS simulation against the test server.
Expected Result: Monitor server response under load; ensure the server remains stable or fails gracefully.
Adaptive Stress Test

Setup: Target a server with known performance metrics.
Action: Run the adaptive stress test and observe adjustments based on latency.
Expected Result: Dynamic scaling of stress based on detected anomalies.
Real-World Deployment
Deploy to a Staging Environment

Use Terraform to provision resources across AWS, GCP, and Azure.
Deploy the toolkit using deploy_toolkit.sh.
Run comprehensive stress and threat simulations.
Monitor and Analyze

Use the web dashboard to monitor real-time metrics.
Review centralized logs for insights and anomalies.
Validate that the toolkit adapts to detected threats and load changes.
Future Enhancements
Advanced Threat Simulations

Incorporate additional attack vectors like XSS, CSRF, and more.
Multi-Cloud Orchestration

Implement Kubernetes for enhanced scalability and management.
Collaborative Features

Enable multi-user roles with specific permissions for collaborative monitoring and testing.
Enhanced Visualization

Develop more comprehensive dashboards with detailed analytics and reporting capabilities.
Conclusion
With the implementation of options 1, 2, and 5, your cybersecurity toolkit is now more comprehensive and fully functional. You can perform reconnaissance, vulnerability scans, simulate threats, run stress tests, detect anomalies, classify threats, and generate detailed reports—all from a centralized CLI and web interface. The multi-cloud deployment support ensures scalability and flexibility across different cloud environments.

Feel free to test each feature as described in the usage guide and reach out if you encounter any issues or need further enhancements. Happy testing and stay secure!
```






As always = TY 😊 

<a href="https://www.buymeacoffee.com/diatasso">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy me a cat&emoji=🐈&slug=notarealdev&button_colour=9123cd&font_colour=ffffff&font_family=Bree&outline_colour=ffffff&coffee_colour=FFDD00" />
</a>
