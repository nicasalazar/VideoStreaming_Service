from flask import Flask, request, Response, render_template
from werkzeug.utils import secure_filename

from db import db_init, db
from models import Vid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vid.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db_init(app)

@app.route('/upload')
def hello_world():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    if not video:
        return 'No video uploaded!', 400

    filename = secure_filename(video.filename)
    mimetype = video.mimetype
    if not filename or not mimetype:
        return 'Bad upload!', 400

    vid = Vid(vid=video.read(), name=filename, mimetype=mimetype)
    db.session.add(vid)
    db.session.commit()

    return 'Video Uploaded!', 200

if __name__ == '__main__':
    app.run(port=5001)