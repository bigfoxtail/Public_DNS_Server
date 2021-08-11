# !/usr/bin/python
# -*- coding: utf-8 -*-

# download https://public-dns.info/
import os

import requests

r = requests.get("https://public-dns.info/nameservers-all.csv")

os.rename("DNS_list4.csv", "DNS_list4.bak.csv")  # 重命名
with open("DNS_list4.csv", "wb") as f:
    f.write(r.content)
