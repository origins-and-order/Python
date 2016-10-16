from dependencies import *


# TODO Cythonize code
class Crawler(object):

    # initialize variables for global use with threads
    def __init__(self):
        # self.scope = self.scope(seed)
        self.visited_urls = set()
        self.unvisited = list()
        self.threads = list()
        self.concurrent_state = False
        self.terminate = False
        self.domain = None
        self.graph = dict()

    # search within range of seed's domain
    # i.e. http://example.com/
    # restrict sites to example.com in url

    def scope(self, url):
        return '{uri.scheme}://{uri.netloc}/'.format(uri=urlparse(url))

    # begin traversing
    # implement breadth first search
    def search(self, url, restrict_domain=True, container=None):

        # for a narrow search result based on the root's domain
        # and the use for parallel programming
        # have the global variable domain be used in all threads
        # from root url given.
        #
        # i.e. http://example.com/foo/bar
        # restrict all searches to contain "http://example.com/"

        if restrict_domain and self.domain is None:
            self.domain = self.scope(url)

        # implementation of breadth first search

        # create queue, enqueue
        self.unvisited.append(url)

        # while queue not empty
        while self.unvisited and not self.terminate:

            vertex = self.unvisited.pop()

            # visit neighboring nodes
            for link in Hyperlinks(vertex).links:
                if not self.terminate:
                    if restrict_domain:
                        if self.domain in link and link not in self.visited_urls:
                            self.visited_urls.add(link)
                            self.unvisited.append(link)
                            # print link
                            # for ranker
                            if container:
                                container.add(link)

                    else:
                        self.visited_urls.add(link)
                        self.unvisited.append(link)

            stdout.write("\rRemaining links to visit: %d" % len(self.unvisited))
            stdout.flush()

        # once one crawler terminates,
        # flag will set to true to terminate other crawlers
        self.terminate = True

        # disconnect threads from main process
        if self.concurrent_state:

            f = open('status.txt', 'w')
            f.write('There are ' + str(threading.activeCount()) + ' active threads.')
            f.close()

            for thread in self.threads:
                # if thread.
                thread.exit()

            links = file('links.txt', 'w')

            for link in self.visited_urls:
                links.write(link+'\n')

            links.close()

        else:

            links = file('single_thread_links.txt', 'w')

            for link in self.visited_urls:
                links.write(link + '\n')

            links.close()


        # TODO use 8 threads to traverse (or find number of available CPU threads). Need global variables.
    def concurrent_search(self, root, thread_count, restrict_domain=True, container=None):

        # concurrent state flag for main crawler method
        self.concurrent_state = True

        def start_threads(count):
            time.sleep(1)
            print 'Starting threads.'
            for i in xrange(count):
                stdout.flush()
                t = threading.Thread(target=self.search, args=(root, restrict_domain, container))
                t.name = str(i+1)
                stdout.write("\rThread %s starting." % t.name)
                t.start()
                t.join()

        try:
            start_threads(thread_count)

        except TypeError:
            print 'Integer expected. Got %s.' % type(thread_count)
            # 2 ^ 2 * number of cores
            cpu_count = 2 ** (2 * multiprocessing.cpu_count())
            print 'Using ' + str(cpu_count) + ' threads.'
            start_threads(cpu_count)

    # urls must contain these keywords to visited
    def restrict(self, terms):
        pass

    # load file that has previous visited urls
    def visited(self, f):
        self.visited_urls = [url.strip('\n') for url in open(f).readlines()]

    # save crawler state from visiting and visited.
    def save_state(self):
        pass

    # return concurrent state of crawler
    def is_concurrent(self):
        return self.concurrent_state

    # kill crawler
    def kill(self):
        self.save_state()
        self.terminate = True
        pass

    # train crawler to analyze certain sites
    def train_crawler(self):
        pass

    # clear contents of crawler

    def clear(self):

        self.save_state()
        self.visited_urls = set()
        self.unvisited = list()

        for thread in self.threads:
            thread.exit()

    # rank each page based on number of edges that link to each node
    # node weight = number of sits it's connected to / number of sites from domain
    def ranker(self, root):

        print 'Pre-computing domain'

        # load vertices from links.txt (concurrent search)
        vertices = set(link.strip() for link in open('links.txt').xreadlines())

        # load vertices to not be visited
        self.visited_urls = vertices

        # load vertices to also be visited, visit neighbors
        self.concurrent_search(root, 1024, container=vertices)

        #
        print 'Number of vertices %d' % len(vertices)

        # pre-compute graph

        # get all vertices from graph




        # do calculations


    def __str__(self):
        pass

    def add_rule(self):
        pass