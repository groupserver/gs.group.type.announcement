Introduction
============

This product supplies the core code to support announcement groups. These
groups differ from standard *discussion* groups in two main ways: they have
different `posting rules`_ and the `group page`_ is different. The
announcement group code is enabled by changing the `marker interface`_.

Posting Rules
=============

The main way that an announcement group differs from a discussion group is
that there is a small set of **posting members** who are the only ones that
can post. The announcement group provides a can-post rule [#canpost]_ to
restrict posting to just the posting members.

Group Page
==========

Because an announcement group only has a few posting members the topics
matter less than the fact that someone posted at all. As a result the
*Group* page is altered to emphasise the posts, rather than the topics:

* The *Topics* tab is hidden,
* The **standard** *Posts Summary* tab is hidden,
* A **new** *Posts* tab is shown, which looks more like the standard topics 
  tab.

Marker Interface
================

A group is turned into an announcement group by changing the marker
interface for the group folder to ``IGSAnnouncementGroup``. This marker
interface has the following inheritance tree::

  gs.group.base.interfaces.IGSGroupMarker
      △
      │
  gs.group.type.discussion.interfaces.IGSDiscussionGroup
      △
      │
  gs.group.type.announcement.interfacesIGSAnnouncementGroup

.. [#canpost] See ``gs.group.member.canpost`` for more information.
