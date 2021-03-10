import unittest
from github_api import get_git_info

class test_github_api(unittest.TestCase):

    def test_invalidInput(self):
        self.assertEqual(get_git_info("Angelina-Zaccari"),"User not found")
    def test_my_github(self):
        self.assertEqual(get_git_info("Angelina-Zaccaria"),['Repo: Angelina-Zaccaria.github.io Number of commits: 8', 'Repo: BeeEat Number of commits: 30', 'Repo: ButterflyBot Number of commits: 30', 'Repo: Complexity Number of commits: 30', 'Repo: linux-4.9-azaccari2 Number of commits: 4', 'Repo: osddemo Number of commits: 1', 'Repo: sds1910 Number of commits: 23', 'Repo: SSW-567 Number of commits: 14)'])
    def test_example_github(self):
        self.assertEqual(get_git_info("richkempinski"),['Repo: csp Number of commits: 2', 'Repo: hellogitworld Number of commits: 30', 'Repo: helloworld Number of commits: 6', 'Repo: Mocks Number of commits: 2', 'Repo: Project1 Number of commits: 2', 'Repo: richkempinski.github.io Number of commits: 2', 'Repo: threads-of-life Number of commits: 2', 'Repo: try_nbdev Number of commits: 2', 'Repo: try_nbdev2 Number of commits: 2'])
    
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
