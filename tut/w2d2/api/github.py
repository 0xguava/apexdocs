
import requests as re
from flask import request
from secrets import secrets
from __main__ import app

class github_api:
    """
    weekly commit activity
    last year of commit activity
    all contributor commit activity
    """

    TOKEN = secrets['GITHUB']

    head = {
        'Accept' : 'application/vnd.github+json',
        'Authorization' : f"Bearer {TOKEN}",
        'X-GitHub-Api-Version' : '2022-11-28',
    }

    def get_stats(self, user, repo, stat):
        match stat:
            case 'weekly_commit': 
                stat = 'code_frequency'
            case 'year_of_commit':
                stat = 'commit_activity'
        url = f"https://api.github.com/repos/{user}/{repo}/stats/{stat}"
        stats = re.get(url, headers = self.head).json()
        return stats

git_analytics = github_api()

@app.get("/github")
def github():
    user = request.args.get('user')
    repo = request.args.get('repo')
    stat = request.args.get('stat')
    return git_analytics.get_stats(user, repo, stat)
