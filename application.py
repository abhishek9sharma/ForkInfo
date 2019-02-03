from flask import Flask
from flask_session import Session
from GitHubRepo import Repository as repo

app = Flask(__name__)

@app.route("/")
def index():
    return "Enter the repository name in the format username/repo"

@app.route('/<string:reponame>')
def forkedrepos(reponame):
    print(reponame)
    return f"{reponame}, has been forked"
    #repoinput = repo(reponame)
    #return f"{reponame}, has been forked" + str(repoinput.repoinfoJSON['forks_count']) +" times "
