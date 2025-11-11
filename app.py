from flask import Flask, render_template, jsonify, request, redirect, url_for
from database import Job, SessionLocal, init_db

app = Flask(__name__)

with app.app_context():
    init_db()


@app.route('/')
def hello_world():

    db = SessionLocal()
    jobs = db.query(Job).all()
    jobs_list = [job.to_dict() for job in jobs]
    db.close()

    return render_template('home.html', jobs=jobs_list, company_name="X")


@app.route('/api/jobs')
def job_list():

    db = SessionLocal()
    jobs = db.query(Job).all()
    jobs_list = [job.to_dict() for job in jobs]
    db.close()

    return jsonify(jobs_list)


@app.route('/api/jobs/add', methods=['POST'])
def add_job():

    data = request.get_json()

    db = SessionLocal()
    try:
        new_job = Job(
            title=data.get('title'),
            location=data.get('location'),
            salary=data.get('salary')
        )
        db.add(new_job)
        db.commit()
        db.refresh(new_job)

        return jsonify({
            'success': True,
            'job': new_job.to_dict()
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400
    finally:
        db.close()


@app.route('/admin')
def admin_panel():

    return render_template('admin.html')


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