DNSClient.py
import dns.resolver

# Set the IP address of the local DNS server and a public DNS server
local_host_ip = '127.0.0.1'
real_name_server = '8.8.8.8'  # Google's public DNS server

# Create a list of domain names to query - use the same list from the DNS Server
domainList = ['example.com.', 'safebank.com.', 'google.com.', 'nyu.edu.', 'legitsite.com.']

def query_local_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [local_host_ip]
    answers = resolver.resolve(domain, question_type)
    ip_address = answers[0].to_text()
    return ip_address

def query_dns_server(domain, question_type):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = [real_name_server]
    answers = resolver.resolve(domain, question_type)
    ip_address = answers[0].to_text()
    return ip_address

def compare_dns_servers(domainList, question_type):
    for domain_name in domainList:
        local_ip_address = query_local_dns_server(domain_name, question_type)
        public_ip_address = query_dns_server(domain_name, question_type)
        if local_ip_address != public_ip_address:
            return False
    return True

def local_external_DNS_output(question_type):
    print("Local DNS Server")
    for domain_name in domainList:
        ip_address = query_local_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")
    print("\nPublic DNS Server")
    for domain_name in domainList:
        ip_address = query_dns_server(domain_name, question_type)
        print(f"The IP address of {domain_name} is {ip_address}")

def exfiltrate_info(???, ???):  # testing method for part 2
    data = query_local_dns_server(???, ???)
    return data

if __name__ == '__main__':
    question_type = 'A'
    #local_external_DNS_output(question_type)
    result = compare_dns_servers(domainList, question_type)
    result = query_local_dns_server('nyu.edu.', question_type)
    print(result)
    #print(exfiltrate_info())