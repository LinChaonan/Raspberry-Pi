
# coding=utf-8

import sys
import json
import base64


# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus

# 防止https证书校验不正确
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

API_KEY = 'gwApQmoc2RVqKFR1VKpRBrsY'

SECRET_KEY = 'NGQPl96krboAGCqRftoiCf8LLbQHRn83'


IMAGE_RECOGNIZE_URL = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"


"""  TOKEN start """
TOKEN_URL = 'https://aip.baidubce.com/oauth/2.0/token'


"""
    获取token
"""
def fetch_token():
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        result_str = f.read()
    except URLError as err:
        print(err)
    if (IS_PY3):
        result_str = result_str.decode()

    result = json.loads(result_str)

    if ('access_token' in result.keys() and 'scope' in result.keys()):
        if not 'brain_all_scope' in result['scope'].split(' '):
            print ('please ensure has check the  ability')
            exit()
        return result['access_token']
    else:
        print ('please overwrite the correct API_KEY and SECRET_KEY')
        exit()

"""
    读取文件
"""
def read_file(image_path):
    f = None
    try:
        f = open(image_path, 'rb')
        return f.read()
    except:
        print('read image file fail')
        return None
    finally:
        if f:
            f.close()

"""
    调用远程服务
"""
def request(url, data):
    req = Request(url, data.encode('utf-8'))
    has_error = False
    try:
        f = urlopen(req)
        result_str = f.read()
        if (IS_PY3):
            result_str = result_str.decode()
        return result_str
    except  URLError as err:
        print(err)

"""
    调用图片识别接口并打印结果
"""
def print_result(filename, url):
    # 获取图片
    file_content = read_file(filename)

    response = request(url, urlencode(
        {
            'image': base64.b64encode(file_content),
            'top_num': 1
        }))
    result_json = json.loads(response)

    # 打印图片结果
    for data in result_json["result"]:
        try:
            print(u"  垃圾名称: " + data["keyword"])
            global Name 
            Name = data["keyword"]
        except:
            print("未查询到物体")
        break

    #查询垃圾类别
    import requests
    URL="https://service.xiaoyuan.net.cn/garbage/index/search?kw="+Name
    res = requests.get(URL)
    result = json.loads(res.text)  # 字符串转字典

    # 打印图片分类
    for i in result["data"]:
        try:  
            print(u"  垃圾分类: " + i["category"])
        except:
            print("未查询到分类")
        break

if __name__ == '__main__':

    # 获取access token
    token = fetch_token()

    # 拼接图像识别url
    url = IMAGE_RECOGNIZE_URL + "?access_token=" + token

    # 垃圾图1
    print("垃圾类型")
    print_result("./1.png", url)
'''
    # 垃圾图3
    print("垃圾2")
    print_result("./2.jpg", url)

    # 垃圾图3
    print("垃圾3")
    print_result("./3.jpg", url)
'''