#!/usr/bin/env python
#
# $Id: setup.py,v 1.11 2005/02/15 16:32:22 warnes Exp $

CVS=0

from setuptools import setup, find_packages
import os
import io

def read(*rnames):
    return u"\n"+ io.open(
        os.path.join('.', *rnames),
        encoding='utf8',
    ).read()
url="https://github.com/kiorky/SOAPpy.git"
long_description=u"SOAPpy provides tools for building SOAP clients and servers.  For more information see " + url\
    +u'\n'+read('README.rst')\
    +u'\n'+read('CHANGES.txt')
setup(
    name="SOAPpy",
    version='0.12.23.dev0',
    description="SOAP Services for Python",
    maintainer="Gregory Warnes, kiorky",
    maintainer_email="Gregory.R.Warnes@Pfizer.com, kiorky@cryptelium.net",
    url = url,
    long_description=long_description,
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    install_requires=[
        'wstools',
        'defusedxml',
    ]
)

