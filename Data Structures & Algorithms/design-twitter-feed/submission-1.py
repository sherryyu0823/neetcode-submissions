class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list) #Key=userId, Value=List of (time, tweetId)
        self.follows = defaultdict(set)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append((-self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        news = []
        followers = self.follows[userId].copy()
        followers.add(userId)
        for users in followers:
            news.extend(self.posts[users])
        heapq.heapify(news)
        feeds = []

        while news and len(feeds)<10:
            tid = heapq.heappop(news)
            feeds.append(tid[1])

        return feeds


    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.follows[followerId].discard(followeeId)
