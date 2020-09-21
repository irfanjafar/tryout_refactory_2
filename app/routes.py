from app import app
# from app.controllers import controllerRoute

# @app.route('/ctr')
# def tesctr():
#     return controllerRoute.fungsiController()

# @app.route('/ctr/')
# @app.route('/ctr/<parameter>')
# def tesctrParameter(parameter="kosong"):
#     return controllerRoute.fungsiControllerParameter(parameter)


@app.route('/')
def index():
    return "hello world"

# @app.route('/users/')
# def tesParameter1():
#     return "ini users"

# @app.route('/user/<name>')
# @app.route('/user/')
# def tesParameter(name="kosong"):
#     return f"Hello,{name}!"