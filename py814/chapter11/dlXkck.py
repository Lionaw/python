# Downloads every single XKCD comic.
import requests, os ,bs4

url = 'http://xkcd.com'               # starting url

os.makedirs('xkcd',exist_ok=True)     #store comics in ./xkcd
while not url.endswith('#'):
    #TODO:Download the page.
    print('Downloading page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    #TODO:Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
        print('Could not find comic image.')
    else:
        comicUrl = comicElem[0].get('src')
        if comicUrl[1] =='/':                   #src=后的解析地址不规范
            comicUrl='http:'+comicUrl
        else:
            comicUrl='http:/'+comicUrl
        #Download the image
        print('Downloading image %s...' % (comicUrl))
        headers={'Connextion':'close',}          #数据传输要保持TCP连接，为节省流量，默认为keep-alive，不能返回连接池
        res = requests.get(comicUrl,headers=headers)
        res.raise_for_status()

    #TODO:Save the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    #TODO:Get the Prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')

print('Done!')
