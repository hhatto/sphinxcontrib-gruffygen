# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

requires = ['Sphinx>=0.6', 'gruffy>=0.2']

setup(
    name='sphinxcontrib-gruffygen',
    version='0.1.1',
    url='http://pypi.python.org/pypi/sphinxcontrib-gruffygen/',
    license='BSD',
    author='Hideo Hattori',
    author_email='hhatto.jp@gmail.com',
    description='Gruffy Sphinx extension',
    long_description=open('README.rst').read(),
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires,
    namespace_packages=['sphinxcontrib'],
)
