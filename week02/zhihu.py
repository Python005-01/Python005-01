# -*- coding: latin-1 -*-
import requests
"""
?????????15?
"""
def get_url_name():

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    header = {'user-agent': ua,
              'Referer': 'https://www.toutiao.com/ch/software/',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
              'Cookie': '_zap=922227e0-33af-411a-8b8f-88c2deca0428; _xsrf=bFhGR06gF7Qx7vBfePPvpE3r1pGP6vlc; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1607005774,1607005940,1607006074,1607043777; d_c0="AABRnpIQShKPTjpPF7oc3PMeYADxcl1N55s=|1606988045"; capsion_ticket="2|1:0|10:1607043924|14:capsion_ticket|44:NjMyZGIwOWViMTJhNGIzYjliODg4MjRiYWIxMjU4YWU=|3a524666e0cafb7ba53cf8bfce54f3b62e7e4b75064361a05326d4777bbde147"; q_c1=b825ee10fade420d8921a1c5c535649c|1606988299000|1606988299000; r_cap_id="MGJiMjMyZjljOWQ2NGY0NTk1YTcyM2NmOWU0ODg5OT?baidu|utmccn=(organic)|utmcmd=organic; __utmv=51854390.000--|3=entry_date=20201203=1; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1607043924|1607043773; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1607043926; SESSIONID=hWmQN3KsSNQkx1XBFNWjJ0YCGuHW5p7JOyTsoeLBGse; JOID=VFscAE8Dj4aDQWoyXwZY1_nff39CbtLh1Q1ccyZSxN3iPllvF7MFQtlGZTJSQX_Ao7Gxesegg7CiREYIcSq-T_U=; osd=UVESBkIGhYiFTG84UQBV0vPReXJHZNzn2AhWfSBfwdfsOFRqHb0DT9xMazRfRHXOpby0cMmmjrWoSkAFdCCwSfg=; l_n_c=1; n_c=1; __utmb=51854390.0.10.1607043787; __utmc=51854390'
              }
    # offset=0&count=15?????? offset???0?? limit??????15?
    myurl = 'https://www.zhihu.com/api/v4/questions/324665833/root_comments?order=normal&limit=15&offset=0&status=open'
    response = requests.get(myurl, headers=header)

    data = dict(response.json())

    for i in range(15):
        print(i+1, data['data'][i]['content'])


if __name__ == '__main__':
    get_url_name()

