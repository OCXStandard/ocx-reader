from bs4 import BeautifulSoup

file = "napa-ocx_M8.3docx"
schema = "OCX_Schema.xsd"

with open(file, "r") as f:
    xml_data = f.read()
soup = BeautifulSoup(xml_data, features="xml")

root = soup.find()
print(root.name)  # ocxXML

elements = soup.find_all('Panel')
for element in elements:
    attributes = element.attrs
    print(attributes)
