import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Local MongoDB
app.config["MONGO_URI"] = "mongodb://localhost:27017/obul_portfolio"

mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile_summary.html')

@app.route('/skills')
def skills():
    return render_template('technical_skills.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/softskills')
def softskills():
    return render_template('softskills.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    mongo.db.contacts.insert_one({
        "name": name,
        "email": email,
        "message": message
    })

    return redirect(url_for('contact_page'))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
