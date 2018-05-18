from flask import Flask, render_template
from app.api.user import bp as user_bp
from app.api.question import bp as question_bp
from flask_admin import Admin
from app.admin import admin_session, ModelView, User, Question


app = Flask(__name__)
app.config.from_object('config')

admin = Admin(app, name='Admin-Panel', template_mode='bootstrap3')
admin.add_view(ModelView(User, admin_session))
admin.add_view(ModelView(Question, admin_session))

app.register_blueprint(user_bp)
app.register_blueprint(question_bp)


@app.route('/')
def sample_route():
    return render_template('index.html')
