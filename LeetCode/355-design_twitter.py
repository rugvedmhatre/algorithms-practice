"""

https://leetcode.com/problems/design-twitter/

Design a simplified version of Twitter where users can post
tweets, follow/unfollow another user, and is able to see the
10 most recent tweets in the user's news feed.

Implement the Twitter class:
- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new 
  tweet with ID tweetId by the user userId. Each call to 
  this function will be made with a unique tweetId.
- list<Integer> getNewsFeed(int userId) Retrieves the 10 
  most recent tweet IDs in the user's news feed. Each item in
  the news feed must be posted by users who the user followed
  or by the user themself. Tweets must be ordered from most
  recent to least recent.
- void follow(int followerId, int followeeId) The user with
  ID followerId started following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with
  ID followerId started unfollowing the user with ID followeeId.


Example 1:
Input
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", 
  "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output
[null, null, [5], null, null, [6, 5], null, [5]]
Explanation
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return 
                         // a list with 1 tweet id -> [5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list
                         // with 2 tweet ids -> [6, 5]. Tweet id 6 
                         // should precede tweet id 5 because it is 
                         // posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list
                         // with 1 tweet id -> [5], since user 1 is 
                         // no longer following user 2.


Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, 
  getNewsFeed, follow, and unfollow.

"""

from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time, tweetId])
        self.time -= 1

    def getNewsFeed(self, userId: int) -> list[int]:
        result = []
        minHeap = []

        if userId not in self.following[userId]:
            self.following[userId].add(userId)
        
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:
                currentIdx = len(self.tweets[followeeId]) - 1
                postTime, tweetId = self.tweets[followeeId][currentIdx]
                minHeap.append([postTime, tweetId, followeeId, currentIdx - 1])
        
        heapq.heapify(minHeap)

        while minHeap and len(result) < 10:
            postTime, tweetId, followeeId, nextIdx = heapq.heappop(minHeap)
            result.append(tweetId)
            if nextIdx >= 0:
                postTime, tweetId = self.tweets[followeeId][nextIdx]
                heapq.heappush(minHeap, [postTime, tweetId, followeeId, nextIdx - 1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)

if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print(twitter.getNewsFeed(1))
    twitter.follow(1, 2) 
    twitter.postTweet(2, 6)
    print(twitter.getNewsFeed(1))
    twitter.unfollow(1, 2)
    print(twitter.getNewsFeed(1))