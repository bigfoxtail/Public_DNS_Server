# !/usr/bin/python
# -*- coding: utf-8 -*-

# download https://dnschecker.org/public-dns/
import os
import time
from lxml import etree
import requests


def download_dns():
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-language": "zh-CN,zh;q=0.9,zh-Hans;q=0.8,und;q=0.7",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "sec-gpc": "1",
        "upgrade-insecure-requests": "1",
        "referrer": "https://dnschecker.org/public-dns",
    }

    rs = requests.session()
    url = 'https://dnschecker.org/public-dns'
    res = rs.get(url, headers=headers)
    selector = etree.HTML(res.text)
    country_list = selector.xpath("//ul[@class='countries_list']//@href")
    os.rename("DNS_list1.csv", "DNS_list1.bak.csv")  # 重命名
    with open("DNS_list1.csv", 'w', encoding='UTF-8') as f:
        f.writelines(
            '"countryname","IPAddress","DNSDOMAIN","Location","ASNNumber","SoftwareVersion","DNSSEC","Reliability"' +
            "\n")
        for country_url in country_list:
            res = rs.get(country_url, headers=headers)
            selector = etree.HTML(res.text)
            dnslist = selector.xpath("//div[@class='table-responsive']/table/tbody/tr")
            CountryName = "\"" + selector.xpath("//li[@class='list-group-item']/p/strong/text()")[0] + "\""
            for dns in dnslist:
                IPAddress = "\"" + dns.xpath('./td[1]//text()')[0] + "\""
                DNSDOMAIN = "\"" + ''.join(dns.xpath('./td[1]//text()')[1:]) + "\""
                Location = "\"" + ' '.join(dns.xpath('./td[2]/text()')) + "\""
                ASNNumber = "\"" + ' '.join(dns.xpath('./td[3]//text()')).replace("\"", " ") + "\""
                SoftwareVersion = "\"" + ' '.join(dns.xpath('./td[4]/text()')) + "\""
                DNSSEC = "\"" + ' '.join(dns.xpath('./td[5]/text()')) + "\""
                Reliability = "\"" + ' '.join(dns.xpath('./td[6]/text()')) + "\""
                f.writelines(CountryName + "," +
                             IPAddress + "," +
                             DNSDOMAIN + "," +
                             Location + "," +
                             ASNNumber + "," +
                             SoftwareVersion + "," +
                             DNSSEC + "," +
                             Reliability + "\n")
                print(CountryName + "," +
                      IPAddress + "," +
                      DNSDOMAIN + "," +
                      Location + "," +
                      ASNNumber + "," +
                      SoftwareVersion + "," +
                      DNSSEC + "," +
                      Reliability)
            time.sleep(2)
            # exit()


if __name__ == '__main__':
    download_dns()
