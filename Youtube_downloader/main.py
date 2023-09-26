# import package
from flask import Flask,render_template,request
import yt_dlp

app = Flask(__name__)

@app.route("/",methods=(["GET"]))
def homepage():
    return render_template("index.html")

@app.route("/geturl",methods=(["GET","POST"]))
def download_video():

    # get url from client
    input_url = request.form.get('url')

    ydl_opts = {}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([input_url])

    return "video downloaded successfully"

app.run(debug=True)

