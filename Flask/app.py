from flask import Flask, render_template, url_for, flash, redirect
import admin
from forms import SingUpForm, SingInForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'a747219fb0e4c41cad24ceca1de9355aeb007141cc6adf2a058fa24f6d3bc47c'
# print(app)


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Home', projects=admin.projects)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/singin', methods=['GET', 'POST'])
def singin():
    form = SingInForm()
    return render_template('singin.html', title='Sing in', form=form)

@app.route('/singup', methods=['GET', 'POST'])
def singup():
    form = SingUpForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}", 'success')
        return redirect(url_for('home'))
    return render_template('singup.html', title='Sing up', form=form)


# main function

if __name__ == "__main__":
    app.run(debug=True)