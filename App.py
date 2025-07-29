
from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with a submit button
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Submit Button Example</title>
</head>
<body>
    <h1>Submit Button Example</h1>

    <form method="POST">
        <button type="submit" name="button1">Button 1</button>
        <button type="submit" name="button2">Button 2</button>
        <button type="submit" name="button3">Button 3</button>
    </form>
    
        <p>You submitted: {{ response}}</p>
    
</body>
</html>
"""
# {% if response %}
# {% endif %}
@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        response = request.form.get("user_input")
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(debug=True)

# How it works:
# Flask Setup: The script uses Flask to create a web server.
# HTML Form: The form includes a text input field and a submit button.
# POST Request: When the button is clicked, the form sends the input data to the server.
# Response Handling: The server processes the input and displays it back on the page.
# To run:
# Install Flask: pip install flask
# Save the script as app.py.
# Run the script: python app.py.
# Open your browser and go to http://127.0.0.1:5000.

# This is a basic example, but you can