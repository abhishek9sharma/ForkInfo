import requests
from bs4 import BeautifulSoup
from lxml import etree

class Repository:
    def __init__(self,repopath):
        self.repopath = repopath
        self.githublink = 'https://github.com/'+repopath
        self.apilink = 'https://api.github.com/repos/' + repopath
        self.repoinfoJSON = self.getRepInfoasJSON() 
        self.forked_count = self.repoinfoJSON['forks_count']
    

    def scrapeRepoInfo(self,link):
        repohtml = requests.get(link).text
        reposoup = BeautifulSoup(repohtml, 'lxml')
        diffinfo = reposoup.find('div', attrs={'class': 'branch-infobar'})
        #forkinfo = reposoup.find()
        diff_info_line = diffinfo.contents[-1].strip()
        return diff_info_line

    def getRepInfoasJSON(self):
        return requests.get(self.apilink).json()
        #return self.repoinfoJSON

    def getForkedRepos(self):
        self.forkedrespjson = requests.get(self.apilink+'/forks')
        self.commitinfo ={}
        for repoinfo in self.forkedrespjson.json():
            reponame = repoinfo['full_name']
            self.commitinfo[reponame]= self.scrapeRepoInfo('https://github.com/' + reponame)



#repo = Repository('gcushen/hugo-academic')
#print("No of forks of main repo :" , repo.getRepInfoasJSON()['forks_count'])    
#print(repo.getForkedRepos())   
