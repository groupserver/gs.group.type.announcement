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
from gs.group.type.announcement.set import (
    SetAnnouncementGroup, UnsetAnnouncementGroup, INTERFACES)
REPLYTO = b'replyto'
POSTING_MEMBERS = b'posting_members'


class TestSet(TestCase):
    'Test the Set rules'

    @patch.object(SetAnnouncementGroup, 'set_list_property')
    @patch('gs.group.type.announcement.set.IGSGroupInfo')
    def test_set_admins_as_posting_members(self, igi, sli):
        'Test that we can set the group-admins as the posting members'
        gi = igi.return_value
        admins = [MagicMock(id='admin1'), MagicMock(id='admin2')]
        gi.group_admins = admins

        g = MagicMock()
        sag = SetAnnouncementGroup(g)
        sag.set_admins_as_posting_members()

        sli.assert_called_once_with(POSTING_MEMBERS, [a.id for a in admins])

    @patch.object(SetAnnouncementGroup, 'set_admins_as_posting_members')
    def test_set_default_posting_members_no_property(self, sa):
        'Test that we set posting_members if there is no property'
        g = MagicMock()
        g.getId.return_value = 'example_group'
        eg = g.site_root().ListManager.example_group
        eg.hasProperty.return_value = False

        sag = SetAnnouncementGroup(g)
        sag.set_default_posting_members()

        sa.assert_called_once_with()

    @patch.object(SetAnnouncementGroup, 'set_admins_as_posting_members')
    def test_set_default_posting_members_property(self, sa):
        '''Test that we skip setting the posting_members if the property
exists'''
        g = MagicMock()
        g.getId.return_value = 'example_group'
        eg = g.site_root().ListManager.example_group
        eg.hasProperty.return_value = True

        sag = SetAnnouncementGroup(g)
        sag.set_default_posting_members()

        self.assertEqual(0, sa.call_count)

    @patch.object(SetAnnouncementGroup, 'add_marker')
    @patch.object(SetAnnouncementGroup, 'set_default_posting_members')
    @patch.object(SetAnnouncementGroup, 'set_list_property')
    def test_set(self, slp, sdpm, am):
        'Test we set the reply-to to sender'
        g = MagicMock()

        sag = SetAnnouncementGroup(g)
        sag.set()

        slp.assert_called_once_with(REPLYTO, 'sender')
        am.assert_called_once_with(g, INTERFACES)
        sdpm.assert_called_once_with()


class TestUnset(TestCase):
    @patch.object(UnsetAnnouncementGroup, 'del_marker')
    @patch.object(UnsetAnnouncementGroup, 'del_list_property')
    def test_unset(self, dlp, dm):
        g = MagicMock()

        uag = UnsetAnnouncementGroup(g)
        uag.unset()

        dlp.assert_called_once_with(REPLYTO)
        dm.assert_called_once_with(g, INTERFACES)
