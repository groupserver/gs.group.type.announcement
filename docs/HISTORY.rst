Changelog
=========

4.1.2 (2016-02-02)
------------------

* Following the update to `gs.search.base`_
* Updating the JavaScript that loads the *Posts* tab so it passes
  the `Google Closure Linter`_
* Adding to the unit tests

.. _gs.search.base: https://github.com/groupserver/gs.search.base
.. _Google Closure Linter:
   https://developers.google.com/closure/utilities/

4.1.1 (2015-04-28)
------------------

* Removing ``role="application"``, closing `Bug 4156`_

.. _Bug 4156: https://redmine.iopen.net/issues/4156

4.1.0 (2014-11-13)
------------------

* Setting the group administrators to be the posting members by
  default
* Added unit tests for the ``PostingMembers`` can-post rule
* Added unit tests for the set and unset classes


4.0.1 (2014-09-17)
------------------

* Naming the reStructuredText files as such
* Switching the primary repository to GitHub_

.. _GitHub:
   https://github.com/groupserver/gs.group.type.announcement

4.0.0 (2014-07-21)
------------------

* Added support for ``gs.group.type.set``

3.2.1 (2014-06-30)
------------------

* Updating the page templates for the *Posts* viewlet and *Recent
  members* viewlet, because a ``<ul>`` element cannot have the
  ``navigation`` role

3.2.0 (2014-03-26)
------------------

* Added an *All Members* tab on the *Members* page, fixing a
  privacy issue.
* Adding a *Recently active* list
* Switching to Unicode literals.

3.1.2 (2013-11-26)
------------------

* Switching to the new character-spinner
* Metadata update

3.1.1 (2013-07-26)
------------------

* Adding a *Web feed* icon

3.1.0 (2013-05-30)
------------------

* Following the updates to jQuery
* Fixing an issue with the Post tab being hidden by default

3.0.1 (2013-03-25)
------------------

* Cleaning up the JavaScript, and using the minified JavaScript code
* Updating the README
* Dropping old JavaScript code

3.0.0 (2013-02-28)
------------------

* Following the updates to the new user interface
* Whitespace cleanup

2.0.1 (2012-10-29)
------------------

* Updating the README

2.0.0 (2012-07-27)
------------------

* Fixing permissions
* Updating the version number

1.1.0 (2012-06-06)
------------------

* Switching to the standard Search JavaScript

1.0.0 (2012-05-16)
------------------

* Moved the can-post rules here from ``gs.group.member.canpost``
* Made an announcement group a subclass of a discussion group
* Hid the standard *Topics* tab and the *Posts* tab
* Added a new *Posts* tab

..  LocalWords:  Changelog
