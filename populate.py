from main import Post, User, session

new_user = User(
    username="test_user",
    email="tugrp@example.com"
    
)

session.add(new_user)
session.commit()
