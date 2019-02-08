import requests
from bs4 import BeautifulSoup
from lxml import etree
import json
from multiprocessing.dummy import Pool


class Repository:
    def __init__(self,repopath):
        self.repopath = repopath
        self.githublink = 'https://github.com/'+repopath
        self.apilink = 'https://api.github.com/repos/' + repopath
        self.repoinfo = repopath.split('/')
     
        #self.repoinfoJSON = self.getRepInfoasJSON() 
        #self.forked_count = self.repoinfoJSON['forks_count']
    

    
    def scrapeRepoInfo(self,repoinfo):
        
        reponame = repoinfo['full_name']
        ownername = repoinfo['owner']['login']
        commitinfodict ={'ahead':-1, 'behind':-1, 'files_ahead':-1 ,'files_behind':-1}
        
        link='https://github.com/' + reponame
        repohtml = requests.get(link).text
        reposoup = BeautifulSoup(repohtml, 'lxml')
        diffinfo = reposoup.find('div', attrs={'class': 'branch-infobar'})


        try:
            diff_info_line = diffinfo.contents[-1].strip()
            for infokey in commitinfodict:
                if str(infokey) in diff_info_line:
                    commitinfodict[infokey] = diff_info_line.split(infokey)[0].split()[-2]
                else:
                    commitinfodict[infokey] = 0
        
        except:
            pass

        for k in commitinfodict:
             repoinfo[k] = commitinfodict[k]
        return repoinfo

    def getRepInfoasJSON(self):
        self.repoinfoJSON = requests.get(self.apilink).json()
        return self.repoinfoJSON
        #return self.repoinfoJSON

    def getForkedRepos(self):
        #print(self.apilink)
        self.forkedrespjson = requests.get(self.apilink+'/forks?sort=stargazers&per_page=100').json()
  
        
        if('message' in self.forkedrespjson):
            pass
        else: 
            self.repoowner =  self.repoinfo[0]
            self.reponame = self.repoinfo[1]
            with Pool(25) as p:
                forkedrespjsonitr = p.imap_unordered(self.scrapeRepoInfo,self.forkedrespjson)
                self.forkedrespjson = [repo for repo in forkedrespjsonitr if repo]
  
            # self.commitinfo ={}
            # for repoinfo in self.forkedrespjson:
            #     reponame = repoinfo['full_name']
            #     self.commitinfo[reponame]= self.scrapeRepoInfo('https://github.com/' + reponame)
            #     for k in self.commitinfo[reponame]:
            #         repoinfo[k] = self.commitinfo[reponame][k]



