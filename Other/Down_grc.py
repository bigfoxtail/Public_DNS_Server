# !/usr/bin/python
# -*- coding: utf-8 -*-

# download https://www.grc.com/dns/resources.htm
import os

import requests

r = requests.get("http://www.GRC.com/dns/resolvers.csv")

os.rename("DNS_list5.csv", "DNS_list5.bak.csv")  # 重命名
with open("DNS_list5.csv", "wb") as f:
    f.write(r.content)
