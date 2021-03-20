import unittest
from unittest.mock import Mock, patch
# import json
# from GitHubApi import get_git_info
import GitHubApi

# @patch('GitHubApi.requests.get')
# def test_get_git_info(mock_get):
#     # if mock_get == "Angelina-Zaccari":
#     mock_get.status_code = 404

# def mocked_requests_get(*args, **kwargs):
#     class MockResponse:
#         def __init__(self, text, status_code):
#             self.text = text
#             self.status_code = status_code

#         def json(self):
#             return json.dumps(self.text)

#     if args[0] == "https://api.github.com/users/Angelina-Zaccaria/repos":
#         with open('repos.txt', 'r') as file:
#             repos = file.read().replace('\n', '')
#         print(repos)
#         return MockResponse(repos, 0)
#     if args[0] == "https://api.github.com/repos/Angelina-Zaccaria/Angelina-Zaccaria.github.io/commits":
#         with open('commits.txt', 'r') as file:
#             commits = file.read().replace('\n', '')
#         print(commits)
#         return MockResponse(commits, 0)
#     # elif args[0] == 'https://api.github.com/users/richkempinski/repos':
#     #     return MockResponse({"key2": "value2"}, 200)

#     return MockResponse(None, 404)


class test_github_api(unittest.TestCase):
    
    @patch('GitHubApi.get_git_info')
    def test_invalidInput(self, mock_get_git_info):
        mock_get_git_info.return_value = "User not found"
        self.assertEqual(GitHubApi.get_git_info("Angelina-Zaccari"),"User not found")
    @patch('GitHubApi.get_git_info')
    def test_my_github(self, mock_get_git_info):
        # just testing the first one since this the commits increment on my public 567 repo
        mock_get_git_info.return_value = ['Repo: Angelina-Zaccaria.github.io Number of commits: 8']
        self.assertEqual(GitHubApi.get_git_info("Angelina-Zaccaria")[0],'Repo: Angelina-Zaccaria.github.io Number of commits: 8')
    @patch('GitHubApi.get_git_info')
    def test_example_github(self, mock_get_git_info):
        mock_get_git_info.return_value = ['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5']
        self.assertEqual(GitHubApi.get_git_info("richkempinski"),['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 10', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 9', 'Repo: threads-of-life Number of commits: 1', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 5'])
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
