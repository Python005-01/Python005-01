import requests
"""
今日头条任意话题评论前15条
"""
def get_url_name():

    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'
    header = {'user-agent': ua,
              'Referer': 'https://www.toutiao.com/ch/software/',
              'Cookie' : 'tt_webid=6901959953180952078; MONITOR_WEB_ID=b90698c6-b81a-4085-88cf-b8f0727d2451; s_v_web_id=verify_ki8wp0ny_alSftX7R_8yJQ_49au_90fr_j1Wr4gn3QteU; __ac_nonce=05fc8efaf00162a4d295c; __ac_signature=_02B4Z6wo00f011qYdtwAAIBBx2Zh-Vg-R.tanXJAAIl3brAQOMrevQPWT3LUF8YwID4hhpGU6j7n0xH1EyDLhiOOUlmWaqll9Ql7Uh3nLlomzjCfLcbpw1Hj4E.JBeHcfBTc3Ds7CikUV.Nve3; tt_scid=brMY7k8-FcfYMQPKSiqF8Yxxb9WETAkyB4SmUESWYji-CaiPxt2fJ.d3.7MZMnEv6110'
              }
    # offset=0&count=15这里参数代表 offset代表从0开始 count代表评论数量15条
    myurl = 'https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=0&count=15&group_id=6900889909318451716&item_id=6900889909318451716&_signature=_02B4Z6wo00d01a8AcrwAAIBDMv5lml20FYmvBXYAADQMw8nLCCOABznkrH.uedc-sc0htzjddzNqkofBIoNhObuylNiNFOG6VSzfuWn5x.n8OCm2Mm8ymqth-JgJrP.kuO3J7Ffv6lKgZHbPc5'
    response = requests.get(myurl, headers=header)
    data = dict(response.json())

    for i in range(15):
        print(i+1, data['data'][i]['comment']['text'])


if __name__ == '__main__':
    get_url_name()

