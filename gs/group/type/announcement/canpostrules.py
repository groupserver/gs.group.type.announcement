# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
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
from gs.group.member.canpost.rules import BaseRule


class PostingMember(BaseRule):
    '''Only a select few members can post to this group. If
    no posting members are specified then every member of this group
    is a posting member.'''
    weight = 90

    def check(self):
        if not self.s['checked']:
            ml = self.mailingList
            postingMembers = ml.getProperty('posting_members', [])
            if postingMembers and (self.userInfo.id in postingMembers):
                self.s['canPost'] = True
                self.s['status'] = 'a posting member'
                self.s['statusNum'] = 0
            elif (postingMembers
                  and (self.userInfo.id not in postingMembers)):
                self.s['canPost'] = False
                self.s['status'] = 'not a posting member'
                self.s['statusNum'] = self.weight
            elif not(postingMembers):
                self.s['canPost'] = True
                self.s['status'] = 'a posting member, like everyone'
                self.s['statusNum'] = 0
            self.s['checked'] = True

        assert self.s['checked']
        assert type(self.s['canPost']) == bool
        assert type(self.s['statusNum']) == int
