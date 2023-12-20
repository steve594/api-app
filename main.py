import requests
from email_sender import email_sender
#Key
api_keys = "your api key"

#Endpoints
api_url = "url"

#Make request
request = requests.get(api_url)

#Get a dictionary with data
display_content = request.json()

#Access the article titles and description
body = ""
for article in display_content["articles"]:
    if article["title"] is not None:
        body = "Subject: Today's news" +"\n" +body + article["title"] + "\n" \
               + article["description"] + 2*"\n"

body = body.encode("utf-8")
email_sender(message=body)

