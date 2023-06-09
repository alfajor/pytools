import sys
import nmap

# POC script-ify nmap scan
def usage():
    if len(sys.argv) < 2:
        print('Usage: {} <ip_addr>. Please supply an IP to scan'.format(sys.argv[0]))
        sys.exit(1)
usage()

def scanner():
    target = str(sys.argv[1])
    # common interesting ports
    target_ports = [21, 22, 443, 80, 8080]
    port_scanner = nmap.PortScanner()

    try:
        print('Scanning ports on: {}'.format(target))

        for port in target_ports: 
            active_scan = port_scanner.scan(target, str(port))
            port_state = active_scan['scan'][target]['tcp'][port]['state']

            print('Port {} is {}'.format(port, port_state))

        target_status = active_scan['scan'][target]['status']['state']
        print('{} is {}'.format(target, target_status))
    
    except Exception as err:
        print('There was a problem', err)

scanner()