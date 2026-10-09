# AWS Flask Student Registration Project

## Project Overview

This project is a web-based student registration application developed using Python Flask and deployed on Amazon Web Services (AWS).

## Technologies Used

* Python and Flask
* Amazon EC2
* Amazon RDS (MySQL)
* Amazon S3
* Gunicorn
* Nginx

## Features

* Student registration form
* Store student information in a MySQL database
* Upload and store student photos in Amazon S3
* Display registration success messages

## AWS Deployment

The Flask application runs on an Amazon EC2 instance. Gunicorn serves the application locally, and Nginx acts as a reverse proxy for HTTP traffic. Amazon RDS stores student records, while Amazon S3 stores uploaded photos.

## Application Access

The deployed application was tested using the EC2 public IP address over HTTP.

## Security Notes

Database passwords and other credentials should be stored in environment variables and must not be committed to GitHub.

## Repository Contents

* `app.py` — Flask application
* `requirements.txt` — Python dependencies
* `.gitignore` — Files excluded from Git tracking

## Author

Devika T. S.
