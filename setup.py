import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name = 'python-function-depends',
	version = '0.0.1',
	description = 'Provides decorators to allow for function dependencies',
	url = 'http://github.com/Naddiseo/python-function-depends',
	author = 'Richard Eames',
	author_email = 'reames@asymmetricventures.com',
	licence = 'GPLv3',
	long_description = read('README'),
	packages = ['depends'],
	classifiers = [
		'Programming Language :: Python'
	]	
)
