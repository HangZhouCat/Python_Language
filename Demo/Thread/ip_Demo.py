import requests

def jiance():
    pass

def Main():
    with open('ip.txt') as ip_file:
        ip = ip_file.read()
        print(len(ip))
        ip_list = ip.split('\n')
        print(len(ip_list))
        for ip_port in ip_list:
            ip = ip_port.split(':')


if __name__ == '__main__':
    Main()