import requests
import re

def executerequest():
    print("--- CFX.re IP Resolver ---")
    while True:
        user_input = input("Please input the server's CFX.re address (e.g., cfx.re/join/xxxx): ").strip()
        if user_input.startswith("cfx.re/join/"):
            first_url = f"https://{user_input}"
            formatted_url = user_input
        elif user_input.startswith("https://cfx.re/join/"):
            first_url = user_input
            formatted_url = user_input.replace("https://", "")
        else:
            first_url = f"https://cfx.re/join/{user_input}"
            formatted_url = f"cfx.re/join/{user_input}"

        try:
            response = requests.get(first_url, timeout=10)
            server_url = response.headers.get("x-citizenfx-url")
            if server_url:
                server_ip = server_url.replace("http://", "").replace("/", "")
                print(f"\nCFX.re Link: \033[37m{formatted_url}\033[0m")
                print(f"Resolved IP: \033[33m{server_ip}\033[0m\n")
            else:
                raise Exception("Header not found")

        except Exception:
            print("\033[31mError: Unable to find the server! Verify the CFX.re address or check if the server is currently online.\033[0m\n")

if __name__ == "__main__":
    try:
        executerequest()
    except KeyboardInterrupt:
        print("\nScript terminato.")