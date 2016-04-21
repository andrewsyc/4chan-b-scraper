from bs4 import BeautifulSoup
import urllib
import urllib2
import os

import time

start = time.time()

def get_threads(url, board, dir):


    response = urllib2.urlopen(url)
    soup = BeautifulSoup(response.read(), "lxml")

    links = soup.find_all("a", attrs={"class": "replylink"})

    for link in links:
        link_string = link['href']
        thread_id = link_string.split('/')
        print thread_id[1]
        thread_url = "http://boards.4chan.org/" + dir + "/thread/" + thread_id[1]
        thread_response = urllib2.urlopen(thread_url)

        image_urls = BeautifulSoup(thread_response.read(), "lxml")
        images = image_urls.find_all("a", attrs={"class": "fileThumb"})
        # Chage this to the path directory you want to save it to. This was for a usb drive.
        directory = os.path.dirname("/media/4chan/" + thread_id[1])


        if not os.path.exists(directory + "/thread/" + thread_id[1]):
            os.makedirs(directory + "/thread/" + thread_id[1])
        for image in images:
            string = image['href']
            one = string.split('/b/')
            urllib.urlretrieve("http:" + image['href'], directory + "/thread/" + thread_id[1] + "/" + one[1])



prepend = ["boards",]
append = ['b',]

for dir in append:
    for board in prepend:
        print board
        url = "http://{}.4chan.org/{}".format(board, dir)
        print "This is the directory: " + dir
        get_threads(url, board, dir)


end = time.time()
print(end - start)
