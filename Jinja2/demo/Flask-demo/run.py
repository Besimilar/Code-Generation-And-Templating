from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/simple")
def simple():
    return render_template('simple.html', my_string="simple test!",
        my_list=[0,1,2,3,4,5])


@app.route("/inheritance")
def inheritance():
    return render_template('template.html', my_string="Template inheritance",
        my_list=[6,7,8,9,10,11])


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    # app.run(debug=True)
