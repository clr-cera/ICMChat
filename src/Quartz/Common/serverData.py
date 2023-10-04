"""Here is all network data Management"""

import dns.resolver
from Quartz import DOMAIN, IP, IPTYPE, PORT


def getIP(domain: str, ip: str, iptype: str) -> str:
    '''This function receives a domain, an ip and an ip type (IPV6 or IPV4)
    if the ip is not empty, it returns the ip
    if the domain is not empty it resolves the domain
    else, it returns "localhost"'''

    if ip != "":
        return ip

    if domain != "":
        if iptype == "IPV6":
            return dns.resolver.resolve(domain, "AAAA")[0].to_text()

        elif iptype == "CNAME":
            indomain = dns.resolver.resolve(domain, "CNAME")[0].to_text()

            ip = dns.resolver.resolve(indomain, "A")[0].to_text()
            return ip

        else:
            return dns.resolver.resolve(domain, "A")[0].to_text()

    else:
        return "localhost"


HOST = getIP(DOMAIN, IP, IPTYPE)
PORT = PORT


if __name__ == "__main__":
    print(HOST)
