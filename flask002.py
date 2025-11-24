#本篇将对网站添加校验，基于文档
#创建一个文档将授权使用的客户的id进行记录
"""
本篇代码创建1个路由，且使用文档校验的方法对访问者进行校验，必须输入正确token才能调用
关键：创建路由，导入模块，注意导入模块时，flask包里面的模块可以通过逗号分割统一导入，其他模块需要单独导入
构造函数用来解析文档中的token，使用字典储存token及名字，遍历文档每一行可以使用字符串分割方法
分割用逗号分隔的token及名字，并将其分别赋值，用字典构造方法将其储存在已经创建好的字典中，整个函数返回字典
然后可以分开判断有没有token以及token值是否正确，通过判断有没有token以及token是否存在bd文档中判断，加上判断其有没有上传参数

"""
from flask import Flask,jsonify,request#导入需要的模块
import hashlib#导入需要的模块
def get_user_dict():#构建函数用来解析文档token
    info_dict = {}#创建字典用来储存解析的token和对应的名字
    with open("bd.txt","r",encoding= "utf-8") as f:#使用with方法安全打开文档
        for line in f:#遍历每一行
            line = line.strip()#此处使用字符串方法strip()方法用来清除每行首尾空格
            token,name  = line.split(",")#通过字符串方法split()方法分割字符串并将其分别赋值
            info_dict[token] = name#创建字典
    return info_dict#函数返回字典

app = Flask(__name__)

@app.route("/bili",methods=["POST"])#创建路由，此处加上限定条件，只能对我发送post请求

def bili():#创建函数
    token = request.args.get("token")#token变量用来储存用户请求路由中的token参数
    if not token:#没有传入token的情况下
        return jsonify({"status":False,"error":"未检测到token"})

    user_dict = get_user_dict()#变量指向get_user_dict()函数
    if token not in user_dict:#用户传了token参数，但不在文档中
        return jsonify({"status":False,"error":"token错误"})
    ordered_string = request.json.get("ordered_string")#变量获取用户传入的请求体参数
    if not ordered_string:#如果没有请求体
        return jsonify({"status":False,"error":"参数错误"})
    #以下为正常时的算法
    encrypt_string = ordered_string + "fueuiwhfgwiuhgfiuhweiufh"
    obj = hashlib.md5(encrypt_string.encode('utf-8'))
    sign = obj.hexdigest()
    return jsonify({"status":True,"date":sign})#返回给用户的参数

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)


"""
上文中提到了一个算法，此算法实际上工作内容为第一步将用
户传入的请求体的内容与一个固定字符串进行拼接，第二步创建哈希对象并对字符串进行编码
其中encrypt_string.encode('utf-8')的意思是将字符串转化为字节序列以方便MD5算法处理
最后将哈希值转化为更易读懂的16进制
"""