import requests
from email_sender import email_sender
#Key
api_keys = "251e29fb7dc241848c84ea29dcb7b47f"

#Endpoints
api_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-20&sortBy=publishedAt&apiKey=251e29fb7dc241848c84ea29dcb7b47f"

#Make request
request = requests.get(api_url)

#Get a dictionary with data
display_content = request.json()

#Access the article titles and description
body = ""
for article in display_content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_sender(message=body)

