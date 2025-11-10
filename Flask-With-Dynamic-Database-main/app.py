from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {'job_id': 1, 'title': 'Cyber Security', 'location': 'Chicago', 'salary': 100000},
    {'job_id': 2, 'title': 'Backend Engineer', 'location': 'Remote', 'salary': 90000},
    {'job_id': 3, 'title': 'Frontend Engineer', 'location': 'San Francisco'},
    {'job_id': 4, 'title': 'Data Analytics', 'location': 'Pune', 'salary': 50000}
]

@app.route('/')
def hello_world():
    return render_template('home.html', jobs=JOBS, company_name="X")

@app.route('/api/jobs')
def job_list():
    return jsonify(JOBS)

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
