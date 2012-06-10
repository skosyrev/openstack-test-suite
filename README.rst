openstack-test-suite
====================

This suite was created to test functionality of openstack.

Prerequisites
-------------
Before test installation, make sure that you have installed the following tools: Lettuce and Bunch.
It is important that you need fork of Lettuce supplied by Grid Dynamics.

Use the one from deliverable or clone Lettuce_ from GitHub::

  > cd lettuce
  > pip install .

Then install main testing tool Bunch. Use source code from deliverable or clone tool_ from GitHub::

To run tests you need:

* Preconfigured Openstack (Essex release) with working Keystone authorization;
* Services must be installed and ready to run without errors: nova- (api,compute,sceduler,cert,network,volume), glance, keystone;
* Image for instance spawning must be uploaded and changed in `config.yaml`
* Test should be run by user, able to run sudo without password.

What this suite does
--------------------

Test suite contain a directory (integration-tests/ubuntu-essex/) with Bunch_ scripts.
These scripts are BDD scenarios, you can see what steps are performed and understand what is tested.

.. _Bunch: http://openstack.griddynamics.com/docs/bunch/

For example, basic test (01-keystone-instance.test) performs the following:

* Makes changes to configuration files to perform initial keystone configuration;
* Creates project, user, network, user keys, checking tha all goes fine;
* Spawns instance and check it is accessible from outside;
* Stops instance, removes project, user, network, user keys checking every step does what it should.

There are also tests for:

* security groups
* floating ip
* volumes


Installation
------------

Get  tarball with code. Unpack it. Then perform::

    > cd openstack-test-suite
    > sudo pip install .


Configuration
-------------

Configuration file is located in scenario folder:  `integration-tests/ubuntu-essex/config.yaml`

In general to run tests you need to configure:

* image.name - name of preloaded image (shown by nova image-list).
* server.external - ip address of cloud controller (if needed. 127.0.0.1 by default)
* location of conf files of services (if needed)
* net.cloud.cidr - network for instances (if needed)
Other parameters' meaning can be clearly understood while reading test scenarios.


Running test
------------
To run tests execute::

  cd openstack-test-suite/integration-tests
  bunch --output-plugin="checklist_layout" --plugin-params="dst_dir=/var/www/" ubuntu-essex ./result_dir

Where `ubuntu-essex` is the folder for bunch tests, `result_dir` is temporary directory. Results of this run will be available in "./result_dir/ubuntu-essex" dir

After running tests, in a result dir, you can find:
* reports for every scenario run
* log file "bash.log"
* keys and other authorization files

   HTML report will be placed to directory specified by option --plugin-params="dst_dir=<your dir>".
Bunch also maintains `index.html` file. All further results are linked by this index and are kept together.
So if Web server is configured it gives you a static web site with test reports.

Troubleshooting
---------------
Commands executed by tests are logged into  ./result_dir/bash.log in details, so you can always repeat actions performed to debug them.

Known Issues
------------



.. _tool: https://github.com/griddynamics/bunch.git
.. _Lettuce: https://github.com/skosyrev/lettuce.git