from flask import Flask, render_template
app = Flask(__name__)

@app.route("/index.html")
def home():
    return render_template('index.html')

#about page
@app.route('/about.html')
def about():
    return render_template('about.html')

#post page
@app.route('/post.html')
def post():
    return render_template('post.html')

#contact.html
@app.route('/contact.html')
def contact():
    return render_template('contact.html')


app.run(debug=True)