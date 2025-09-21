from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # Handle form submission
        first_name = request.form.get('first_name')
        print(first_name)
        last_name = request.form.get('last_name')
        email = request.form.get('email')
        date = request.form.get('date')
        occupation = request.form.get('occupation')
        # Process the data as needed
    return render_template('index.html')

app.run(debug=True,port=5000)