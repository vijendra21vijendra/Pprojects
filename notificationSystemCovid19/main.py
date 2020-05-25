# this is notification system
from plyer import notification  # for notification
import requests
from bs4 import BeautifulSoup


def notifyMe(title, msg):
    notification.notify(
        title=title,
        message=msg,
        app_icon="./virus.ico",
        timeout=10
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    #notifyMe("vijendra", "let's stop the corona")
    url = "https://www.mohfw.gov.in/"
    myHtmlData = getData(url)
    soup = BeautifulSoup(myHtmlData, 'html.parser')
    soup.prettify()
    total = 0
    table = soup.find('table')
    # print(type(table))
    # print(table)
    cases = []
    myDataStr = ""
    for tr in table.find_all('tr'):
        myDataStr += tr.getText()
    itemList = myDataStr.split("\n\n")
    # print(tr.getText())
    # csp = []
    # for td in tr:
    #     csp.append(td)
    # cases.append(csp)

    # print(cases)
    # for table in soup.find_all('table'):
    #     # print(table.find_all('td'))
    #     # print(soup)
    #     # https://www.mohfw.gov.in/
    #     pass
    # print(len(itemList))
    # print(len(itemList[0]))
    x = itemList[0].split('\n')
    # print(len(x))
    # for p in x:
    #     print(p, end=' ')
    # print("sr.No\tname\t\t\t\t total\t cured\t deaths")
    itemList = itemList[1:35]
    totalCases = 0
    deaths = 0
    cured = 0
    # print(itemList[0][2])
    # print(itemList[0][3])
    for p in itemList:
        p = p.split('\n')
        totalCases += int(p[2])
        deaths += int(p[4])
        cured += int(p[3])
        # for k in p.split('\n'):
        #     if(len(k) > 10):
        #         print(k.split(' ')[0], end='\t')
        #     else:
        #         print(k, end='\t')
        # print("")
    notifyData = "totalCases: " + \
        str(totalCases) + "\ncured: "+str(cured) + "\nacitive" + \
        str((totalCases-cured-deaths)) + "\ndeaths: " + str(deaths)
    print(notifyData)
    notifyMe("vijendra singh see it", notifyData)
