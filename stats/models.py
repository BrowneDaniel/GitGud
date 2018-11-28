# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from github import Github

from collections import Counter

# Create your models here.
limit = 100  # the maximum number of friends to iterate through to calculate averages, for the benefit of load times.


class User(models.Model):
    username = models.CharField(max_length = 128)
    pw = models.CharField(max_length = 256)

    def __str__(self):
        return self.username

    def followers(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        retval = account.get_followers().totalCount
        return retval

    def following(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        retval = account.get_following().totalCount
        return retval

    def repos(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        retval = account.get_repos().totalCount
        return retval

    def stars(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        repos = account.get_repos()
        retval = 0
        for repo in repos:
            retval += repo.stargazers_count
        return retval

    def languages(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        repos = account.get_repos()
        keylist = []
        for repo in repos:
            test = repo.get_languages()
            keylist += list(test.keys())

        retval = len(set(keylist))
        return retval

    def total_languages(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        repos = account.get_repos()
        keylist = []
        for repo in repos:
            test = repo.get_languages()
            keylist += list(test.keys())

        retval = Counter(keylist).items()
        return retval

    def friends_followers(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        friends = account.get_followers()
        friendfollowers = []

        index = 0
        for friend in friends:
            friendfollowers.append(friend.get_followers().totalCount)
            index += 1
            if index >= limit:
                break

        avgfriendfollowers = 0

        for num in friendfollowers:
            avgfriendfollowers += num

        avgfriendfollowers = avgfriendfollowers / len(friendfollowers)

        retval = avgfriendfollowers
        return retval

    def friends_following(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        friends = account.get_followers()
        friendfollowing = []

        index = 0
        for friend in friends:
            friendfollowing.append(friend.get_following().totalCount)
            index += 1
            if index >= limit:
                break

        avgfriendfollowing = 0

        for num in friendfollowing:
            avgfriendfollowing += num

        avgfriendfollowing = avgfriendfollowing / len(friendfollowing)
        retval = avgfriendfollowing
        return retval

    def friends_repos(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        friends = account.get_followers()
        friendrepos = []

        index = 0
        for friend in friends:
            friendrepos.append(friend.get_repos().totalCount)
            index += 1
            if index >= limit:
                break

        avgfriendrepos = 0

        for num in friendrepos:
            avgfriendrepos += num

        avgfriendrepos = avgfriendrepos / len(friendrepos)
        retval = avgfriendrepos
        return retval

    def friends_stars(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        friends = account.get_followers()
        friendstars = []

        index = 0
        for friend in friends:
            repos = friend.get_repos()
            starcount = 0
            for repo in repos:
                starcount += repo.stargazers_count

            friendstars.append(starcount)
            index += 1
            if index >= limit:
                break

        avgfriendstars = 0
        for num in friendstars:
            avgfriendstars += num

        avgfriendstars = avgfriendstars / len(friendstars)
        retval = avgfriendstars
        return retval

    def friends_languages(self):
        g = Github(self.username, self.pw)
        account = g.get_user()
        friends = account.get_followers()
        friendlanguages = []

        index = 0
        for friend in friends:
            repos = friend.get_repos()
            keylist = []
            for repo in repos:
                test = repo.get_languages()
                keylist += list(test.keys())
            langs = len(set(keylist))
            friendlanguages.append(langs)
            index += 1
            if index >= limit:
                break

        avgfriendlanguages = 0

        for num in friendlanguages:
            avgfriendlanguages += num

        avgfriendlanguages = avgfriendlanguages / len(friendlanguages)

        retval = avgfriendlanguages
        return retval
