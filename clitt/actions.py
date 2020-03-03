import tweepy

from .interface import show_message, show_tweet, show_user


def dm(api: tweepy.API, target: str, content: str):
    """
        Sends a direct message to target user

        Keyword arguments:
        api -- API instance for handling the request
        target -- Target user's screename (e.g. @jake/jake)
        content -- String that will be sent as message
    """

    target = target.replace("@", "")
    user = api.get_user(target)
    api.send_direct_message(user.id, content)


def search(api: tweepy.API, query: str, count: int):
    """
        Searches for tweets containing the input string

        Keyword arguments:
        api -- API instance for handling the request
        query -- String passed as search query for the API
        count -- Maximum number of results the API will return
    """

    results = api.search(query, count=count)
    for result in results:
        show_tweet(result)


def user(api: tweepy.API, query: str, count: int):
    """
        Searches for users related to the input string

        Keyword arguments:
        api -- API instance for handling the request
        query -- String passed as search query for the API
        count -- Maximum number of results the API will return
    """

    results = api.search_users(query, count=count)
    for user in results:
        show_user(user)


def post(api: tweepy.API, content: str):
    """
        Update the status for currently logged user (basically, this methods tweets)

        Keyword arguments:
        api -- API instance for handling the request
        content -- String that will be posted
    """

    api.update_status(content)


def chat(api: tweepy.API, user: str):
    """
        Search and displays private chat with target user

        Keyword arguments:
        api -- API instance for handling the request
        user -- Target user's screename (e.g. @jake/jake)
    """

    try:
        user = user.replace("@", "")
        user = api.get_user(user)
        me = api.me()
        messages = api.list_direct_messages(count=100)
        for message in sorted(
            messages, key=lambda message: int(message.created_timestamp)
        ):
            if int(message.message_create["sender_id"]) == user.id:
                show_message(message, user)
            if (
                int(message.message_create["sender_id"]) == me.id
                and int(message.message_create["target"]["recipient_id"]) == user.id
            ):
                show_message(message, me, reverse=True)
    except tweepy.TweepError:
        print("Sorry, user not found")


def read(api: tweepy.API, count: int):
    """
        Read currently logged user's timeline

        Keyword arguments:
        api -- API instance for handling the request
        count -- Maximum number of results the API will return
    """

    public_tweets = api.home_timeline(count=count)
    for tweet in public_tweets:
        show_tweet(tweet)
