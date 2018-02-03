#coding=utf-8
import json
import urllib,urllib2

BING_API_KEY='ab303bb10f974eb9847f0323c1541975'
headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': 'ab303bb10f974eb9847f0323c1541975',
}
def run_query(search_terms):
    #确定我们希望每页返回的结果
    #缓冲区决定了结果队列的开始
    #假如每页有10个 结果 offset为11 那就从第二页开始显示
    root_url='https://api.datamarket.azure.com/Bing/SearchWeb/v1/'
    # root_url='https://api.datamarket.azure.com/Bing/Search/v1/Web?Query=%27rango%27'
    source = 'Web'
    result_per_page=10
    offset=0

    ##给bing 提交的数据需要 有'' 所以对提交格式进行处理
    query="'{0}'".format(search_terms)
    query=urllib.quote(query)
    ##对请求的url进行构建
    search_url="{0}{1}?$format=json&top={2}&skip={3}&Query={4}"\
        .format(root_url,source,result_per_page,offset,query)
    #用户名 为空
    username=''
    #生成一个 密码管理者 来处理权限
    password_mgr=urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None,search_url,username,BING_API_KEY)
    print(search_url)
    #结果队列
    results=[]
    #准备好连接数据库
# try:
    handler=urllib2.HTTPBasicAuthHandler(password_mgr)
    opener=urllib2.build_opener(handler)
    urllib2.install_opener(opener)
#连接到服务器 得到回应的值
    response=urllib2.urlopen(search_url).read()
#将回应的字符串转成字典
    json_response=json.loads(response)
    for result in json_response['d']['result']:
        results.append({'title':result['Title'],
                        'link':result['URL'],
                        'summary':result['Description']})
# except urllib2.URLError as e:
#     print('出现了错误 在访问api时',e)

    return  results



if __name__ == '__main__':
    run_query('樊佳亮')


