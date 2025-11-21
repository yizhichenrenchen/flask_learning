"""
                                 这是flask笔记
1，主要格式
先导入flask包
app = Flask(__name__)

app.route("/xxx)路由，但是此种写法只支持get请求，可以在路由后面
加上.methods = ["GET","POST"]即可给请求方式增加post请求
然后开始定义函数以及要返回的内容
用户在请求时，参数可能会通过路由传过来，或者在请求体中传参
参数格式可能为form表单或者json格式，想要处理用户传过来的参数，分别可以
通过request.args.get(),括号内加上用户传参的键
form表单可以用request.form.get()括号内容同上
json格式可以用request.json.get()括号内容同上方法来解析用户传入的参数
当我们在给用户返回数据时，一般是以json格式返回，此时我们可
以使用return json.dump(内容为键值对)
或者导入jsonify,用return.jsonify()的格式，会格式化我们返回给用户的内容为
字符串格式的json数据
"""