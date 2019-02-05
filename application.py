from flask import Flask, render_template,request,url_for,redirect
from flask_session import Session
from GitHubRepo import Repository as repo

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<path:reponame>')
def forkedrepos(reponame):
    repoobj = repo(reponame)
    forked_repos = repoobj.getForkedRepos()
    info = ''
    for k in repoobj.commitinfo:
        info += repoobj.commitinfo[k]
    return info
    

@app.route('/forks', methods =['GET','POST'])
def forks():
    if(request.method == "GET"):
         return "Please submit the form direct get not allowed"
    else:
        repoin = request.form.get('repo')
        return redirect(url_for('forkedrepos',reponame=repoin))

    