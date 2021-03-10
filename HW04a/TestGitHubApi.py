import unittest
from GitHubApi import get_git_info

class test_github_api(unittest.TestCase):

    def test_invalidInput(self):
        self.assertEqual(get_git_info("Angelina-Zaccari"),"User not found")
    def test_my_github(self):
        # just testing the first one since this the commits increment on my public 567 repo
        self.assertEqual(get_git_info("Angelina-Zaccaria")[0],'Repo: Angelina-Zaccaria.github.io Number of commits: 8')
    def test_example_github(self):
        self.assertEqual(get_git_info("richkempinski"),['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 2', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 2', 'Repo: threads-of-life Number of commits: 2', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 2'])
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
