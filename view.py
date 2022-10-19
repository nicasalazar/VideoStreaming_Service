from flask import Flask, request, Response, render_template
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Vid

app = Flask(__name__)
# SQLAlchemy config. Read more: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vid.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route("/", methods=["GET", "POST"])
def patient_info_page():
     if request.method == "GET":
         return render_template("view.html")


@app.route('/<int:id>')
def get_vid(id):
    vid = Vid.query.filter_by(id=id).first()
    if not vid:
        return 'Video Not Found!', 404

    return Response(vid.vid, mimetype=vid.mimetype)

if __name__ == '__main__':
    app.run(port=5002)