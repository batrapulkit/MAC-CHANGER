import subprocess
import optparse
import re

def get_argument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name to change MAC Address for")
    parser.add_option("-m", "--mac", dest="new_mac_address", help="New MAC address you want")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use -h or --help for more info.")
    elif not options.new_mac_address:
        parser.error("[-] Please specify a new MAC address you want, use -h or --help for more info.")
    
    if re.search(r"\w\w-\w\w-\w\w-\w\w-\w\w-\w\w", options.new_mac_address):
        return options
    else:
        parser.error("[-] Not a valid MAC address! Try again with a valid MAC address")

def change_mac(interface, new_mac_address):
    print("[+] Changing MAC address for " + interface + " to " + new_mac_address)
    # Disable the network interface
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=disable"])
    # Change the MAC address using netsh
    subprocess.call(["netsh", "interface", "set", "interface", interface, "newmac=" + new_mac_address])
    # Enable the network interface again
    subprocess.call(["netsh", "interface", "set", "interface", interface, "admin=enable"])

def get_mac(interface):
    # Use `getmac` to retrieve the current MAC address
    try:
        ifconfig_output = subprocess.check_output(["getmac", "/v", "/fo", "list"], encoding="utf-8")
        # Look for the interface in the `getmac` output
        for line in ifconfig_output.splitlines():
            if interface in line:
                mac_address = line.split(":")[1].strip()
                return mac_address
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving MAC address: {e}")
        return None

options = get_argument()

change_mac(options.interface, options.new_mac_address)

new_mac = get_mac(options.interface)

if new_mac == options.new_mac_address:
    print("[+] MAC address changed to " + new_mac)
else:
    print("[-] Encountered an error while changing MAC address!")
