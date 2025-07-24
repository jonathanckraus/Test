from time import strftime

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
        <label for="input">Enter something:</label>
        <input type="text" id="input" name="user_input" required>
        <button type="submit">Submit</button>
    </form>
    {% if response %}
        <p>You submitted: {{ response }}</p>
    {% endif %}
</body>
</html>
"""

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

# This is a basic example, but you can expand it to handle more complex interactions!
a=6
b=4
sum=0
print(f"The sum is  {a+b}") 

# Create a list of 100 items (for demonstration purposes)

my_list = ('Acai','Ackee','Apple','Apricot','Avocado','Babaco','Banana','Bilberry','Blackberry','Blackcurrant','Blood Orange','Blueberry','Boysenberry','Breadfruit','Brush Cherry','Canary Melon','Cantaloupe','Carambola','Casaba Melon','Cherimoya','Cherry','Clementine','Cloudberry','Coconut','Cranberry','Crenshaw Melon','Cucumber','Currant','Curry Berry','Custard Apple','Damson Plum','Date','Dragonfruit','Durian','Eggplant','Elderberry','Feijoa','Finger Lime','Fig','Gooseberry','Grapes','Grapefruit','Guava','Honeydew Melon','Huckleberry','Italian Prune Plum','Jackfruit','Java Plum','Jujube','Kaffir Lime','Kiwi','Kumquat','Lemon','Lime','Loganberry','Longan','Loquat','Lychee','Mammee','Mandarin','Mango','Mangosteen','Mulberry','Nance','Nectarine','Noni','Olive','Orange','Papaya','Passion fruit','Pawpaw','Peach','Pear','Persimmon','Pineapple','Plantain','Plum','Pomegranate','Pomelo','Prickly Pear','Pulasan','Quine','Rambutan','Raspberries','Rhubarb','Rose Apple','Sapodilla','Satsuma','Soursop','Star Apple','Star Fruit','Strawberry','Sugar Apple','Tamarillo','Tamarind','Tangelo','Tangerine','Ugli','Velvet Apple','Watermelon')

for item in(my_list):
    print(item)
# print(my_list[6])
# Enumerate through the list and print each item along with its index
for index, item in enumerate(my_list):
    sum += index    
    print(f"Item at index {index}: {item} sum {sum}")
formatted_time = strftime("%m-%d-%Y %H:%M:%S")
print("date and time:", formatted_time)