import requests
res = []
response = requests.get('https://coinmarketcap.com/')
response_text = response.text

response_parse = response_text.split('<span>')
for parse_elem1 in response_parse:
    if parse_elem1.startswith('$'):
        for parse_elem2 in parse_elem1.split('</span>'):
            if parse_elem2.startswith('$') and parse_elem2[1].isdigit():
                res.append(parse_elem2)
print(res[0])
