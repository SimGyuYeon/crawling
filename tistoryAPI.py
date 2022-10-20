import requests

# Authorization code 획득
'''
https://www.tistory.com/oauth/authorize?client_id=48492a14fd2759d8e6e4fb354af01376&redirect_uri=https://arg-dev.tistory.com/&response_type=code
'''

# Access Token 획득
def getAccessCode():
    url = 'https://www.tistory.com/oauth/access_token?'

    param = {
        'client_id':'48492a14fd2759d8e6e4fb354af01376',
        'client_secret':'48492a14fd2759d8e6e4fb354af01376e22f24c9d233da2d4b40ed6830396d4dbb123d1e',
        'redirect_uri':'http://arg-dev.tistory.com/',
        'code':'28a7701de330290a330dd42e2d63b7092c96539d4d02bc88abaf1308dd1438e7767744a4',
        'grant_type':'authorization_code'
    }

    response = requests.get(url, params=param)
    print(response.url)
    print(response.text)

# 블로그 포스팅 함수
def postBlogAPI(title, content):
    url = 'https://www.tistory.com/apis/post/write?'

    param = {
        'access_token':'479630ae6cbc3902c835b167b723877f_ea84b113389aebe34341420875e8590b',
        'blogName':'arg-dev',
        'title':title,
        'content':content,
        'visibility':'0',
        'category':'0',
        'tag':'tag',
        'acceptComment':'1',
        'password':'2693'
    }

    response = requests.post(url, params=param)
    print(response.text)



# getAccessCode()
postBlogAPI('')
