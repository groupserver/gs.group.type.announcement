# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from gs.group.member.list.lists import AllMemberList
from gs.group.member.viewlet import GroupAdminViewlet


class AnnouncementAllMembersList(AllMemberList, GroupAdminViewlet):
    '''Members  of an announcement group should be able to lurk in peace:

    * A normal group member should not see the All tab.
    * A posting member should see the All tab.
    <https://redmine.iopen.net/issues/4076>'''

    def __init__(self, group, request, view, manager):
        super(AnnouncementAllMembersList, self).__init__(
            group, request, view, manager)

    @Lazy
    def mailingList(self):
        site_root = self.group.site_root()
        mailingListManager = site_root.ListManager
        retval = mailingListManager.get_list(self.groupInfo.id)
        return retval

    @Lazy
    def postingMembers(self):
        retval = self.mailingList.getProperty('posting_members', [])
        return retval

    @Lazy
    def show(self):
        retval = ((not self.loggedInUser.anonymous)
                  and ((self.loggedInUser.id in self.postingMembers)
                       or (self.isAdmin)))
        assert type(retval) == bool
        return retval
