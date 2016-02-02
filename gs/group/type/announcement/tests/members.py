# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
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
from mock import MagicMock, patch, PropertyMock
from unittest import TestCase
from gs.group.type.announcement.members import AnnouncementAllMembersList


class TestAnnouncementAllMembersList(TestCase):
    'Test the AnnouncementAllMembersList viewlet'

    @patch.object(AnnouncementAllMembersList, 'postingMembers', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'loggedInUser', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'groupInfo', new_callable=PropertyMock)
    def test_posting_member(self, m_gI, m_lIU, m_pM):
        'Can a posting-member see the All Members list?'
        m_pM.return_value = ['example', ]
        aaml = AnnouncementAllMembersList(MagicMock(), MagicMock(), MagicMock(), MagicMock())
        loggedInUser = aaml.loggedInUser
        loggedInUser.anonymous = False
        loggedInUser.id = 'example'

        r = aaml.show
        self.assertTrue(r)

    @patch.object(AnnouncementAllMembersList, 'postingMembers', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'loggedInUser', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'groupInfo', new_callable=PropertyMock)
    def test_normal_member(self, m_gI, m_lIU, m_pM):
        'Is a normal-member blocked from seeing the All Members list?'
        m_pM.postingMembers.return_value = ['other', ]
        aaml = AnnouncementAllMembersList(MagicMock(), MagicMock(), MagicMock(), MagicMock())
        loggedInUser = aaml.loggedInUser
        loggedInUser.anonymous = False
        loggedInUser.id = 'example'

        r = aaml.show
        self.assertFalse(r)

    @patch.object(AnnouncementAllMembersList, 'postingMembers', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'loggedInUser', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'groupInfo', new_callable=PropertyMock)
    def test_anon(self, m_gI, m_lIU, m_pM):
        'Is the All Members list hidden from Anon?'
        m_pM.return_value = ['example', ]
        aaml = AnnouncementAllMembersList(MagicMock(), MagicMock(), MagicMock(), MagicMock())
        loggedInUser = aaml.loggedInUser
        loggedInUser.anonymous = True
        loggedInUser.id = 'anonymous'

        r = aaml.show
        self.assertFalse(r)

    @patch.object(AnnouncementAllMembersList, 'postingMembers', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'loggedInUser', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'groupInfo', new_callable=PropertyMock)
    @patch.object(AnnouncementAllMembersList, 'isAdmin', new_callable=PropertyMock)
    def test_admin(self, m_iA, m_gI, m_lIU, m_pM):
        'Is the All Members list shown to an admin?'
        m_iA.return_value = True
        m_pM.return_value = ['other', ]
        aaml = AnnouncementAllMembersList(MagicMock(), MagicMock(), MagicMock(), MagicMock())
        loggedInUser = aaml.loggedInUser
        loggedInUser.anonymous = False
        loggedInUser.id = 'example'

        r = aaml.show
        self.assertTrue(r)
