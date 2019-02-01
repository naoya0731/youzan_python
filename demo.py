import auth
from yzclient import YZClient
import requests
import json

client_id = ''
client_secret = ''
kdt_id = ''

def get_token(client_id, client_secret, kdt_id):
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    params = {'client_id': client_id, 'client_secret': client_secret, 'grant_type': 'silent', 'kdt_id': kdt_id}
    response = requests.post('https://open.youzan.com/oauth/token', headers=headers, data=params)
    data = response.json()
    if 'error' in data:
        return None
    else:
        access_token = data['access_token']
        return access_token    

if __name__ == '__main__':
    access_token = get_token(client_id, client_secret, kdt_id)
    if access_token == None:
        print("could not get token...")
    else:
        token = auth.Token(token=access_token)
        client = YZClient(token)
        response = client.invoke('kdt.shop.basic.get', '1.0.0', 'GET')
        print(response)
    # print yzclient.invoke('kdt.item.add', '1.0.0', 'POST', params={'title': 'pythongegege333', 'desc': 'new goods',
    #                                                                'price': '1.0', 'post_fee': '0.1'},
    #                       files=[
    #     ('images[]', ('foo.png', open('/Users/ph0ly/Desktop/3.pic.jpg', 'rb'), 'image/png')),
    #     ('images[]', ('bar.png', open('/Users/ph0ly/Desktop/thumb_up_normal.png', 'rb'), 'image/png'))])

    # 上传文件参数files为数组[]，格式形如： ('images[]', ('foo.png', open('/Users/ph0ly/Desktop/3.pic.jpg', 'rb'), 'image/png'))

