from distutils.core import setup

from setuptools import find_packages

import os


# Pull project description (long) from project readme
current_directory = os.path.dirname(os.path.abspath(__file__))

# Linke to the requirements text file
requirementPath = current_directory + '/requirements.txt'
install_requires = []
if os.path.isfile(requirementPath):
    with open(requirementPath) as f:
        install_requires = f.read().splitlines()

try:

    with open(os.path.join(current_directory,'README.md'), encoding='utf-8') as f:

        long_description = f.read()

except Exception:

    long_description = ''

setup(

	# Project name: 

	name='',

	# Packages to include in the distribution: 

	packages=find_packages(''),

	# Project version number:

	version='1.0.0',

	# List a license for the project, eg. MIT License

	license='MIT License',

	# Short description of your library: 

	description='',

	# Long description of your library: 

	long_description=long_description,

	long_description_content_type='text/markdown',

	# Your name: 

	author='Asa LeHolland',

	# Your email address:

	author_email='asaleholland@gmail.com',

	# Link to your github repository or website: 

	url='https://github.com/asa-leholland/{repo-name}',

	# Download Link from where the project can be downloaded from:

	download_url='https://github.com/asa-leholland/{repo-name}',

	# List of keywords: 

	keywords=['Python', ],

	# List project dependencies: 

	install_requires=install_requires,

	# https://pypi.org/classifiers/ 

	classifiers=['Environment :: Win32 (MS Windows)', 'Development Status :: 5 - Production/Stable', 'Intended Audience :: End Users/Desktop', 'License :: Free For Educational Use', 'Programming Language :: Python :: 3.7', 'Topic :: Education']

)
