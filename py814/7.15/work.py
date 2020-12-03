import re
numRegex = re.compile(r'\d+')
print(numRegex.sub('X','12 drummers,11 pipers,five rings,3 hens'))

n1Regex = re.compile(r'^\d{1,3}(?:,\d{3})*$')    #?: 意思是不捕获括号内匹配到的数据
text='''
42
1,234
6,456,789
12,23,567
1234
'''
result=n1Regex.findall('4,566,123')
print(result)
mo = n1Regex.search('4,566,123')

n2Regex = re.compile(r'^\d{1,3}(,\d{3})*$')
result1 = n2Regex.match('4,566,123')
print(result1.group())