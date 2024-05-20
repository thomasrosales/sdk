import random

from sdk.client import Client, client
from sdk.modules.posts import PostData
from sdk.modules.users import UserData


if __name__ == "__main__":

    users = client.users.all()
    print(users)
    post1 = client.posts.retrieve(1000)
    print(post1)
    post_to_be_created = [
        PostData(
            userId=1,
            title=f"Post-{index}",
            body=f"My body {index}",
        )
        for index in range(10)
    ]

    posts = client.posts.create_bulk(post_to_be_created)
    print(posts)

    """
    # users = client.users.list()
    user = client.users.retrieve(1, raise_on_failure=True)
    post = user.posts.list()[0]

    post3 = client.posts.retrieve(1000, raise_on_failure=True)

    post1 = client.posts.retrieve(1)
    post2 = client.posts.retrieve(4)
    print(post1.comments.list())
    print(post2.comments.list())

    # print(client.todos.retrieve(197))
    """
