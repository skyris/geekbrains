
from grab import Grab, UploadFile
import json

HW_URL = 'https://geekbrains.ru/api/v2/lessons/3107/homeworks'

def login(g, auth):
    g.go('https://geekbrains.ru/login')
    g.doc.set_input_by_id('user_email', auth['login'])
    g.doc.set_input_by_id('user_password', auth['password'])
    g.doc.submit()


def post_hw(g, filename):
    g.setup(url=HW_URL, multipart_post={"data[attachment]": UploadFile(filename) } )
    g.request()


auth = {}
with open('fakeauth.json') as f:
    res = f.read()
    auth = json.loads(res)

g = Grab()
g.setup(connect_timeout=20, timeout=20)

login(g, auth)
print(g.response.code)    

post_hw(g, 'xxx.zip')
print(g.response.code)    


