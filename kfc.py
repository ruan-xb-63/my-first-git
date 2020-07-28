# 如果动态加载数据是经过加密的 url="http://www.kfc.com.cn/kfccda/storelist/index.aspx"
# ajax请求 XHR是ajax请求包
# params是get请求封装参数  data是post请求封装参数
import requests
def main():
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    headers = {
        "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
    }
    data = {
        "cname":"",
        "pid":"",
        "keyword": "固始",
        "pageIndex": "1",
        "pageSize": "10",
    }
    response = requests.post(url=url,headers=headers,data=data)
    text = response.json()
    for i in text["Table1"]:
        print(i["addressDetail"])
if __name__ == '__main__':
    main()