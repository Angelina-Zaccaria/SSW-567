import requests
import json

#  input a GitHub user ID. 
#  output list of the names of the repositories that the user has, along with the number of commits that are in each of the listed repositories
def get_git_info(userID):
    user_response = requests.get("https://api.github.com/users/"+str(userID)+"/repos")
    if user_response.status_code == 404:
        return "User not found"
    user_data = user_response.json()
    repos = []
    for repo in user_data:
        repo_response = requests.get("https://api.github.com/repos/"+str(userID)+"/"+str(repo["name"])+"/commits")
        repo_data = repo_response.json()
        repos.append("Repo: " + str(repo["name"]) + " Number of commits: " + str(len(repo_data)))
    return repos

def stringify_repos(repos):
    return "\n".join(repos)

# print(stringify_repos(get_git_info("Angelina-Zaccaria")))
# print(get_git_info("richkempinski"))