'''
Write a function that stores URLs in chronological order and if a URL already exists then keep only the last one of the two.

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.prev = None
        self.next = None

class URLMaintainer:
	def __init__(self):
		self.url_list = None
		self.url_map = {}
		self.last = None

	def addUrl(self, url):
		if url in self.url_map:
			node = self.url_map[url]
			# check if first element
			if not node.prev:
				self.url_list = node.next
			else:
				node.prev.next = node.next
			# check if last element
			if not node.next:
				self.last = node.prev
			else:
				node.next.prev = node.prev
			del self.url_map[url]

		if not self.url_list: # still empty url bank
			self.url_list = ListNode(url)
			self.last = self.url_list
			self.url_map[url] = self.url_list
		else: # add to the last element
			node = ListNode(url)
			node.prev = self.last
			if self.last:
				self.last.next = node
			self.last = node
			self.url_map[url] = self.last

	def printUrls(self):
		cur = self.url_list
		l = []
		while cur:
			l.append(cur.val)
			cur = cur.next
		print(l)

class Solution:
    def maintainUrls(self, urls):
    	maintainer = URLMaintainer()
    	for url in urls:
    		print("Adding %s...", url)
    		maintainer.addUrl(url)
    		maintainer.printUrls()

# And this is the example:

s = Solution()
s.maintainUrls(["https://leetcode.com/",
	"https://www.alz.org/",
	"https://github.com/",
	"https://github.com/",
	"https://www.justonecookbook.com/okonomiyaki/",
	"https://www.justonecookbook.com/okonomiyaki/",
	"https://www.alz.org/",
	"https://leetcode.com/"])
print("---")
s.maintainUrls(["https://leetcode.com/",
	"https://leetcode.com/",
	"https://leetcode.com/"])