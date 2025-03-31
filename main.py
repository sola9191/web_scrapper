from flask import Flask, render_template, request
import wanted_scrapper

app = Flask("__name__")

@app.route('/')
def home():
    return render_template("home.html", name="sola")
@app.route('/search')
def search():
    keyword = request.args.get("keyword")
    test = wanted_scrapper.Web_scrapper(keyword)
    jobs = test.get_job_data(keyword)
    return render_template("search.html", keyword=keyword, jobs=jobs)

app.run(debug=True)