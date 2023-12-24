from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs 10,00,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs 20,00,000'
}, {
    'id': 3,
    'title': 'Frontend developer',
    'location': 'Remote'
}, {
    'id': 1,
    'title': 'Backend Engineer',
    'location': 'Pune, India',
    'salary': 'Rs 100,00,000'
}]


@app.route('/')
def hello_world():
  company_name = 'Horixons'
  return render_template('home.html', jobs=JOBS, company_name=company_name)


@app.route('/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
