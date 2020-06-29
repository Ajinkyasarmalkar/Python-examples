import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(txt[0:17])
print(x)