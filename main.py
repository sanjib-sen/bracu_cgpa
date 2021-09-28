from flask import Flask, render_template, request

app = Flask(__name__)

count = None
cgpa = None
credits = None

@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template("index.html")

def calculate(cgpa, credits, count, gpas):
    courses = credits
    cgpa = cgpa*courses
    for a in gpas:
        cgpa+=a
    return round(cgpa/(courses+count),3)

@app.route('/courses', methods=['POST'])
def courses():
    if request.method == 'POST':
        global count, cgpa, credits
        try:
            count = int(request.form['coursecount'])
            cgpa = float(request.form['cgpa'])
        except:
            return render_template("error.html")
        credits = int(request.form['credits'])
        return render_template("courses.html", count=count)


@app.route('/result', methods=['POST'])
def resultshow():
    if request.method == 'POST':
        global count, cgpa, credits
        gpas = []
        for i in range(1, count+1):
            gpas.append(float(request.form['gpa'+str(i)]))
        result = calculate(cgpa, credits, count, gpas)
        return render_template("result.html", result = result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="8080")
