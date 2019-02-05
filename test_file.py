from GitHubRepo import Repository as repo
repoobj = repo('abhishek9sharma/EASE17Scripts')
print(repoobj.repoinfoJSON['forks_count'])
forked_repos = repoobj.getForkedRepos()
for k in repoobj.commitinfo:
    print(repoobj.commitinfo[k])
