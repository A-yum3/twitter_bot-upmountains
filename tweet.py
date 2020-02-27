import tweepy
import re
import os


def timeline_favo():
    consumer_key=os.environ["CONSUMER_KEY"]
    consumer_secret=os.environ["CONSUMER_SECRET"]
    access_token_key=os.environ["ACCESS_TOKEN_KEY"]
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True)

    get_to_timeline_tweet_count = 100

    public_tweets = api.home_timeline(count=get_to_timeline_tweet_count)

    favcount = 0
    words = ["ダーツ", "投げ"]

    print("--------------------------------------------------------")

    for tweet in public_tweets:
        print(tweet.text)
        for word in words:
            if re.search(word, tweet.text):
                try:
                    # リプライツイは無視する
                    if tweet.in_reply_to_user_id is None:
                        api.create_favorite(tweet.id)
                        print(tweet.user.name+"のツイートをファボしました。\n\n")
                        favcount += 1
                except Exception as e:
                    print(tweet.in_reply_to_user_id)
                    print("既に{}はファボしています\n".format(tweet.user.name))
                    print(e)
                    break


    print("合計{}件をファボしました。".format(favcount))
    print("---------------------------------------------------------")

# hashtag_words = ['#ダーツ初心者', '#ダーツ好きな人と繋がりたい']

# set_count = 10
# results = api.search(q=hashtag_words, count=set_count)

# for result in results:
#     username = result.user._json['screen_name']
#     user_id = result.id
#     print("ユーザーID："+str(user_id))
#     user = result.user.name
#     print("ユーザー名："+user)
#     tweet = result.text
#     print("ユーザーのコメント："+tweet)

#     try:
#         api.create_favorite(user_id) # favo
#         api.create_friendship(username) # follow
#         print(user+"をフォローと「いいね」をしました\n\n")
#     except:
#         print(user+"はもうフォローしてます\n\n")