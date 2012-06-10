#!/usr/bin/env python

from setuptools import setup

required_modules = ['pexpect', 'IPy']

setup(name='openstack-core-test',
      version='1.0.0',
      description='Grid Dynamics OpenStack test suite',
      author=u'Grid Dynamics',
      author_email='openstack@griddynamics.com',
      url='http://griddynamics.com/',
      packages=['openstack_core_test', 'openstack_core_test.utils'],
      install_requires=required_modules
      )


