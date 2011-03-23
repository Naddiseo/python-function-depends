#    Simple test file
#    Copyright (C) 2011  Richard Eames
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

from depends import FnDepend

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
@d.fdepends_on()
def grandchild3():
	print "grandchild3"

@d.depends_on(child2)
@d.fdepends_on()
def grandchild4():
	print "grandchild4"

grandchild3.depends_on(grandchild4)

@d.depends_on(grandchild1)
def greatgrandchild1():
	print "greatgrandchild1"

grandchild4.depends_on(greatgrandchild1)

	
def root2():
	print "root2"

@d.depends_on(root2)
def child3():
	print "child3"


@d.fdepends_on()
def circ1():
	print "circ1"

@d.depends_on(circ1)
def circ2():
	print "circ2"

circ1.depends_on(circ2)

d.run()
