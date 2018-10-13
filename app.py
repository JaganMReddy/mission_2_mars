# Dependencies
from flask import Flask, jsonify, render_template, request, redirect
import pymongo
import scrape_mars

app = Flask(__name__)
# Mongo connection
conn = 'mongodb://localhost:27017'

client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def index():
    mars_info = db.mars_data_entries.find_one()

    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scrape():
    mars_info = db.mars_data_entries
    mars_data = scrape_mars.Scrape()
    mars_info.update(
        {},
        mars_data,
        upsert = True
    )

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=False, port=5016)