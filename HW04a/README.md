# Homework 05a - Isolate External Dependencies
[![build status of master](https://travis-ci.org/Angelina-Zaccaria/SSW-567.svg?branch=HW05a_Mocking)](https://travis-ci.org/Angelina-Zaccaria/SSW-567)

# Homework 04a - Develop with the Perspective of the Tester in mind
[![build status of master](https://travis-ci.org/Angelina-Zaccaria/SSW-567.svg?branch=master)](https://travis-ci.org/Angelina-Zaccaria/SSW-567)

When designing the code, something I did to make it easier to test was separate out the function that displayed the information for each repo on a separate line. This made it so I could make the unit tests compare to a list of repo info rather than one long string. It was also important to include the edge case of when a user ID is not valid and so the API returns a 404 error. Additionally, I had to make sure to use return for all functions rather than print so that I could use the return values in my unit tests.

The main challenge I faced when testing this assignment was the API request limit. After hitting the limit locally, I was able to use Travis CI to continue testing, but that quickly hit the limit as well. My first mistake was that I was using my own username for one of the unit tests and of course the commit number for this repo incremented every time I committed so it kept failing that unit test, which I fixed by just comparing the info for the first repo on the list which is a few years old. My second mistake was that the commit count that I was comparing for some of `richkempinski`'s later repos were incorrect because I evidently hit the API call limit halfway through my last run when I separated out `stringify_repos`, so I ended up checking for 2 commits even though it was really just that there were 2 items in the json data for the rate limit message.

Overall, having the mindset of a tester when developing is very beneficial because you end up writing cleaner, more testable code, and it is something that I will keep in mind when developing in the future.
