# coding=utf-8
from zope.cachedescriptors.property import Lazy
from gs.group.member.canpost.rules import BaseRule

class PostingMember(BaseRule):
    u'''Only a select few members can post to this group. If
    no posting members are specified then every member of this group
    is a posting member.'''
    weight = 90
    def __init__(self, user, group):
        BaseRule.__init__(self, user, group)
        self.__checked = False
            
    def check(self):
        if not self.__checked:
            ml = self.mailingList
            postingMembers = ml.getProperty('posting_members', [])
            if postingMembers and (self.userInfo.id in postingMembers):
                self.__canPost = True
                self.__status = u'a posting member'
                self.__statusNum = 0
            elif postingMembers and (self.userInfo.id not in postingMembers):
                self.__canPost = False
                self.__status = u'not a posting member'
                self.__statusNum = self.weight
            elif not(postingMembers):
                self.__canPost = True
                self.__status = u'a posting member, like everyone'
                self.__statusNum = 0
                
        assert type(self.__canPost) == bool
        assert type(self.__status) == unicode
        assert type(self.__statusNum) == int

    @Lazy
    def canPost(self):
        self.check()
        return self.__canPost
    
    @Lazy
    def statusNum(self):
        self.check()
        return self.__statusNum

    @Lazy
    def status(self):
        self.check()
        return self.__status

