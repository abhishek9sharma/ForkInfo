from GitHubRepo import Repository as repo
import json
repoobj = repo('abhishek9sharma/EASE17Scripts')
#print(repoobj.forked_count)
repoobj.getForkedRepos()
for k in repoobj.commitinfo:
    print(repoobj.commitinfo[k])
#print(json.dumps(repoobj.forkedrespjson,indent=4, sort_keys=True))