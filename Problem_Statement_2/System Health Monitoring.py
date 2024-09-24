import psutil
import time

# Define thresholds in percentage
CPU_threshold = 80  
Memory_threshold  = 80
Disk_threshold  = 80

def check_system_health():
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_threshold:
        print(f"ALERT: High CPU usage detected: {cpu_usage}%")
    
    # Check memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > Memory_threshold:
        print(f"ALERT: High Memory usage detected: {memory_usage}%")
    
    # Check disk usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > Disk_threshold:
        print(f"ALERT: High Disk usage detected: {disk_usage}%")
    
    # Check number of running processes
    process_count = len(psutil.pids())
    print(f"Running processes: {process_count}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)