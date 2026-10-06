from flask import Flask, render_template, request, redirect

app = Flask(__name__)

students = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/admission', methods=['GET', 'POST'])
def admission():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        course = request.form['course']
        students.append({'name': name, 'phone': phone, 'course': course})
        return redirect('/admin')
    return render_template('admission.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin')
def admin():
    return render_template('admin.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)