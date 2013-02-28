# coding=utf-8
from gs.group.member.canpost.rules import BaseRule


class PostingMember(BaseRule):
    u'''Only a select few members can post to this group. If
    no posting members are specified then every member of this group
    is a posting member.'''
    weight = 90

    def check(self):
        if not self.s['checked']:
            ml = self.mailingList
            postingMembers = ml.getProperty('posting_members', [])
            if postingMembers and (self.userInfo.id in postingMembers):
                self.s['canPost'] = True
                self.s['status'] = u'a posting member'
                self.s['statusNum'] = 0
            elif postingMembers and (self.userInfo.id not in postingMembers):
                self.s['canPost'] = False
                self.s['status'] = u'not a posting member'
                self.s['statusNum'] = self.weight
            elif not(postingMembers):
                self.s['canPost'] = True
                self.s['status'] = u'a posting member, like everyone'
                self.s['statusNum'] = 0
            self.s['checked'] = True

        assert self.s['checked']
        assert type(self.s['canPost']) == bool
        assert type(self.s['status']) == unicode
        assert type(self.s['statusNum']) == int
