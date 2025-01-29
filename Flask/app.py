from flask import Flask, render_template, url_for
import admin

app = Flask(__name__)


# print(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home', projects=admin.projects)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/singin')
def singin():
    return render_template('singin.html', title='Sing in')

@app.route('/singup')
def singup():
    return render_template('singup.html', title='Sing up')



# main function

if __name__ == "__main__":
    app.run(debug=True)