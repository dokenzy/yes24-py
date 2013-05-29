# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
	name='yes24',
	version='0.1.1',
	packages=['yes24'],
	package_dir={'yes24': 'src/yes24'},
	install_requires=['beautifulsoup4', 'lxml'],
	license='MIT License',
	author='dokenzy',
	author_email='dokenzy@gmail.com',
	url='https://github.com/dokenzy/yes24-py',
	description='yes24.com api',
)