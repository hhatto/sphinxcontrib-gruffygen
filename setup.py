# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

long_desc = '''
This package contains the Gruffy_ Sphinx_ extension.

.. _Sphinx: http://sphinx.pocoo.org/
.. _Gruffy: https://pypi.python.org/pypi/gruffy

Gruffy is Graphing Library.

This extension adds the ``gruffy`` directive that automatically selects the
image format to use acording to the Sphinx_ writer used to generate the
documentation.

Usage example::

    .. gruffy::
        :width: 500
        :title: Sphinx with Gruffy

        data("test" (1, 3, 5, 3))
        data("test-long" (5, 3, 2, 6))

'''

requires = ['Sphinx>=0.6', 'gruffy>=0.2']

setup(
    name='sphinxcontrib-gruffygen',
    version='0.1',
    url='http://pypi.python.org/pypi/sphinxcontrib-gruffygen/',
    license='BSD',
    author='Hideo Hattori',
    author_email='hhatto.jp@gmail.com',
    description='Gruffy Sphinx extension',
    long_description=long_desc,
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
