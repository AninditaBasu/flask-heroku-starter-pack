from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def first_page():
    return render_template('first_page.html')

@app.route('/response_page', methods = ['POST'])
def response_page():
    name = request.form['name']    
    return render_template('response_page.html', name=name)

if __name__ == "__main__":
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)
        #app.run()