import requests
from bs4 import BeautifulSoup

''' Lines 7-33 were taken from:
https://stackoverflow.com/questions/37754138/how-to-render-html-with-pyqt5s-qwebengineview
'''
def render(url):
    """Fully render HTML, JavaScript and all."""

    import sys
    from PyQt5.QtCore import QEventLoop,QUrl
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtWebEngineWidgets import QWebEngineView

    class Render(QWebEngineView):
        def __init__(self, url):
            self.html = None
            self.app = QApplication(sys.argv)
            QWebEngineView.__init__(self)
            self.loadFinished.connect(self._loadFinished)
            self.load(QUrl(url))
            while self.html is None:
                self.app.processEvents(QEventLoop.ExcludeUserInputEvents | QEventLoop.ExcludeSocketNotifiers | QEventLoop.WaitForMoreEvents)
            self.app.quit()

        def _callable(self, data):
            self.html = data
            self.app.quit()

        def _loadFinished(self, result):
            self.page().toHtml(self._callable)

    return Render(url).html


def scrape():
    url = "https://tftactics.gg/tierlist/team-comps/"
    html = requests.get(url).text
    renderedHTML = render(url)
    soup = BeautifulSoup(renderedHTML,"html.parser")
    #Returns a list of all the team characters (use their hrefs to parse the names)
    teamCharacters = soup.find_all(class_="team-characters")
    preScrapeTeamNames = soup.find_all('div',{"class" : "team-name"})
    teamList = []
    tierList = []
    #iterate through all the names and only add S or A tier teams to the teamList
    for each in preScrapeTeamNames:
        name = each.text
        tier = name[:1]
        if tier != 'S' and tier != 'A':
            continue
        tierList.append(tier)
        newName = name[1:]
        teamList.append(newName)
    numOfTeamCharactersNeeded = len(teamList)
    preScrapeTeamCharactersAll = soup.find_all('div',{"class" : "team-characters"})
    preScrapeTeamCharactersStoA = preScrapeTeamCharactersAll[:numOfTeamCharactersNeeded]
    tierGroupSoup = soup.find_all("div",{"class" : "tier-group"})
    charactersFound = []
    for i in range(0,2):
        charactersListSoup = tierGroupSoup[i].find_all("div",{"class":"characters-list"})
        for j in charactersListSoup:
            teamPortraitSoup = j.find_all("div",{"class":"team-portrait"})
            for k in teamPortraitSoup:
                teamCharactersSoup = k.find("div",{"class":"team-characters"})
                imgSoup = teamCharactersSoup.find_all('img', alt=True)
                hrefSoup = teamCharactersSoup.find_all('a', href=True)
                team = []
                for img in imgSoup:
                    print(img["alt"])
                for p in hrefSoup:  
                    if p["href"] != "/item-builder":
                        name = p["href"]
                        splitName = name.split("/")
                        name = splitName[2]
                        team.append(name)
                charactersFound.append(team)

    teamDictionary = dict(zip(teamList, charactersFound))
    tierDictionary = dict(zip(teamList, tierList))

    return tierDictionary, teamDictionary
