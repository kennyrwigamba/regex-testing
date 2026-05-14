import xml.etree.ElementTree as ET
import re

tree = ET.parse("modified_sms_v2.xml")
root = tree.getroot()

regex = re.compile(r'You have received (\d+) RWF')
total = 0

for sms in root.findall("sms"):
    body = sms.get("body")
    match = regex.search(body)
    if match:
        print(match.group(0))
        total += int(match.group(1))
        
print(f"Total: {total} RWF")