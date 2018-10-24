from flask import Flask, render_template, request, redirect, session
app = Flask (__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    count = 1
    session['count'] = session['count'] + count
    return render_template("index.html", sCount=session['count'])

@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.clear()
    count = 0
    session['count'] = count
    return redirect('/')

@app.route('/count2', methods=['POST'])
def count_2():
    count = 1
    session['count'] = session['count'] + count
    return redirect('/')
    
if __name__=="__main__":
    app.run(debug=True)
