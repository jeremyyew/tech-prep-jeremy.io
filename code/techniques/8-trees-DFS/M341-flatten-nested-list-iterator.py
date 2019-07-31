'''
- Only pop and unpack what is necessary. 
- Pop and unpack when `hasNext` is called - it ensures there is a next available for `next`, if there really is a next. 
- At the end only need to check if stack is nonempty - stack nonempty and last element not integer is not possible.
'''

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