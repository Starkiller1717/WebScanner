(venv) user@Term-Project:~/offsec-framework/sample_outputs$ cat report.md
# Automated Security Assessment Report

## Target: 127.0.0.1

## Network Scan (Nmap)
Starting Nmap 7.80 ( https://nmap.org ) at 2026-03-24 15:48 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00049s latency).
Not shown: 999 closed ports
PORT    STATE SERVICE VERSION
631/tcp open  ipp     CUPS 2.4

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 7.52 seconds

## Whois Information

#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#


NetRange:       127.0.0.0 - 127.255.255.255
CIDR:           127.0.0.0/8
NetName:        SPECIAL-IPV4-LOOPBACK-IANA-RESERVED
NetHandle:      NET-127-0-0-0-1
Parent:          ()
NetType:        IANA Special Use
OriginAS:       
Organization:   Internet Assigned Numbers Authority (IANA)
RegDate:        
Updated:        2024-05-24
Comment:        Addresses starting with "127." are used when one program needs to talk to another program running on the same machine using the Internet 
Comment:        Protocol.  127.0.0.1 is the most commonly used address and is called the "loopback" address.
Comment:        
Comment:        These addresses were assigned by the IETF, the organization that develops Internet protocols, in the Standard document, RFC 1122, which can  
Comment:        be found here:
Comment:        http://datatracker.ietf.org/doc/rfc1122
Ref:            https://rdap.arin.net/registry/ip/127.0.0.0



OrgName:        Internet Assigned Numbers Authority
OrgId:          IANA
Address:        12025 Waterfront Drive
Address:        Suite 300
City:           Los Angeles
StateProv:      CA
PostalCode:     90292
Country:        US
RegDate:        
Updated:        2024-05-24
Ref:            https://rdap.arin.net/registry/entity/IANA


OrgTechHandle: IANA-IP-ARIN
OrgTechName:   ICANN
OrgTechPhone:  +1-310-301-5820 
OrgTechEmail:  abuse@iana.org
OrgTechRef:    https://rdap.arin.net/registry/entity/IANA-IP-ARIN

OrgAbuseHandle: IANA-IP-ARIN
OrgAbuseName:   ICANN
OrgAbusePhone:  +1-310-301-5820 
OrgAbuseEmail:  abuse@iana.org
OrgAbuseRef:    https://rdap.arin.net/registry/entity/IANA-IP-ARIN


#
# ARIN WHOIS data and services are subject to the Terms of Use
# available at: https://www.arin.net/resources/registry/whois/tou/
#
# If you see inaccuracies in the results, please report at
# https://www.arin.net/resources/registry/whois/inaccuracy_reporting/
#
# Copyright 1997-2026, American Registry for Internet Numbers, Ltd.
#


## DNS Information

; <<>> DiG 9.18.39-0ubuntu0.22.04.2-Ubuntu <<>> 127.0.0.1
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NXDOMAIN, id: 54642
;; flags: qr rd ra; QUERY: 1, ANSWER: 0, AUTHORITY: 1, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;127.0.0.1.			IN	A

;; AUTHORITY SECTION:
.			5	IN	SOA	a.root-servers.net. nstld.verisign-grs.com. 2026032401 1800 900 604800 86400

;; Query time: 34 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Tue Mar 24 15:48:13 EDT 2026
;; MSG SIZE  rcvd: 113

(venv) user@Term-Project:~/offsec-framework/sample_outputs$ 
