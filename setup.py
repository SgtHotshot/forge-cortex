import os
import os.path
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as readme:
	README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt'), 'r') as requirements:
	REQUIREMENTS = requirements.readlines()

os.chdir(
	os.path.normpath(
		os.path.join(os.path.abspath(__file__), os.pardir)
	)
)

setup(
	name                 = 'forge-cortex',
	version              = '1.0.0.0',
	author               = 'Ben Ebert, James Durand, Andrew Ebert',
	author_email         = 'ebertb@alumni.msoe.edu, james.durand@alumni.msoe.edu, developer@andrewtebert.com',
	license              = 'MIT',
	description          = 'Minecraft Forge mod directory',
	long_description     = README,
	url                  = 'https://github.com/sgthotshot/forge-cortex',
	packages             = ['cortex'],
	include_package_data = True,
	install_requires     = REQUIREMENTS,
)

