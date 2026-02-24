from flask import Flask, redirect, request, render_template_string, url_for

app = Flask(__name__)

# This acts as our "database"
messages = []

# The HTML template (VULNERABLE)
# We use |safe in Jinja2 to explicitly tell it NOT to escape HTML.
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Vulnerable Guestbook</title>
    <style>body { font-family: sans-serif; margin: 40px; line-height: 1.6; }</style>
</head>
<body>
    <h1>Vulnerable Guestbook</h1>
    <p>Submit a message. HTML is allowed (and dangerous!)</p>

    <form method="POST" action="/post">
        <input type="text" name="message" placeholder="Type something..." required>
        <button type="submit">Post Message</button>
    </form>

    <hr>
    <h3>Stored Messages:</h3>
    <ul>
        {% for msg in messages %}
            <li>{{ msg | safe }}</li>
        {% endfor %}
    </ul>
</body>
</html>
'''


@app.route('/')
def index():
    # Only handles GET requests to display the page
    return render_template_string(HTML_TEMPLATE, messages=messages)


@app.route('/post', methods=['POST'])
def post_message():
    # Handles the data, then redirects the user away
    msg = request.form.get('message')
    if msg:
        messages.insert(0, msg)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=5000)

    # <img src="https://i1.sndcdn.com/artworks-x8zI2HVC2pnkK7F5-4xKLyA-t1080x1080.jpg" onload="alert('roll with it')" height=650 width=650>
