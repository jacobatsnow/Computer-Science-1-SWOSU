import platform
import psutil
import subprocess
import json

def get_cpu_info():
    try:
        cpu_name = subprocess.check_output(
            ["powershell", "(Get-CimInstance Win32_Processor).Name"]
        ).decode().strip()
    except:
        cpu_name = platform.processor()

    cores = psutil.cpu_count(logical=False)
    threads = psutil.cpu_count(logical=True)

    freq_info = psutil.cpu_freq()
    freq = freq_info.current if freq_info else 0

    return {
        "name": cpu_name,
        "cores": cores,
        "threads": threads,
        "frequency_mhz": freq
    }

def get_ram_info():
    ram = psutil.virtual_memory()
    return {"total_gb": round(ram.total / (1024**3), 2)}

def get_gpu_info():
    try:
        gpu_raw = subprocess.check_output(
            ["powershell", "(Get-CimInstance Win32_VideoController).Name"]
        ).decode().strip().split("\n")
        gpus = [g.strip() for g in gpu_raw if g.strip()]
    except:
        gpus = ["Unknown GPU"]
    return gpus

def get_disk_info():
    disk = psutil.disk_usage('C:\\')
    return {
        "total_gb": round(disk.total / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2)
    }

def rate_system(cpu, ram, gpu):
    score = 0

    if cpu["cores"] >= 8:
        score += 3
    elif cpu["cores"] >= 4:
        score += 2
    else:
        score += 1

    if ram["total_gb"] >= 16:
        score += 3
    elif ram["total_gb"] >= 8:
        score += 2
    else:
        score += 1

    if any("RTX" in g or "RX" in g for g in gpu):
        score += 3
    elif any("GTX" in g for g in gpu):
        score += 2
    else:
        score += 1

    if score >= 8:
        rating = "High-end — great for gaming, engineering, and heavy workloads"
    elif score >= 5:
        rating = "Mid-range — good for everyday use and light gaming"
    else:
        rating = "Low-end — fine for basic tasks but limited for gaming or engineering"

    return rating, score

def main():
    cpu = get_cpu_info()
    ram = get_ram_info()
    gpu = get_gpu_info()
    disk = get_disk_info()

    rating, score = rate_system(cpu, ram, gpu)

    results = {
        "CPU": cpu,
        "RAM": ram,
        "GPU": gpu,
        "Disk": disk,
        "System Rating": rating,
        "Score": score
    }

    print(json.dumps(results, indent=4))
    input()

if __name__ == "__main__":
    main()
    input()