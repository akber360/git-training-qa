from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField # We will only use StringField and SubmitField in our simple form.
from wtforms.validators import DataRequired, Length, ValidationError

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY' #Configure a secret key for CSRF protection.

class UserCheck:
    txt = (""" ! @ " ' '£ $ / \ , root admin sys """)
    x = txt.split() 
    def __init__(self, banned, message=None):# Here we set up the class to have the banned and message attributes. banned must be passed through at declaration.
        self.banned = banned
        if not message:
            message = 'Please choose another username' # If no message chosen, then this default message is returned.
        self.message = message

    def __call__(self, form, field):
    # Here we define the method that is ran when the class is called. If the data in our field is in the list of words then raise a ValidationError object with a message.
        if field.data.lower() in (x.lower() for x in self.banned): 
            raise ValidationError(self.message)
      
class myForm(FlaskForm):
    txt = (""" ! @ " ' '£ $ / \ , root admin sys """)
    x = txt.split()
    username = StringField('Username', validators=[
        DataRequired(),
        # We call our custom validator here, and pass through a message to override the default one. We pass through the list of banned usernames as a list.

        UserCheck(message="That username is not allowed", banned = x),
        Length(min=2,max=15)
        ])
    submit = SubmitField('Sign up')  

@app.route('/', methods=['GET','POST'])
def postName():
    form = myForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form = form, username=username)
    else:
        return render_template('home.html', form = form, username="") 
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')