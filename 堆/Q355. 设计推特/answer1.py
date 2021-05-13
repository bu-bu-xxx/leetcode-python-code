# encoding:utf-8
# @Author :ZQY
# @web : https://leetcode-cn.com/problems/


# 自己做
import collections


class Twitter:
    import collections

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.followDictSet = collections.Counter()
        self.tw = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        # 有这个人则发推特，没人则注册后再发
        self.tw.append((userId, tweetId))

    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.
        Each item in the news feed must be posted by users who the user
        followed or by the user herself. Tweets must be ordered from most
        recent to least recent.
        """
        allId = {userId} if userId not in self.followDictSet \
            else {userId} | self.followDictSet[userId]
        k = 1
        result = []
        for (postId, tweetId) in self.tw[-1::-1]:
            if k == 11:
                break
            if postId in allId:
                result.append(tweetId)
                k += 1
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid,
        it should be a no-op.
        """
        # follower关注followee
        if followerId not in self.followDictSet:
            self.followDictSet[followerId] = {followeeId}
        else:
            self.followDictSet[followerId] = self.followDictSet[followerId] | {followeeId}

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee.
        If the operation is invalid, it should be a no-op.
        """
        # follower关注followee
        if followerId in self.followDictSet:
            self.followDictSet[followerId] = self.followDictSet[followerId] - {followeeId}
