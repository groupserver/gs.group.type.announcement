# coding=utf-8
from zope.cachedescriptors.property import Lazy
from zope.component import getMultiAdapter
from Products.GSGroup.interfaces import IGSMailingListInfo
from gs.group.member.canpost.interfaces import IGSPostingUser
from gs.group.home.simpletab import PublicTab

class DoNothing(PublicTab):
    def __init__(self, group, request, view, manager):
        PublicTab.__init__(self, group, request, view, manager)
            
    @Lazy
    def show(self):
        return False

class PostsTab(PublicTab):
    def __init__(self, group, request, view, manager):
       PublicTab.__init__(self, group, request, view, manager)
        
    @Lazy
    def canPost(self):
        retval = getMultiAdapter((self.groupInfo.groupObj, self.userInfo), 
                                  IGSPostingUser)
        return retval
