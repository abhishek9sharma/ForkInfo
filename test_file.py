from GitHubRepo import Repository as repo
import json
repoobj = repo('abhishek9sharma/EASE17Scripts')
#repoobj = repo('gcushen/hugo-academic')
#print(repoobj.forked_count)
repoobj.getForkedRepos()
#print(repoobj.forkedrespjson)
#for k in repoobj.commitinfo:
#    print(repoobj.commitinfo[k])
#print(json.dumps(repoobj.f:orkedrespjson,indent=4, sort_keys=True))
for k in repoobj.forkedrespjson:
    print(k['full_name'], k['ahead'] , k['behind'], k['files_ahead'], k['files_behind'])