import requests

# Authorization code 획득
'''
'''

# Access Token 획득
def getAccessCode():
    url = 'https://www.tistory.com/oauth/access_token?'

    param = {
        'client_id':'',
        'client_secret':'',
        'redirect_uri':'http://arg-dev.tistory.com/',
        'code':'',
        'grant_type':'authorization_code'
    }

    response = requests.get(url, params=param)
    print(response.url)
    print(response.text)

# 블로그 포스팅 함수
def postBlogAPI(title, content):
    url = 'https://www.tistory.com/apis/post/write?'

    param = {
        'access_token':'',
        'blogName':'arg-dev',
        'title':title,
        'content':content,
        'visibility':'0',
        'category':'0',
        'tag':'tag',
        'acceptComment':'1',
        'password':''
    }

    response = requests.post(url, params=param)
    print(response.text)



# getAccessCode()
postBlogAPI('')
