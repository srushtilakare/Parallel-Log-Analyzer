import random
import time

statuses = [200, 404, 500, 301, 302]
methods = ["GET", "POST", "DELETE", "PUT"]
ips = [f"192.168.1.{i}" for i in range(1, 50)]
urls = ["/home", "/login", "/dashboard", "/api/data", "/logout"]

def generate_log():
    ip = random.choice(ips)
    method = random.choice(methods)
    url = random.choice(urls)
    status = random.choice(statuses)
    response_time = round(random.uniform(0.1, 1.5), 3)
    log = f"{ip} - - [{time.strftime('%Y-%m-%d %H:%M:%S')}] \"{method} {url} HTTP/1.1\" {status} {response_time}\n"
    return log

with open("data/sample_logs.log", "a") as f:
    while True:
        log_line = generate_log()
        f.write(log_line)
        f.flush()
        time.sleep(0.3)  # simulate real-time log generation
