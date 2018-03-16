
#-*- coding: UTF-8 -*-
from urllib import request
from urllib import parse
import chardet  
import json

if __name__ == "__main__":
    Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    Form_Data ={}
    Form_Data['i'] = '傻狗阿淮'
    Form_Data['form'] = 'AUTO'
    Form_Data['to'] = 'AUTO' 
    Form_Data['smartresult'] = 'dict'
    Form_Data['client'] = 'fanyideskweb'
    Form_Data['salt'] = '1521168663843'
    Form_Data['sign'] = 'af916783b846c8f77ba8ecc3a733bfe0'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['action'] = 'FY_BY_REALTIME'

    data = parse.urlencode(Form_Data).encode('utf-8')
    response = request.urlopen(Request_URL,data)
    html = response.read().decode('utf-8')
    translate_results = json.loads(html)
    translate_results = translate_results['translateResult'][0][0]['tgt']
    print("翻译的结果是：%s" % translate_results)


# -*- coding: UTF-8 -*-
# from urllib import request
# from urllib import parse
# import json

# if __name__ == "__main__":
#     #对应上图的Request URL
#     Request_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
#     #创建Form_Data字典，存储上图的Form Data
#     Form_Data ={}
#     Form_Data['i'] = '傻狗阿淮说不就不'
#     Form_Data['form'] = 'AUTO'
#     Form_Data['to'] = 'AUTO' 
#     Form_Data['smartresult'] = 'dict'
#     Form_Data['client'] = 'fanyideskweb'
#     Form_Data['salt'] = '1521168663843'
#     Form_Data['sign'] = 'af916783b846c8f77ba8ecc3a733bfe0'
#     Form_Data['doctype'] = 'json'
#     Form_Data['version'] = '2.1'
#     Form_Data['keyfrom'] = 'fanyi.web'
#     Form_Data['action'] = 'FY_BY_REALTIME'

#     data = parse.urlencode(Form_Data).encode('utf-8')
#     response = request.urlopen(Request_URL,data)
#     html = response.read().decode('utf-8')
#     translate_results = json.loads(html)
#     translate_results = translate_results['translateResult'][0][0]['tgt']
#     print("翻译的结果是：%s" % translate_results)