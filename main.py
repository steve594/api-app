import requests
#Key
api_keys = "251e29fb7dc241848c84ea29dcb7b47f"

#Endpoints
api_url = "https://newsapi.org/v2/everything?q=tesla&from=2023-11-19&sortBy=publishedAt&apiKey=251e29fb7dc241848c84ea29dcb7b47f"

request = requests.get(api_url)

#Get a dictionary with data
display_content = request.json()

#Access the article titles, description and author
for articles in display_content["articles"]:
    print(articles["description"])
    print(articles["title"])
    print(articles["author"])
