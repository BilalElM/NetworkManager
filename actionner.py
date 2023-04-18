import os
import json
import ping3


def show_help():
    print()
    print("Available commands")
    print("------------------")
    print("- list: Lists all the hosts that are currently being monitored")
    print("- add: Adds a new host to the list of hosts to be monitored")
    print("- remove: Removes a host from the list of hosts to be monitored")
    print("- check: Checks if the hosts in the list are responding")
    print("- help: Displays this help message")


def list_hosts():
    hosts_file_path = os.path.expanduser("~") + "/okserver/list.json"
    if os.path.exists(hosts_file_path):
        with open(hosts_file_path) as f:
            hosts_list = json.load(f)["hosts"]
            print("List of hosts being monitored")
            print("-----------------------------")
            if len(hosts_list) > 0:
                for host in hosts_list:
                    print(host)
            else:
                print("No hosts are being monitored")
                print("Use the 'add' command to add a host to the list")
    else:
        print("List of hosts being monitored")
        print("-----------------------------")
        print("No hosts are being monitored")
        print("Use the 'add' command to add a host to the list")


def add_host(host):
    hosts_dir_path = os.path.expanduser("~") + "/okserver"
    hosts_file_path = hosts_dir_path + "/list.json"
    if not os.path.exists(hosts_dir_path):
        os.mkdir(hosts_dir_path)
    if not os.path.exists(hosts_file_path):
        with open(hosts_file_path, "w") as f:
            hosts = {"hosts": [host]}
            json.dump(hosts, f)
    else:
        with open(hosts_file_path, "r") as f:
            hosts_list = json.load(f)
            hosts_list["hosts"].append(host)
        with open(hosts_file_path, "w") as f:
            json.dump(hosts_list, f)


def remove_host(host):
    hosts_file_path = os.path.expanduser("~") + "/okserver/list.json"
    if os.path.exists(hosts_file_path):
        with open(hosts_file_path, "r") as f:
            hosts_list = json.load(f)
        try:
            hosts_list["hosts"].remove(host)
        except ValueError:
            print("Host not found")
            return
        with open(hosts_file_path, "w") as f:
            json.dump(hosts_list, f)


def check_hosts():
    hosts_file_path = os.path.expanduser("~") + "/okserver/list.json"
    if os.path.exists(hosts_file_path):
        with open(hosts_file_path) as f:
            hosts_list = json.load(f)["hosts"]
        status = {}
        for host in hosts_list:
            if ping3.ping(host) is False:
                print(f"Host {host} is not responding")
                status[host] = "down"
            else:
                print(f"Host {host} is responding")
                status[host] = "up"
        with open(os.path.expanduser("~") + "/okserver/status.json", "w") as f:
            json.dump(status, f)
        generate_html()
    else:
        print("No hosts are being monitored")
        print("Use the 'add' command to add a host to the list")


def generate_html():
    status_file_path = os.path.expanduser("~") + "/okserver/status.json"
    if os.path.exists(status_file_path):
        with open(status_file_path) as f:
            server
