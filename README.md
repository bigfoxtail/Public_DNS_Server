# Public DNS Server



| DNSName                                                      | IPv4FirstChoice | IPv4Alternative | IPv6FirstChoice            | IPv6Alternative                        |
| ------------------------------------------------------------ | --------------- | --------------- | -------------------------- | -------------------------------------- |
| Cloudflare DNS                                               | 1.1.1.1         | 1.0.0.1         | 2606:4700:4700::1111       | 2606:4700:4700::1001                   |
| Cloudflare DNS  Malware Blocking Only                        | 1.1.1.2         | 1.0.0.2         | 2606:4700:4700::1112       | 2606:4700:4700::1002                   |
| Cloudflare DNS  Malware and Adult Content Blocking Together  | 1.1.1.3         | 1.0.0.3         | 2606:4700:4700::1113       | 2606:4700:4700::1003                   |
| Cloudflare  DNS64                                            |                 |                 | 2606:4700:4700::64         | 2606:4700:4700::6400                   |
| Google Public  DNS                                           | 8.8.8.8         | 8.8.4.4         | 2001:4860:4860::8888       | 2001:4860:4860::8844                   |
| Google Public  DNS64                                         |                 |                 | 2001:4860:4860::6464       | 2001:4860:4860::64                     |
| Quad9 DNS  Standard                                          | 9.9.9.9         | 149.112.112.112 | 2620:fe::fe                | 2620:fe::fe:9                          |
| Quad9 DNS  Unsecured                                         | 9.9.9.10        | 149.112.112.10  | 2620:fe::10                | 2620:fe::fe:10                         |
| Quad9 DNS ECS  support                                       | 9.9.9.11        | 149.112.112.11  | 2620:fe::11                | 2620:fe::fe:11                         |
| Cisco OpenDNS  Standard                                      | 208.67.222.222  | 208.67.220.220  | 2620:119:35::35            | 2620:119:53::53                        |
| Cisco OpenDNS  FamilyShield                                  | 208.67.222.123  | 208.67.220.123  | 2620:119:53::123           | 2620:119:35::123                       |
| Cisco OpenDNS  DNS64                                         |                 |                 | 2620:0:ccc::2              | 2620:0:ccd::2                          |
| AdGuard DNS  Default                                         | 94.140.14.14    | 94.140.15.15    | 2a10:50c0::ad1:ff          | 2a10:50c0::ad2:ff                      |
| AdGuard DNS  Default (can block ads, tracking and phishing URLs) | 176.103.130.130 | 176.103.130.131 | 2a00:5a60::ad1:0ff         | 2a00:5a60::ad2:0ff                     |
| AdGuard DNS  Family Protection                               | 94.140.14.15    | 94.140.15.16    | 2a10:50c0::bad1:ff         | 2a10:50c0::bad2:ff                     |
| AdGuard DNS  Family protection (default + block adult sites + safe search) | 176.103.130.132 | 176.103.130.134 | 2a00:5a60::bad1:0ff        | 2a00:5a60::bad2:0ff                    |
| AdGuard DNS  Non-filtering                                   | 94.140.14.140   | 94.140.14.141   | 2a10:50c0::1:ff            | 2a10:50c0::2:ff                        |
| CleanBrowsing  Adult Filter                                  | 185.228.168.10  | 185.228.169.11  | 2a0d:2a00:1::1             | 2a0d:2a00:2::1                         |
| CleanBrowsing  Security Filter                               | 185.228.168.9   | 185.228.169.9   | 2a0d:2a00:1::2             | 2a0d:2a00:2::2                         |
| CleanBrowsing  Family Filter                                 | 185.228.168.168 | 185.228.169.168 | 2a0d:2a00:1::              | 2a0d:2a00:2::                          |
| (Neustar)  (Verisign) (UltraDNS) Public DNS                  | 64.6.64.6       | 64.6.65.6       | 2620:74:1b::1:1            | 2620:74:1c::2:2                        |
| (Neustar)  (Verisign) (UltraDNS) Public DNS Threat Protection | 156.154.70.2    | 156.154.71.2    | 2610:a1:1018::2            | 2610:a1:1019::2                        |
| (Neustar)  (Verisign) (UltraDNS) Public DNS Family Secure    | 156.154.70.3    | 156.154.71.3    | 2610:a1:1018::3            | 2610:a1:1019::3                        |
| Comodo DNS                                                   | 8.26.56.26      | 8.20.247.20     |                            |                                        |
| Comodo Secure  Internet Gateway                              | 8.26.56.10      | 8.20.247.10     |                            |                                        |
| Norton  Security                                             | 199.85.126.10   | 199.85.127.10   |                            |                                        |
| Norton  Security + Pornography                               | 199.85.126.20   | 199.85.127.20   |                            |                                        |
| Norton  Security + Pornography + Other                       | 199.85.126.30   | 199.85.127.30   |                            |                                        |
| OneDNS Block  Edition                                        | 117.50.11.11    | 52.80.66.66     |                            |                                        |
| OneDNS Home  Edition                                         | 117.50.60.30    | 52.80.60.30     |                            |                                        |
| OneDNS Pure  Edition                                         | 117.50.10.10    | 52.80.52.52     |                            |                                        |
| dns.watch                                                    | 84.200.69.80    | 84.200.70.40    | 2001:1608:10:25::1c04:b12f | 2001:1608:10:25::9249:d69b             |
| DNS.SB PumpleX  server                                       | 185.222.222.222 | 45.11.45.11     | 2a09::                     | 2a09::1                                |
| Dyn DNS                                                      | 216.146.35.35   | 216.146.36.36   |                            |                                        |
| 114 DNS  Regular public DNS (clean and no hijacking)         | 114.114.114.114 | 114.114.115.115 |                            |                                        |
| 114 DNS Block  phishing virus Trojan sites (protect online security) | 114.114.114.119 | 114.114.115.119 |                            |                                        |
| 114 DNS Block  pornographic sites (protect children)         | 114.114.114.110 | 114.114.115.110 |                            |                                        |
| AliDNS DNS                                                   | 223.5.5.5       | 223.6.6.6       | 2400:3200::1               | 2400:3200:baba::1                      |
| Baidu BaiduDNS                                               | 180.76.76.76    |                 | 2400:da00::6666            |                                        |
| DNSPod  (Tencent) DNS                                        | 119.29.29.29    |                 | 2402:4e00::                |                                        |
| 360 (dnspai)  Secure DNS Telecom/Mobile/Railway              | 101.226.4.6     | 218.30.118.6    |                            |                                        |
| 360 (dnspai)  Secure DNS Unicom                              | 123.125.81.6    | 140.207.198.6   |                            |                                        |
| CNNIC sDNS                                                   | 1.2.4.8         | 210.2.4.8       |                            |                                        |
| China's CFIEC  Public DNS                                    |                 |                 | 240C::6666                 | 240C::6644                             |
| Yandex Basic                                                 | 77.88.8.8       | 77.88.8.1       | 2a02:6b8::feed:0ff         | 2a02:6b8:0:1::feed:0ff                 |
| Yandex Safe                                                  | 77.88.8.88      | 77.88.8.2       | 2a02:6b8::feed:bad         | 2a02:6b8:0:1::feed:bad                 |
| Yandex Family                                                | 77.88.8.7       | 77.88.8.3       | 2a02:6b8::feed:a11         | 2a02:6b8:0:1::feed:a11                 |
| Netherlands  Freenom World Public DNS                        | 80.80.80.80     | 80.80.81.81     |                            |                                        |
| UncensoredDNS                                                | 91.239.100.100  | 89.233.43.71    | 2001:67c:28a4::            | 2a01:3a0:53:53::                       |
| SkyDNS RU ECS  support                                       | 193.58.251.251  |                 |                            |                                        |
| CIRA Canadian  Shield DNS Private                            | 149.112.121.10  | 149.112.122.10  | 2620:10A:80BB::10          | 2620:10A:80BC::10                      |
| CIRA Canadian  Shield DNS Protected                          | 149.112.121.20  | 149.112.122.20  | 2620:10A:80BB::20          | 2620:10A:80BC::20                      |
| CIRA Canadian  Shield DNS Family                             | 149.112.121.30  | 149.112.122.30  | 2620:10A:80BB::30          | 2620:10A:80BC::30                      |
| DNS for Family  Germany DNS Server                           | 94.130.180.225  | 78.47.64.161    | 2a01:4f8:1c0c:40db::1      | 2a01:4f8:1c17:4df8::1                  |
| CZ.NIC ODVR  Germany DNS Server                              | 193.17.47.1     | 185.43.135.1    | 2001:148f:ffff::1          | 2001:148f:fffe::1                      |
| SafeSurfer DNS  PumpleX server                               | 104.155.237.225 | 104.197.28.121  |                            |                                        |
| puntCAT DNS                                                  | 109.69.8.51     |                 | 2a00:1508:0:4::9           |                                        |
| SafeDNS                                                      | 195.46.39.39    | 195.46.39.40    |                            |                                        |
| Alternate DNS                                                | 76.76.19.19     | 76.223.122.150  | 2602:fcbc::ad              | 2001:4800:780e:510:a8cf:392e:ff04:8982 |

