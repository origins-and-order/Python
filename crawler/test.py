from Crawler import Crawler

# testing
url = 'http://www.utrgv.edu/en-us/admissions/paying-for-college/grants/index.htm'

# the born of the yung spidey, started so yung :')
spidey = Crawler.Crawler()

# lil spidey :)
spidey.search(url)

# okay, get the exterminator lmao
spidey.concurrent_search(url, 2048)

# rank how kool the pages r ;-O
# spidey.ranker(url)


# def test(container):
#     for i in range(10):
#         container.add(i)
#
# c = set()
# test(c)
# print c