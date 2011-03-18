from depend import FnDepend

d = FnDepend()

def root():
	print "root"

@d.depends_on(root)
def child():
	print "child"

@d.depends_on(root)
def child2():
	print "child2"
	
@d.depends_on(child)
def grandchild1():
	print "grandchild1"

@d.depends_on(child)
def grandchild2():
	print "grandchild2"

@d.depends_on(child2)
def grandchild3():
	print "grandchild3"

@d.depends_on(child2)
def grandchild4():
	print "grandchild4"

@d.depends_on(grandchild1)
def greatgrandchild1():
	print "greatgrandchild1"
	
def root2():
	print "root2"

@d.depends_on(root2)
def child3():
	print "child3"


@d.depends_on('circ2')
def circ1():
	print "circ1"

@d.depends_on(circ1)
def circ2():
	print "circ2"

d.run()
