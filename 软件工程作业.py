import requests
import  time

url='https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/8775accd-a4cf-4b03-9748-40ca4dd12194'
header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
url1=requests.get(url,headers=header)
shangpin=url1.json()
# print(shangpin)
print('------------商品:'+shangpin['data']['name']+'-------------')
print('规格:'+shangpin['data']['spec'])
print('价格:'+str(shangpin['data']['price']/100))
print('折扣价/原价:'+str(shangpin['data']['market_price']/100))
print('详细内容'+shangpin['data']['share_content'])
print('------------商品:'+shangpin['data']['name']+'产品的价格波动-------------')
for i in range(5):
    url = 'https://j1.pupuapi.com/client/product/storeproduct/detail/7c1208da-907a-4391-9901-35a60096a3f9/8775accd-a4cf-4b03-9748-40ca4dd12194'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36'}
    url1 = requests.get(url, headers=header)
    print('当前时间为：%s，价格为%s'%(time.strftime('%y-%M-%d %H:%m:%S',time.localtime()),str(url1.json()['data']['price']/100)))



