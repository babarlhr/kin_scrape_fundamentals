from lxml import etree

tree = etree.parse("fundamentals/src/web_page.html")
title_element = tree.find("head/title")
print(title_element.text)

p_element = tree.find("body/p")
print(p_element.text)

list_items = tree.findall("body/ul/li")
for li in list_items:
    a = li.find("a")
    if a is not None:
        print(f'{li.text.strip()} {a.text}')
    else:    
        print(f'{li.text}')