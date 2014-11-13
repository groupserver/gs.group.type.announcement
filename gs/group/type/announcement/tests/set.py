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
from gs.group.type.announcement.set import SetAnnouncementGroup


class TestSet(TestCase):
    'Test the Set rules'

    @patch.object(SetAnnouncementGroup, 'set_list_property')
    @patch('gs.group.type.announcement.set.IGSGroupInfo')
    def test_set_admins_as_posting_members(self, igi, sli):
        'Test that we can set the group-admins as the posting members'
        gi = igi.return_value
        admins = [MagicMock(), MagicMock()]
        admins[0].id = 'admin1'
        admins[1].id = 'admin2'
        gi.group_admins = admins

        g = MagicMock()
        sag = SetAnnouncementGroup(g)
        sag.set_admins_as_posting_members()

        sli.assert_called_once_with('posting_members',
                                    [a.id for a in admins])
