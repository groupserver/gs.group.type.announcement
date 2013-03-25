# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.home.simpletab import PublicTab, UserInfoTab


class DoNothing(PublicTab):
    def __init__(self, group, request, view, manager):
        super(DoNothing, self).__init__(group, request, view, manager)

    @Lazy
    def show(self):
        return False


class PostsTab(UserInfoTab):
    def __init__(self, group, request, view, manager):
        super(PostsTab, self).__init__(group, request, view, manager)

    @Lazy
    def canPost(self):
        retval = getMultiAdapter((self.groupInfo.groupObj, self.loggedInUser),
                                    IGSPostingUser)
        return retval
