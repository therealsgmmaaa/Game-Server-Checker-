#!/usr/bin/env python3
import socket
import time

# ANSI Colors
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

# GoldSrc / Quake Color Palette mapping (^0 - ^7)
QC = {
    "0": "\033[30m", # Black
    "1": "\033[31m", # Red
    "2": "\033[32m", # Green
    "3": "\033[33m", # Yellow
    "4": "\033[34m", # Blue
    "5": "\033[36m", # Cyan
    "6": "\033[35m", # Magenta
    "7": "\033[37m", # White
}

def colorize(s):
    if not s:
        return ""
    out = ""
    i = 0
    while i < len(s):
        if s[i] == "^" and i + 1 < len(s) and s[i+1] in QC:
            out += QC[s[i+1]]
            i += 2
        else:
            out += s[i]
            i += 1
    return out + RESET

def query_cs_server(ip, port):
    # A2S_INFO query packet for HL1 / GoldSrc / Xash3D / Source
    packet = b"\xff\xff\xff\xffTSource Engine Query\x00"
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(2.5)
    
    start = time.perf_counter()
    try:
        sock.sendto(packet, (ip, port))
        data, _ = sock.recvfrom(4096)
        latency = (time.perf_counter() - start) * 1000
        
        if data.startswith(b"\xff\xff\xff\xff"):
            header = data[4:5]
            payload = data[5:]
            
            protocol_str = "Unknown"
            
            # Modern A2S_INFO (Header 'I')
            if header == b"I":
                proto_byte = payload[0]
                if proto_byte == 49:
                    protocol_str = "49 ( Xash3D Engine )"
                elif proto_byte == 48:
                    protocol_str = "48 ( GoldSrc )"
                else:
                    protocol_str = f"{proto_byte}"

                parts = payload[1:].split(b"\x00")
                if len(parts) >= 3:
                    server_name = parts[0].decode("latin-1", errors="ignore")
                    map_name = parts[1].decode("utf-8", errors="ignore")
                    folder = parts[2].decode("utf-8", errors="ignore")
                    game = parts[3].decode("utf-8", errors="ignore") if len(parts) > 3 else ""

                    # Calculate offset to extract player counts
                    rem = payload[1:]
                    null_count = 0
                    idx = 0
                    for i, b in enumerate(rem):
                        if b == 0:
                            null_count += 1
                            if null_count == 4:
                                idx = i + 1
                                break

                    rem_bytes = rem[idx:]
                    players = rem_bytes[2] if len(rem_bytes) >= 3 else 0
                    max_players = rem_bytes[3] if len(rem_bytes) >= 4 else 0

                    return {
                        "name": server_name,
                        "map": map_name,
                        "folder": folder,
                        "game": game,
                        "protocol": protocol_str,
                        "players": players,
                        "max_players": max_players,
                        "ping": round(latency, 1)
                    }

            # Legacy GoldSrc (Header 'm')
            elif header == b"m":
                protocol_str = "47 ( GoldSrc Legacy )"
                parts = payload.split(b"\x00")
                if len(parts) >= 4:
                    server_name = parts[1].decode("latin-1", errors="ignore")
                    map_name = parts[2].decode("utf-8", errors="ignore")
                    folder = parts[3].decode("utf-8", errors="ignore")
                    game = parts[4].decode("utf-8", errors="ignore") if len(parts) > 4 else ""
                    players = parts[0][0] if len(parts[0]) > 0 else 0
                    max_players = parts[0][1] if len(parts[0]) > 1 else 0

                    return {
                        "name": server_name,
                        "map": map_name,
                        "folder": folder,
                        "game": game,
                        "protocol": protocol_str,
                        "players": players,
                        "max_players": max_players,
                        "ping": round(latency, 1)
                    }
    except socket.timeout:
        pass
    except Exception:
        pass
    finally:
        sock.close()
    return None

def main():
    print(f"\n{BOLD}{CYAN}============== [ GoldSrc / CS 1.6 UDP Server Query ] =============={RESET}")
    print(f"{YELLOW}[i] Description:{RESET} Direct UDP A2S_INFO query tool for Counter-Strike 1.6 & HL1 servers.\n")

    server_input = input(f"{YELLOW}[?] Enter Server IP:Port (e.g. 127.0.0.1:27015 or play.example.com:27015): {RESET}").strip()
    
    if not server_input:
        print(f"\n{RED}[!] No target input provided.{RESET}\n")
        return

    if ":" in server_input:
        host, port_str = server_input.split(":", 1)
        port = int(port_str) if port_str.isdigit() else 27015
    else:
        host = server_input
        port = 27015

    try:
        ip = socket.gethostbyname(host)
        print(f"\n{YELLOW}[*] Querying server {ip}:{port} via UDP...{RESET}")
    except socket.gaierror:
        print(f"\n{RED}[!] Invalid Domain or IP Address.{RESET}\n")
        return

    info = query_cs_server(ip, port)

    if info:
        formatted_name = colorize(info['name'])
        
        print(f"\n{GREEN}[+] Server {ip}:{port}{RESET} " + "─" * 50)
        print(f"  Hostname   : {formatted_name}")
        print(f"  Raw Colors : {info['name']}")
        print(f"  Map        : {info['map']}")
        print(f"  Players    : {info['players']} / {info['max_players']}".ljust(45) + f"Game Type  : {info['folder']}")
        print(f"  Server Protocol   : {info['protocol']}".ljust(45) + f"ISP Ping : {info['ping']} ms")
        print("─" * 75 + "\n")
    else:
        print(f"\n{RED}[!] Server Offline or Unreachable (No UDP response on port {port}).{RESET}\n")

if __name__ == "__main__":
    main()
