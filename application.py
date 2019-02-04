from flask import Flask, render_template,request
from flask_session import Session
from GitHubRepo import Repository as repo

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/<path:reponame>', methods =['GET','POST'])
def forkedrepos(reponame):
    #print(reponame)
    #repoinput = repo(reponame)
    #forked_count = repoinput.repoinfoJSON['forks_count']
    #return f"{reponame}, has been forked, {forked_count}, times "
    if request.method=='GET':
        return f"<h1>Finding forks for :{reponame}</h1>"
    else:
        reponame = request.form.get('name')
        return f"<h1>Finding forks for :{reponame}</h1>"


@app.route('/displayforks')
def displayforks():
    return render_template('forks.html')
    