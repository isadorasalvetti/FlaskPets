from flask import Flask, render_template, flash, redirect, url_for
from forms.user_forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "bad key"

@app.route("/")
def main():
    return render_template('base.html')


@app.route("/login.html")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)


@app.route("/signup.html", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Accounted created for {form.username.data}.", "success")
        return redirect(url_for("login"))
    return render_template('signup.html', title="SignUp", form=form)


if __name__ == "__main__":
    app.run(debug=True)


