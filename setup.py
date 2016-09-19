#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.1.0'

if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print("Wheel library missing. Please run `pip install wheel`.")
        sys.exit()

    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')

    sys.exit()

if sys.argv[-1] == 'tag':
    print('Tagging the version on git:')

    os.system('git tag -a {0} -m "Version {0}"'.format(version))
    os.system('git push --tags')

    sys.exit()

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='django-rolodex',
    version=version,
    description="A Django application for managing your contacts.",
    long_description=readme + '\n\n' + history,
    author='Myles Braithwaite',
    author_email='me@mylesbraithwaite.com',
    url='https://github.com/myles/django-rolodex',
    packages=[
        'rolodex',
    ],
    include_package_data=True,
    install_requires=[
        'django-model-utils>=2.0',
        'psycopg2==2.6.2',
    ],
    license='MIT',
    zip_safe=False,
    keywords='django rolodex contacts address book',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
