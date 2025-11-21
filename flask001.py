from flask import Flask,request,jsonify



app = Flask(__name__)
@app.route("/index",methods=["GET","POST"])#路由后面加上methods可以添加请求类型

def index():
    age = request.args.get('age')#路由中体现参数
    height = request.args.get('height')
    print(age,height)

    xx = request.form.get("xx")
    yy = request.form.get("yy")#请求体中传参数
    print(xx,yy)

    aa = request.json.get("aa")
    bb = request.json.get("bb")#请求体中传参数，但是参数格式为json格式
    print(aa,bb,type(request.json))
    return jsonify({"hello":True, "world":333})
    #再给用户返回数据时，一般以json格式返回，有两
    # 种方法，第一种可以在return后面
    # 跟.json.dump加上要返回的字典形式的数据，除了这样还可
    # 以导入python的jsonify模块，可以将字典数据格式化为字符串形式的json格式数据






@app.route("/home")
def home():
    return "成功"
if __name__ == '__main__':
    app.run()
