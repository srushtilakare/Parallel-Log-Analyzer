import time
import re
from concurrent.futures import ThreadPoolExecutor
from collections import defaultdict

LOG_FILE = "data/sample_logs.log"

# pattern: IP, Method, URL, Status, Response time
log_pattern = re.compile(r'(\d+\.\d+\.\d+\.\d+).*"(.*?) (.*?) HTTP.*" (\d+) ([\d.]+)')

def process_log(line):
    match = log_pattern.search(line)
    if not match:
        return None
    ip, method, url, status, response_time = match.groups()
    return {
        "ip": ip,
        "method": method,
        "url": url,
        "status": int(status),
        "response_time": float(response_time)
    }

def analyze_batch(batch):
    summary = defaultdict(int)
    total_time = 0.0

    for log in batch:
        if not log:
            continue
        summary["total"] += 1
        summary[f"status_{log['status']}"] += 1
        summary[f"ip_{log['ip']}"] += 1
        total_time += log["response_time"]

    summary["avg_response_time"] = round(total_time / max(1, summary["total"]), 3)
    return summary

def monitor_logs():
    last_size = 0
    print("📊 Real-time Log Analysis Started...\n")

    with ThreadPoolExecutor(max_workers=4) as executor:
        while True:
            with open(LOG_FILE, "r") as f:
                lines = f.readlines()

            new_lines = lines[last_size:]
            last_size = len(lines)

            if not new_lines:
                time.sleep(1)
                continue

            # Process logs in parallel
            futures = [executor.submit(process_log, line) for line in new_lines]
            processed = [f.result() for f in futures]
            result = analyze_batch(processed)

            print(f"Total: {result['total']}, 404s: {result.get('status_404', 0)}, "
                  f"500s: {result.get('status_500', 0)}, Avg Time: {result['avg_response_time']}s")

            time.sleep(1)

if __name__ == "__main__":
    monitor_logs()
