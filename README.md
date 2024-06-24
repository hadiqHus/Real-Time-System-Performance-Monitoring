# Real-Time-System-Performance-Monitoring
The Real-Time System Performance Monitoring Script is a comprehensive Python-based tool designed to continuously monitor and log various system performance metrics on Windows systems. This script helps in proactively identifying and resolving potential performance bottlenecks by tracking CPU, memory, disk, network, and GPU usage in real-time.

# Key Features:

# CPU Usage Monitoring
The script tracks CPU usage using the psutil library, logging and printing the usage percentage. It flags high usage when it exceeds a customizable threshold.
# Memory Usage Monitoring
It monitors the system’s memory usage, logging and printing the usage percentage. High usage is flagged when it surpasses a set threshold.
# Disk Usage Monitoring
The script checks disk usage for all partitions, logging and printing the usage percentage for each. It highlights partitions with usage above the specified threshold.
# Network Usage Monitoring
It monitors network activity on all interfaces, logging and printing the bytes sent and received. High network usage is flagged based on a customizable threshold.
# (Doesn't work) GPU Usage Monitoring 
Using the GPUtil library, the script tracks GPU usage, logging and printing the load percentage for each GPU. It flags GPUs with usage above the set threshold.
# Customizable Thresholds
Users can set usage thresholds for CPU, memory, disk, network, and GPU to tailor the monitoring to specific needs.
# Continuous Monitoring
The script runs in a loop with a configurable interval, providing ongoing performance insights and facilitating timely interventions during high resource usage periods.
# Logging
All performance metrics and alerts are logged with timestamps to a file for historical reference and analysis.

# Log File
![image](https://github.com/hadiqHus/Real-Time-System-Performance-Monitoring/assets/64806441/3052b5ca-4807-4465-ad78-b19f62cfd190)

# Script
![image](https://github.com/hadiqHus/Real-Time-System-Performance-Monitoring/assets/64806441/ddaf62b1-10b4-499e-8446-89c7523a8576)

