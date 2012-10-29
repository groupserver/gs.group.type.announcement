Introduction
============

This product supplies the core code to support announcement groups in
GroupServer_. These groups differ from standard *discussion* groups in two
main ways: they have different `posting rules`_ and the `group page`_ is
different. The announcement group code is enabled by changing the `marker
interface`_.

Posting Rules
=============

The main way that an announcement group differs from a discussion group is
that there is a small set of **posting members** who are the only ones that
can post. The announcement group provides a can-post rule [#canpost]_ to
restrict posting to just the posting members. This rule is enforced by 
``gs.group.type.announcement.canpostrules.PostingMember``.

Group Page
==========

Because an announcement group only has a few posting members the topics
matter less than the fact that someone posted at all. As a result the
*Group* page is altered to emphasise the posts, rather than the topics:

* The *Topics* tab and its associated JavaScript is hidden [#topics]_,
* The **standard** *Posts Summary* tab is hidden [#posts]_,
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
  gs.group.type.announcement.interfaces.IGSAnnouncementGroup

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.group.type.announcement
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. [#canpost] See ``gs.group.member.canpost`` for more information:
   <https://source.iopen.net/groupserver/gs.group.member.canpost/>
.. [#topics] Specifically, the viewlets_ ``gs-group-messages-topics-tab``
             and ``gs-group-messages-topics-script`` are replaced with
             viewlets that return ``False`` for the ``show`` property.
.. [#posts] Specifically, the viewlets ``gs-group-messages-posts-tab``
            and ``gs-group-messages-posts-script`` are replaced with
            viewlets that return ``False`` for the ``show`` property.

.. _GroupServer: http://groupserver.org
.. _viewlets: http://docs.zope.org/zope.viewlet/
