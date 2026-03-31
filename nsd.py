import time 

logfile = "access.log" 
blocked_file = "blocked_ips.txt" 
ip_count = {} 
blocked_ips = set() 

print("NSD started. Watching access.log...") 

with open(logfile, "r") as f:
    f.seek(0, 2) 

    while True:
        line = f.readline() 
        if not line:
            time.sleep(0.5) 
            continue
        
        parts = line.strip().split() 
        if len(parts) < 2:
            continue
        
        ip = parts[0] 
        path = parts[1] 

        if ip not in ip_count:
            ip_count[ip] = 0
        ip_count[ip] += 1 
 
        print(f"LOG: {ip} {path}") 
        print(f"IP {ip} count {ip_count[ip]}") 
        
        if path == "/admin" or path == "/login":
            print("!!! ALERT: Suspicious access !!!")
        
        if ip_count[ip] >= 5:
            print("!!! ATTACK DETECTED from", ip, "!!!") 

        if ip not in blocked_ips:
            blocked_ips.add(ip) 
            with open(blocked_file, "a") as bf:
                bf.write(ip + "\n")
            print(">>> IP BLOCKED:", ip)
