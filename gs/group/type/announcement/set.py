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


class SetAnnouncementGroup(SetABC):
    'Set a group folder to be an announcement group'
    name = 'Announcement group'
    typeId = 'gs-group-type-announcement-set'
    weight = 20
    show = True

    def set(self):
        self.set_marker()
        self.set_replyto()

    def set_marker(self):
        '''Add the marker-interface to make the group into a discussion
        group.'''
        iFaces = [
            'gs.group.type.announcement.interfaces.IGSAnnouncementGroup']
        self.add_marker(self.group, iFaces)

    def set_replyto(self):
        'Set the reply-to property of the mailing list'
        siteRoot = self.group.site_root()
        listManager = getattr(siteRoot, 'ListManager')
        mailingList = getattr(listManager, self.group.getId())
        if mailingList.hasProperty('replyto'):
            mailingList.manage_changeProperties(replyto='sender')
        else:
            mailingList.manage_addProperty('replyto', 'sender', 'string')


class UnsetAnnouncementGroup(UnsetABC):
    name = 'Announcement group'

    def unset(self):
        self.unset_marker()
        self.unset_replyto()

    def unset_marker(self):
        iFaces = [
            'gs.group.type.announcement.interfaces.IGSAnnouncementGroup']
        self.del_marker(self.group, iFaces)

    def unset_replyto(self):
        siteRoot = self.group.site_root()
        listManager = getattr(siteRoot, 'ListManager')
        mailingList = getattr(listManager, self.group.getId())
        if mailingList.hasProperty('replyto'):
            mailingList.manage_delProperties(['replyto', ])
