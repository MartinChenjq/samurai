from samurai import app
from samurai.route.user import user_bp

app.register_blueprint(user_bp)


@app.route('/hs')
def hs():
    import multiprocessing
    print(multiprocessing.cpu_count())
    return 'ok'
