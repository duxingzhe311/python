import http.client  

class NetTool:
    @staticmethod
    def getInfo(url):
        conn = http.client.HTTPConnection("baidu.com")
        conn.request("GET", url, "", {})
        res = conn.getresponse()
        #code = res.getcode()
#         return res.readall()
#         return res.readlines()
        return res.readall()
       
res = NetTool.getInfo("http://www.baidu.com")
print(res)