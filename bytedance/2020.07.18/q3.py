import re

def if_valid(url):
    pattern = "^([hH][tT]{2}[pP]://|[hH][tT]{2}[pP][sS]://|[fF][tT][pP]://)(([A-Za-z0-9-~]+).)+([A-Za-z0-9-~\\/])+$"

    m = re.match(pattern, url)

    if not m:
        return 'Invalid'

    else:
        return (url.split('/')[2])


if __name__ == '__main__':
    ls = []
    ls.append('http://www.baidu.com')
    ls.append('')
    for url in ls:
        print(if_valid(url))
