from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        
        return f'{name}, your username is {username}'
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)