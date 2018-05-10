from flask import Flask, render_template
from app.api.user import bp as user_bp
from app.api.question import bp as question_bp

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(user_bp)
app.register_blueprint(question_bp)


@app.route('/')
def sample_route():
    return render_template('index.html')
