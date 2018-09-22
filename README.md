# BoardAttachments

This project is a proof of concept for printing all cards on a given board that have attachments

# How does it work?

It uses the Trello api and the python requests library to make a request, deserialize it into an object, traverse all cards and only print the names of those cards with attachments.

# How to set up the project:

1. Make sure you have Python v2.6 or greater installed on your machine (I used version Python 2.7.10)
1. Clone the project
1. Pick your favorite Python IDE and import the project (I used PyCharm Community Edition)
1. Make sure requests is pulled down on your machine (pip install requests)
1. Fill in the variables in BoardAttachments.py
    - api_key can be found [here](https://trello.com/app-key) at the top of the page
    - oauth_token can be found on the same page where you see the hyperlink for "Token" (You will have to hit allow to get the token)
    - board_id can be any board id (found in other api calls not included in this project)
1. Run BoardAttachments.py once the variables are filled in and you should see it print all of the names for cards on the board that have 1 or more attachments