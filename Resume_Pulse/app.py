from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, configure_uploads, DOCUMENTS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///networking.db'
app.config['UPLOADED_RESUMES_DEST'] = 'uploads/resumes'

db = SQLAlchemy(app)
resumes = UploadSet('resumes', DOCUMENTS)
configure_uploads(app, resumes)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    career_path = db.Column(db.String(50))

class NetworkingGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    career_path = db.Column(db.String(50))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'resume' not in request.files:
        return jsonify({'message': 'No file part'})
    
    resume = request.files['resume']
    resume_path = f'uploads/resumes/{resume.filename}'
    resume.save(resume_path)
    # Resume parsing logic can be added here
    
    return jsonify({'message': 'Resume uploaded successfully'})

@app.route('/select_career_path', methods=['POST'])
def select_career_path():
    selected_career_path = request.form.get('career_path')
    # Logic to store selected career path in session or database
    return jsonify({'message': 'Career path selected successfully'})

@app.route('/get_groups')
def get_groups():
    # Logic to retrieve networking groups based on selected career path
    return jsonify({'groups': groups_data})

if __name__ == '__main__':
    app.run(debug=True)
