from collections import defaultdict, deque
from typing import DefaultDict, NamedTuple, Optional, List
import time
from pprint import pprint
from itertools import islice
from heapq import merge
import sys

User = str
Post = NamedTuple('Post', [('user', str), ('text', str), ('timestamp', float)])
posts = deque()             # type: dequeue
user_posts = defaultdict(deque) # type: DefaultDict[User, dequeue]
following = defaultdict(set)
followed = defaultdict(set)

def post_message(text: str, user: User, timestamp: float=None) -> None:
    user = sys.intern(user)
    timestamp = timestamp or time.time()
    post = Post(user, text, timestamp)
    posts.appendleft(post)
    user_posts[user].appendleft(post)


def follow(user: User, followed_user: User) -> None:
    user, followed_user = sys.intern(user),  sys.intern(followed_user)
    following[user].add(followed_user)
    followed[followed_user].add(user)


def post_by_user(user: User,limit: Optional[int]=None) -> List[User]:
    posts = user_posts[user]
    return list(islice(posts, limit))


def posts_for_user(user: User, limit : Optional[int] = None) -> List:
    relevant_posts = merge(
        *[user_posts[followed_user] for followed_user in following[user]], reverse=True,
        key=lambda post : post.timestamp
    )
    return list(islice(relevant_posts, limit))


def search(search_text: str, limit= None) -> List[Post]:
    return list(
        islice(
            (post for post in posts if search_text in post.text), # gen expression
            limit)
    )


if __name__ == '__main__':
    post_message(user= 'guido', text= 'i invented python #python')
    time.sleep(1)
    post_message(user= 'guido', text= 'i love python #python')
    time.sleep(1)
    post_message(user= 'shashank', text= 'i am a fan of python #python')
    time.sleep(1)
    post_message(user= 'raymondh', text= 'i teach modern python course #python')
    time.sleep(1)
    post_message(user= 'raymondh', text= 'i am a great teacher')

    #pprint(posts)
    follow('shashank', 'raymondh')
    follow('shashank', 'guido')
    #print(followed)
    #print(following)
    #pprint(post_by_user('shashank'))
    #pprint(posts_for_user('shashank'))
    pprint(search('fan'))
