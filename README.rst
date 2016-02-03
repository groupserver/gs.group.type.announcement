==============================
``gs.group.type.announcement``
==============================
~~~~~~~~~~~~~~~~~~~~~~~~~~
Announcement group support
~~~~~~~~~~~~~~~~~~~~~~~~~~

:Author: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-11-13
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.net`_.

..  _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

Introduction
============

This product supplies the core code to support announcement
groups in GroupServer_. These groups differ from standard
*discussion* groups in two main ways: they have different
`posting rules`_ and the `group page`_ is different. The
announcement group code is enabled by changing the `marker
interface`_.

Posting Rules
=============

The main way that an announcement group differs from a discussion
group is that there is a small set of **posting members** who are
the only ones that can post. The announcement group provides a
can-post rule [#canpost]_ to restrict posting to just the posting
members. This rule is enforced by
``gs.group.type.announcement.canpostrules.PostingMember``.

The list of posting members is implemented as a list of user
identifiers, on the *mailing* *list* instance, named
``posting_members``. If this property is absent, or if it is
empty, then **all** group members can post. The list of posting
members is set by *Manage Members* [#manage]_.

Group Page
==========

Because an announcement group only has a few posting members the
topics matter less than the fact that someone posted at all. As a
result the *Group* page is altered to emphasise the posts, rather
than the topics:

* The *Topics* tab and its associated JavaScript is hidden
  [#topics]_,
* The **standard** *Posts Summary* tab is hidden [#posts]_,
* A **new** *Posts* tab is shown, which looks more like the
  standard topics tab.

Marker Interface
================

A group is turned into an announcement group by changing the
marker interface for the group folder to
``IGSAnnouncementGroup``. This marker interface has the following
inheritance tree::

  gs.group.base.interfaces.IGSGroupMarker
      △
      │
  gs.group.type.discussion.interfaces.IGSDiscussionGroup
      △
      │
  gs.group.type.announcement.interfaces.IGSAnnouncementGroup

Resources
=========

- Translations:
  https://www.transifex.com/groupserver/gs-group-type-announcement/
- Code repository:
  https://github.com/groupserver/gs.group.type.announcement
- Questions and comments to
  http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#canpost] See ``gs.group.member.canpost`` for more
   information:
   <https://github.com/groupserver/gs.group.member.canpost/>
.. [#manage] See ``gs.group.member.manage`` for more information:
   <https://github.com/groupserver/gs.group.member.manage/>
.. [#topics] Specifically, the viewlets_
             ``gs-group-messages-topics-tab`` and
             ``gs-group-messages-topics-script`` are replaced
             with viewlets that return ``False`` for the ``show``
             property.
.. [#posts] Specifically, the viewlets
            ``gs-group-messages-posts-tab`` and
            ``gs-group-messages-posts-script`` are replaced with
            viewlets that return ``False`` for the ``show``
            property.

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net
.. _Michael JasonSmith: http://groupserver.org/p/mpj17
.. _GroupServer: http://groupserver.org
.. _viewlets: http://docs.zope.org/zope.viewlet/
