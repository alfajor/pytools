# basic script for IP filtering from a sample log file
def ip_address_filter():
    log_directory = '../sample-logs'
    with open(log_directory + '/ip_addresses.txt', 'r') as file:
        text = file.read()
    ip_entries = text.split()

    remove_list = ['192.159.34.3', '192.255.12.0', '192.424.79.104']

    for item in remove_list:
        ip_entries.remove(item)

    updated_entries = " ".join(ip_entries)

    with open(log_directory + '/ip_addresses.txt', 'w') as file:
        file.write(updated_entries)

    print(updated_entries)
    return updated_entries

ip_address_filter()