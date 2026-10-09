import os
import boto3
import pymysql
from flask import Flask, render_template, request

app = Flask(__name__)
bucket_name = os.environ.get("S3_BUCKET_NAME")

db = pymysql.connect(
    host=os.environ.get("DB_HOST"),
    port=3306,
    user=os.environ.get("DB_USER"),
    password=os.environ.get("DB_PASSWORD"),
    database=os.environ.get("DB_NAME", "studentdb"),
    connect_timeout=10
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    photo = request.files['photo']

    s3 = boto3.client('s3')
    s3.upload_fileobj(photo, bucket_name, photo.filename)

    photo_url = f"https://{bucket_name}.s3.amazonaws.com/{photo.filename}"

    with db.cursor() as cursor:
        sql = """
        INSERT INTO students (name, email, course, photo_url)
        VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (name, email, course, photo_url))

    db.commit()
    return "Student Registered Successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
