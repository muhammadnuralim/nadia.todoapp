from app import app
# @app.route("/")
# def serve():
#     return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
