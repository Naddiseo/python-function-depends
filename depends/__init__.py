#    Function dependency decorators for python
#    Copyright (C) 2011 Richard Eames
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
class FnDepend(object):
	class Node(object):
		def __init__(self, func, args = [], kwargs = {}):
			self.func = func
			self.args = args
			self.kwargs = kwargs
			self.dependencies = set([])
			self.children = set([])
			self.patch = {}
		
		def __eq__(self, other):
			return self.func == other
		
		def run(self):
			self.func(*self.args, **self.kwargs)
		
		def __repr__(self):
			if self.func is None:
				return 'NoneType'
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
	
	def _fwrapper(self, func, dependency):
		if dependency is None:
			raise Exception('Dependency is None')
		
		node = self.get_or_set_node(func)
		parent = self.get_or_set_node(dependency)
		
		parent.add_child(node)
		self.nodes.add(node)
	
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
	
	def fdepends_on(self):
		def wrapper(func):
			if func is None:
				raise Exception('Func is none')
			
			def _inner(d):
				return apply(self._fwrapper, (func, d))
			
			setattr(func, 'depends_on', _inner)
			
			return func
		return wrapper
	
	def run(self):
		run = set([])
		top = set([])
		new_top = set([])
		
		for node in self.nodes:
			if len(node.dependencies) == 0:
				top.add(node)
			
		while len(top):
			#print("%s"%top)
			for node in top:
				if (not node in run) and (node.dependencies <= run):
					new_top |= node.children
					node.run()
					run.add(node)
			top = new_top
			new_top = set([])
		
