# !/usr/bin/python
# -*- coding: utf-8 -*-

# download https://0xfab1.net/tech/standards/publicDNS/
import os

from lxml import etree, html
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
    url = 'https://0xfab1.net/tech/standards/publicDNS/'
    res = rs.get(url, headers=headers)
    selector = etree.HTML(res.text.replace('</br>', '<br>'))
    content_list = selector.xpath("//div[@class='md-content']//table/tbody")
    os.rename("DNS_list3.csv", "DNS_list3.bak.csv")  # 重命名
    with open("DNS_list3.csv", 'w', encoding='UTF-8') as f:
        contents = content_list[0]
        for br in contents.xpath(".//br"):
            br.tail = " " + br.tail if br.tail else " "
        f.writelines(
            '"Provider","IPv4","IPv6","DNSoverHTTPSandTLS"' +
            "\n")
        for content in contents:
            Provider = "\"" + ' '.join(content.xpath('.//td[1]//text()')) + "\""
            IPv4 = "\"" + ' '.join(content.xpath('.//td[2]/text()')) + "\""
            IPv6 = "\"" + ' '.join(content.xpath('.//td[3]/text()')) + "\""
            DNSoverHTTPSandTLS = "\"" + ' '.join(content.xpath('.//td[4]/text()')) + "\""
            f.writelines(Provider + "," +
                         IPv4 + "," +
                         IPv6 + "," +
                         DNSoverHTTPSandTLS + "\n")
            print(Provider + "," +
                  IPv4 + "," +
                  IPv6 + "," +
                  DNSoverHTTPSandTLS + "\n")


if __name__ == '__main__':
    download_dns()
