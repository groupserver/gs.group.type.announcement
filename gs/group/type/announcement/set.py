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
    name = 'Announcement group: only “posting members” can post'
    weight = 20
    show = True

    def set(self):
        self.set_marker()
        self.set_list_property('replyto', 'sender')

    def set_marker(self):
        '''Add the marker-interface to make the group into a discussion
        group.'''
        iFaces = [
            'gs.group.type.announcement.interfaces.IGSAnnouncementGroup']
        self.add_marker(self.group, iFaces)


class UnsetAnnouncementGroup(UnsetABC):
    name = 'Announcement group'
    setTypeId = 'gs-group-type-announcement-set'

    def unset(self):
        self.unset_marker()
        self.del_list_property('replyto')

    def unset_marker(self):
        iFaces = [
            'gs.group.type.announcement.interfaces.IGSAnnouncementGroup']
        self.del_marker(self.group, iFaces)
