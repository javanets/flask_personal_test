from flask import Flask, redirect, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ldjflkjdaf_lkjadlfkj_akldjflkjaflkjadljf'


class TestForm(FlaskForm):
    cats_answer = RadioField(
        'Любите ли вы котиков?',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    prog_answer = RadioField(
        'Умеете ли вы программировать?',
        choices=[('yes', 'Да'), ('no', 'Нет')],
        validators=[DataRequired(message='Необходимо выбрать значение')]
    )
    submit = SubmitField('Узнать результат')


@app.route('/test', methods=['GET', 'POST'])
def test():
    form = TestForm()
    if form.validate_on_submit():
        return render_template(
            'result.html',
            cats=form.cats_answer.data,
            prog=form.prog_answer.data
        )
    return render_template('test.html', form=form)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
