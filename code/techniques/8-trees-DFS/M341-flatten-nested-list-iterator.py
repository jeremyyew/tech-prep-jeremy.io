class NestedIterator(object):

	def __init__(self, nestedList):
		self.stack =  nestedList[::-1]


	def next(self):
		return self.stack.pop().getInteger()


	def hasNext(self):
		while self.stack and not self.stack[-1].isInteger():
			nl = self.stack.pop()
			self.stack.extend(nl.getList()[::-1])

		return self.stack