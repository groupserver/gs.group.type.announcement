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
from mock import MagicMock, patch
from unittest import TestCase
from gs.group.type.announcement.canpostrules import PostingMember


class TestCanPost(TestCase):
    'Test the CanPost rules'

    @staticmethod
    def get_group_with_posting_members(members):
        'A helper function to generate groups to test'
        retval = MagicMock()
        # --=mpj17=-- I am not proud of this next line
        gp = retval.site_root().ListManager.get_list().getProperty
        gp.return_value = members
        return retval

    def assert_can_post(self, postingMember):
        failMsg = 'Cannot post: {0}'.format(postingMember.s['status'])
        self.assertTrue(postingMember.s['canPost'], failMsg)

    def assert_cannot_post(self, postingMember):
        failMsg = 'Can post: {0}'.format(postingMember.s['status'])
        self.assertFalse(postingMember.s['canPost'], failMsg)

    @patch.object(PostingMember, 'groupInfo')
    def test_posting_member_can_post(self, gi):
        'A person who is listed as a posting-member should be able to post'
        u = MagicMock()
        u.id = 'postingMember'
        g = self.get_group_with_posting_members(['postingMember'])

        pm = PostingMember(u, g)
        pm.check()

        self.assert_can_post(pm)

    @patch.object(PostingMember, 'groupInfo')
    def test_normal_member_cannot_post(self, gi):
        'A person who is listed as a normal-member should be blocked'
        u = MagicMock()
        u.id = 'normalMember'
        g = self.get_group_with_posting_members(['postingMember'])

        pm = PostingMember(u, g)
        pm.check()

        self.assert_cannot_post(pm)

    @patch.object(PostingMember, 'groupInfo')
    def test_no_members_cannot_post(self, gi):
        'If there are no posting members then everyone can post'
        g = self.get_group_with_posting_members([])

        u = MagicMock()
        u.id = 'postingMember'
        pm = PostingMember(u, g)
        pm.check()
        self.assert_can_post(pm)

        u = MagicMock()
        u.id = 'normalMember'
        pm = PostingMember(u, g)
        pm.check()
        self.assert_can_post(pm)
