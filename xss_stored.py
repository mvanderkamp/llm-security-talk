from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.debug = True  # allow template reloads

# This acts as our "database"
messages = []

@app.route("/")
def index():
    # Only handles GET requests to display the page
    return render_template("xss_stored.html", messages=messages)


@app.route("/post", methods=["POST"])
def post_message():
    # Handles the data, then redirects the user away
    msg = request.form.get("message")
    if msg:
        messages.insert(0, msg)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(port=5000)

    # <img src="https://i1.sndcdn.com/artworks-x8zI2HVC2pnkK7F5-4xKLyA-t1080x1080.jpg" onload="alert('roll with it')" height=650 width=650>
