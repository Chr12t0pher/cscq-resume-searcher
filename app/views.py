import json
from flask import render_template, request, make_response
from app import app, db
from app.models import Comments, Keywords


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")


@app.route("/search/", defaults={"page": 1}, methods=["GET", "POST"])
@app.route("/search/<int:page>")
def search(page):
    if request.method == "POST":
        keywords = request.form.getlist("item")
    elif request.cookies.get("search"):
        keywords = json.loads(request.cookies.get("search"))
    else:
        return "Cookies must be enabled, I can't be bothered to code it properly :D"
    query = Comments.query
    for keyword in keywords:
        query = query.filter(Comments.keywords.any(Keywords.keyword == keyword))
    output = query.order_by(Comments.id.desc()).paginate(page, 8)
    response = make_response(render_template("search.html", paginated=output))
    response.set_cookie("search", json.dumps(keywords))
    return response


@app.route("/about")
def about():
    return render_template("about.html")
