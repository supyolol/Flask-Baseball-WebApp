from flask import Flask
from flask_login import LoginManager
from WebApp.User_Class import userClassid

def create_app():
    app = Flask(__name__,)

    app.config['SECRET_KEY'] = 'SECRET_KEY'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
        unicode_id = userClassid(user_id)
        return unicode_id


    from WebApp.views import views,auth


    app.register_blueprint(views.views, url_prefix='/')
    app.register_blueprint(auth.auth, url_prefix='/auth')



    return app


app = create_app()

if __name__ == '__main__':
    app.run(debug=False])