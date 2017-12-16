import craw_utils as craw_u
from bs4 import BeautifulSoup
def get_main_data():
    url = "http://quote.stockstar.com/stock/industry_a.shtml"
    html = craw_u.getBrowserHtml(url)
    soup = BeautifulSoup(html,"html.parser")
    bodys = soup.find_all(id="datalist")
    dls = soup.find_all("dl","open")
    if len(dls)>0:
        aas = dls[0].find_all("a")
        for a in aas:
            print(a['href'])
    if len(bodys)>0:
        print("the len of bodys ",len(bodys))
        trs = bodys[0].find_all("tr")
        datas = []
        for tr in trs:
            tds = tr.find_all("td")
            data = []
            for td in tds:
                aas = td.find_all("a")
                url = None
                for a in aas:
                    url = a['href']
                text = td.text.replace(" ",'').replace("\n",'').replace("\0xa","")
                if url is not None:
                    #print(url+" "+text)
                    data.append(url+" "+text)
                else:
                    #print(text)
                    data.append(text)
            datas.append(data)
        print(datas)
def get_all_urls():
    url = "http://quote.stockstar.com/stock/industry.shtml"
    browser = craw_u.getBrowser(url)


