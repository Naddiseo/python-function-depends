class FnDepend(object):
	class Node(object):
		def __init__(self, func, args = [], kwargs = {}):
			self.func = func
			self.args = args
			self.kwargs = kwargs
			self.dependencies = set([])
			self.children     = set([])
			self.patch        = {}
		
		def __eq__(self, other):
			return self.func == other
		
		def run(self):
			if isinstance(self.func, basestring):
				eval(self.func + '(*self.args, **self.kwargs)')
			self.func(*self.args, **self.kwargs)
		
		def __repr__(self):
			if self.func is None:
				return 'NoneType'
			elif isinstance(self.func, basestring):
				eval(self.func + '.__name__')
			return self.func.__name__
		
		def add_child(self, child):
			self.children.add(child)
			child.dependencies.add(self)
		
	def __init__(self):
		self.nodes = set([])
		
	def get_or_set_node(self, func):
		for node in self.nodes:
			if node == func:
				return node
		node = FnDepend.Node(func)
		self.nodes.add(node)
		return node
	
	def depends_on(self, dependency):
		def wrapper(func):
			if func is None:
				raise Exception('Func is none')
			if dependency is None:
				raise Exception('Dependency is None')
		
			node = self.get_or_set_node(func)			
			parent = self.get_or_set_node(dependency)

			parent.add_child(node)
					
			self.nodes.add(node)
			return func
		
		return wrapper
		
	def run(self):
		run     = set([])
		top     = set([])
		new_top = set([])
		
		for node in self.nodes:
			if len(node.dependencies) == 0:
				top.add(node)
		
		while len(top):
			for node in top:
				if node.dependencies <= run:
					new_top |= node.children
					node.run()
					run.add(node)
			top = new_top
			new_top = set([])
		
