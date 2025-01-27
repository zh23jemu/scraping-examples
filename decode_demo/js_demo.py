import execjs  # pip install PyExecJS2

with open('js_demo.js', 'r', encoding='UTF-8') as file:
    js_code = file.read()

ctx = execjs.compile(js_code)
print(ctx.call('add', 3, 5))
