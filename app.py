from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
##from wtforms.widgets import TextArea, NumberInput
##from wtforms import StringField, IntegerField

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
app.app_context().push()

##class DogEntryForm(Form):
##    firstName = StringField('Their Name', widget=TextArea())
##    age = IntegerField('Enter Age', widget=NumberInput())
##    location = StringField('Enter a location', widget=TextArea())
##    activity1 = StringField('Enter an activity', widget=TextArea())
##    activity2 = StringField('Enter another activity', widget=TextArea())
#    activity3 = StringField('Again, please ENTER another activity', widget=TextArea())
#    adjective = StringField('Please enter an adjective', widget=TextArea())
#    number = IntegerField('Please enter a random number', widget=NumberInput())
#    number1 = IntegerField('Please enter another random number', widget=NumberInput())
#    tvShow = StringField('Please enter a TV Show', widget=TextArea())
#    aspectTvShow = StringField('Please enter a favorite aspect of the TV Show', widget=TextArea())
#    favoriteSnack = StringField('Please enter a snack.', widget=TextArea())
##    religion = StringField('Please enter a religion or agnostic', widget=TextArea())
##    favoriteDrink = StringField('Please enter a random beverage', widget=TextArea())
##    favoriteStatement = StringField('Please enter a random quote or statement', widget=TextArea())


class DogDatabase(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.now)
    firstName = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, default=0)
    location = db.Column(db.String(200), nullable=False)
    activity1 = db.Column(db.String(200), nullable=False)
    activity2 = db.Column(db.String(200), nullable=False)
    activity3 = db.Column(db.String(200), nullable=False)
    adjective = db.Column(db.String(200), nullable=False)
    number = db.Column(db.Integer, default=0)
    number1 = db.Column(db.Integer, default=0)
    tvShow = db.Column(db.String(200), nullable=False)
    aspectTvShow = db.Column(db.String(200), nullable=False)
    favoriteSnack = db.Column(db.String(200), nullable=False)
    religion = db.Column(db.String(200), nullable=False)
    favoriteDrink = db.Column(db.String(200), nullable=False)
    favoriteStatement = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id, self.firstName

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        dog_content = request.form['content']
        dog_task = DogDatabase(content=dog_content)

        try:
            db.session.add(dog_task)
            db.session.commit()
            return redirect("/")
        except:
            return 'There was an issue adding your distinguished doggie'
    else:
        dogs = DogDatabase.query.order_by(DogDatabase.date_created).all()
        return render_template('index.html', dogs=dogs)
    
@app.route('/delete/<int:id>')
def delete(id):
    dog_to_delete = DogDatabase.query.get_or_404(id)

    try:
        db.session.delete(dog_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting this doggie, stays forever I guess but try again."

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    dogs = DogDatabase.query.get_or_404(id)

    if request.method == 'POST':
        dogs.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating the distinguished dog'
    else:
        return render_template('update.html', dogs=dogs)

if __name__ == "__main__":
    app.run(debug=True)