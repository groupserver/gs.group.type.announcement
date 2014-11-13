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
from gs.group.type.set import (SetABC, UnsetABC)
from Products.GSGroup.interfaces import IGSGroupInfo
INTERFACES = ['gs.group.type.announcement.interfaces.IGSAnnouncementGroup']


class SetAnnouncementGroup(SetABC):
    'Set a group folder to be an announcement group'
    name = 'Announcement group: only \u2018posting members\u2019 can post'
    weight = 20
    show = True

    def set(self):
        self.set_marker()
        self.set_list_property('replyto', 'sender')
        self.set_default_posting_members()

    def set_marker(self):
        '''Add the marker-interface to make the group into a discussion
        group.'''
        self.add_marker(self.group, INTERFACES)

    def set_default_posting_members(self):
        siteRoot = self.group.site_root()
        listManager = getattr(siteRoot, 'ListManager')
        mailingList = getattr(listManager, self.group.getId())
        if not mailingList.hasProperty('posting_members'):
            self.set_admins_as_posting_members()

    def set_admins_as_posting_members(self):
        groupInfo = IGSGroupInfo(self.group)
        admins = [a.id for a in groupInfo.group_admins]
        if admins:
            self.set_list_property('posting_members', admins)


class UnsetAnnouncementGroup(UnsetABC):
    name = 'Announcement group'
    setTypeId = 'gs-group-type-announcement-set'

    def unset(self):
        self.unset_marker()
        self.del_list_property('replyto')
        # Leave the posting_members property alone

    def unset_marker(self):
        self.del_marker(self.group, INTERFACES)
