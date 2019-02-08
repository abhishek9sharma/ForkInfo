from flask import Flask, render_template,request,url_for,redirect
from GitHubRepo import Repository as repo
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<path:reponame>')
def forkedrepos(reponame):
    #commitinfodict ={}
    # for i in range(30):
    #     commitinfodict['repo'+str(random.randint(1,101))] = {'ahead': random.randint(1,101) , 'behind': random.randint(1,101)}
    #return render_template('forks.html', cuur_repo_list= commitinfodict)
    #print(reponame)
    repo_owner = reponame.split('/')[0]
    repoobj = repo(reponame)


    forked_repos = repoobj.getForkedRepos()
    if 'message' in repoobj.forkedrespjson:
        return render_template('apierror.html', curr_msg = repoobj.forkedrespjson)
    else:
        return render_template('forks.html', cuur_repo_list= repoobj.forkedrespjson, parent_user = repo_owner)
    #return render_template('forks.html', cuur_repo_list= repoobj.commitinfo)
 
@app.route('/forks', methods =['GET','POST'])
def forks():
    if(request.method == "GET"):
         return "Please submit the form direct get not allowed"
    else:
        repoin = request.form.get('repo')
        return redirect(url_for('forkedrepos',reponame=repoin))

    