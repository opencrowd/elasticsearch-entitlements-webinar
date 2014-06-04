Demo app for OpenCrowd's ElasticSearch Entitlements Webinar
===========================================================

This is a simple Django app to illustrate the scenario used in
OpenCrowd's ElasticSearch Entitlements webinar.
([Watch the webinar](http://opencrowd.com/media/#entitlements))

For each type of user test, the generated query sent to
ElasticSearch is rendered so that you can see how the entitlement
scheme used in the scenario is implemented.

This app depends on the __requests__ and __django__ packages.  It
also requires a running ElasticSearch instance.

You can get it started by:

    $ ./manage.py init_demo
    $ ./manage.py runserver


