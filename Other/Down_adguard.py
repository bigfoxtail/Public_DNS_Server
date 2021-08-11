# !/usr/bin/python
# -*- coding: utf-8 -*-

# download https://kb.adguard.com/en/general/dns-providers
import os

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
    url = 'https://kb.adguard.com/en/general/dns-providers'
    res = rs.get(url, headers=headers)
    selector = etree.HTML(res.text)
    content_list = selector.xpath("//div[@id='body-inner']/table/tbody")
    os.rename("DNS_list2.csv", "DNS_list2.bak.csv")  # 重命名
    with open("DNS_list2.csv", 'w', encoding='UTF-8') as f:
        f.writelines(
            '"Title1","Title2","IPV4","IPV6","DoH","DoT","Other"' +
            "\n")
        h3title = ""
        h4title = ""
        for n in range(len(content_list)):
            titlelist = []
            titlelist.append(content_list[n].xpath("../preceding-sibling::*[4]")[0])
            titlelist.append(content_list[n].xpath("../preceding-sibling::*[3]")[0])
            titlelist.append(content_list[n].xpath("../preceding-sibling::*[2]")[0])
            titlelist.append(content_list[n].xpath("../preceding-sibling::*[1]")[0])
            for title in titlelist:
                if title.tag == 'h3':
                    h3title = '"' + title.xpath("string(.)") + '"'
                if title.tag == 'h4':
                    h4title = '"' + title.xpath("string(.)") + '"'
            contents = content_list[n].xpath(".//tr")
            IPV4 = ""
            IPV6 = ""
            DoH = ""
            DoT = ""
            Other = ""
            for content in contents:
                Protocol = ' '.join(content.xpath('.//td[1]//text()'))
                Address = ' '.join(content.xpath('.//td[2]/code/text()'))
                if "DNS IPv4" in Protocol or "DNS, IPv4" in Protocol:
                    IPV4 = IPV4 + Address + " "
                elif "DNS IPv6" in Protocol or "DNS, IPv6" in Protocol:
                    IPV6 = IPV6 + Address + " "
                elif "DNS-over-HTTPS" in Protocol:
                    DoH = DoH + Address + " "
                elif "DNS-over-TLS" in Protocol:
                    DoT = DoT + Address + " "
                else:
                    Other = Other + Protocol + ":" + Address + " "

            IPV4 = '"' + IPV4 + '"'
            IPV6 = '"' + IPV6 + '"'
            DoH = '"' + DoH + '"'
            DoT = '"' + DoT + '"'
            Other = '"' + Other + '"'
            f.writelines(h3title + "," +
                         h4title + "," +
                         IPV4 + "," +
                         IPV6 + "," +
                         DoH + "," +
                         DoT + "," +
                         Other + "\n")
            print(h3title + "," +
                  h4title + "," +
                  IPV4 + "," +
                  IPV6 + "," +
                  DoH + "," +
                  DoT + "," +
                  Other + "\n")


if __name__ == '__main__':
    download_dns()
