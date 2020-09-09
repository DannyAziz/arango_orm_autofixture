#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import io

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.md'), encoding="utf8").read()

version = '0.0.1'

tests_require = [
    'pytest',
    'pytest-cov',
    'pytest-flakes',
    'pytest-pep8',
    'faker'
]

# this module can be zip-safe if the zipimporter implements iter_modules or if
# pkgutil.iter_importer_modules has registered a dispatch for the zipimporter.
try:
    import pkgutil
    import zipimport
    zip_safe = hasattr(zipimport.zipimporter, "iter_modules") or \
        zipimport.zipimporter in pkgutil.iter_importer_modules.registry.keys()
except (ImportError, AttributeError):
    zip_safe = False

setup(
    name='arango_orm_autofixture',
    version=version,
    description="Provider for the Faker Python package that reads your schema and generates fake objects.",
    long_description=README,
    classifiers=[
        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'License :: OSI Approved :: Apache Software License'
    ],
    keywords='ararngo arango_orm faker marshmallow autofixture',
    author='dannyaziz',
    author_email='hello@dannyaziz.com',
    url='https://github.com/DannyAziz/arango_orm_autofixture',
    license='Apache License, Version 2.0',
    package_dir={'arango_orm_autofixture': 'src'},
    packages=['arango_orm_autofixture'],
    platforms=['any'],
    zip_safe=zip_safe,
    install_requires=['faker'],
)