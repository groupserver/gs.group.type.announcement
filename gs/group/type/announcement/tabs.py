# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2016 OnlineGroups.net and Contributors.
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
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.home.simpletab import PublicTab, UserInfoTab
from . import GSMessageFactory as _

class DoNothing(PublicTab):
    def __init__(self, group, request, view, manager):
        super(DoNothing, self).__init__(group, request, view, manager)

    @Lazy
    def show(self):
        return False


class PostsTab(UserInfoTab):
    title = _('posts-tab-title', 'Posts')
    def __init__(self, group, request, view, manager):
        super(PostsTab, self).__init__(group, request, view, manager)

    @Lazy
    def canPost(self):
        retval = getMultiAdapter(
            (self.groupInfo.groupObj, self.loggedInUser), IGSPostingUser)
        return retval
