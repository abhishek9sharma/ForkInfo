from flask import Flask, render_template,request,url_for,redirect
from flask_bootstrap import Bootstrap
from GitHubRepo import Repository as repo
import random

app = Flask(__name__)
Bootstrap(app)
#app.url_map.strict_slashes = False

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<path:reponame>')
def forkedrepos(reponame):
    #commitinfodict ={}
    # for i in range(30):
    #     commitinfodict['repo'+str(random.randint(1,101))] = {'ahead': random.randint(1,101) , 'behind': random.randint(1,101)}
    #return render_template('forks.html', cuur_repo_list= commitinfodict)
    repoobj = repo(reponame)
    forked_repos = repoobj.getForkedRepos()
    print(repoobj.commitinfo)
    return render_template('forks.html', cuur_repo_list= repoobj.commitinfo)
 
@app.route('/forks', methods =['GET','POST'])
def forks():
    if(request.method == "GET"):
         return "Please submit the form direct get not allowed"
    else:
        repoin = request.form.get('repo')
        return redirect(url_for('forkedrepos',reponame=repoin))

    