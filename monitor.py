import psutil
from datetime import datetime
import unittest
from unittest.mock import patch
import time

# Configuration
cpu_usage_threshold = 80  # in percent
memory_usage_threshold = 80  # in percent
disk_usage_threshold = 80  # in percent
network_usage_threshold = 80  # in percent
log_file = "monitoring_log.txt"
monitoring_interval = 5  # in seconds

def log_message(message, log_file=log_file):
    with open(log_file, "a") as log:
        log.write(f"{datetime.now()} - {message}\n")

def check_cpu_usage(cpu_usage_threshold):
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU usage: {cpu_usage}%")
    if cpu_usage > cpu_usage_threshold:
        log_message(f"High CPU usage: {cpu_usage}%")
    else:
        log_message(f"CPU usage: {cpu_usage}%")
    return cpu_usage

def check_memory_usage(memory_usage_threshold):
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent
    print(f"Memory usage: {memory_usage}%")
    if memory_usage > memory_usage_threshold:
        log_message(f"High memory usage: {memory_usage}%")
    else:
        log_message(f"Memory usage: {memory_usage}%")
    return memory_usage

def check_disk_usage(disk_usage_threshold):
    disk_partitions = psutil.disk_partitions()
    for partition in disk_partitions:
        disk_usage = psutil.disk_usage(partition.mountpoint).percent
        print(f"Disk usage for {partition.device}: {disk_usage}%")
        if disk_usage > disk_usage_threshold:
            log_message(f"High disk usage on {partition.device}: {disk_usage}%")
        else:
            log_message(f"Disk usage on {partition.device}: {disk_usage}%")
    return disk_usage

def check_network_usage(network_usage_threshold):
    net_io = psutil.net_io_counters(pernic=True)
    for interface, stats in net_io.items():
        print(f"Network usage for {interface} - Bytes sent: {stats.bytes_sent}, Bytes received: {stats.bytes_recv}")
        # Example threshold check for total bytes sent and received
        if stats.bytes_sent + stats.bytes_recv > network_usage_threshold * 1024 * 1024:
            log_message(f"High network usage on {interface}: Bytes sent {stats.bytes_sent}, Bytes received {stats.bytes_recv}")
        else:
            log_message(f"Network usage on {interface}: Bytes sent {stats.bytes_sent}, Bytes received {stats.bytes_recv}")
    return stats.bytes_sent + stats.bytes_recv

def monitor_system(cpu_usage_threshold, memory_usage_threshold, disk_usage_threshold, network_usage_threshold, monitoring_interval):
    while True:
        log_message("Starting a new monitoring cycle")
        check_cpu_usage(cpu_usage_threshold)
        check_memory_usage(memory_usage_threshold)
        check_disk_usage(disk_usage_threshold)
        check_network_usage(network_usage_threshold)
        log_message("Monitoring cycle completed\n")
        time.sleep(monitoring_interval)

class TestMonitoringScript(unittest.TestCase):
    
    @patch('psutil.cpu_percent')
    def test_check_cpu_usage(self, mock_cpu_percent):
        mock_cpu_percent.return_value = 50
        cpu_usage = check_cpu_usage(cpu_usage_threshold)
        self.assertLessEqual(cpu_usage, cpu_usage_threshold)
    
    @patch('psutil.virtual_memory')
    def test_check_memory_usage(self, mock_virtual_memory):
        mock_virtual_memory.return_value.percent = 60
        memory_usage = check_memory_usage(memory_usage_threshold)
        self.assertLessEqual(memory_usage, memory_usage_threshold)
    
    @patch('psutil.disk_partitions')
    @patch('psutil.disk_usage')
    def test_check_disk_usage(self, mock_disk_usage, mock_disk_partitions):
        mock_disk_partitions.return_value = [psutil._common.sdiskpart(device='C:', mountpoint='/', fstype='NTFS', opts='rw')]
        mock_disk_usage.return_value.percent = 50
        disk_usage = check_disk_usage(disk_usage_threshold)
        self.assertLessEqual(disk_usage, disk_usage_threshold)
    
    @patch('psutil.net_io_counters')
    def test_check_network_usage(self, mock_net_io_counters):
        mock_net_io_counters.return_value = {'Ethernet': psutil._common.snetio(bytes_sent=500, bytes_recv=500)}
        network_usage = check_network_usage(network_usage_threshold)
        self.assertLessEqual(network_usage, network_usage_threshold * 1024 * 1024)

if __name__ == '__main__':
    # Run the monitoring script
    print("Starting the system monitoring. Press Ctrl+C to stop.")
    try:
        monitor_system(cpu_usage_threshold, memory_usage_threshold, disk_usage_threshold, 
                       network_usage_threshold, monitoring_interval)
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    
    # Run the tests
    unittest.main(argv=[''], exit=False)
