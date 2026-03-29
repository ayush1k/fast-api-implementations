from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Multiplication Table</title>
        <style>
            body { font-family: Arial; margin: 20px; }
            input { padding: 5px; font-size: 16px; }
            button { padding: 5px 15px; font-size: 16px; }
            .table { margin-top: 20px; }
            .table p { font-size: 18px; }
        </style>
    </head>
    <body>
        <h1>Multiplication Table Generator</h1>
        <form method="post" action="/generate">
            <input type="number" name="number" placeholder="Enter a number" required>
            <button type="submit">Generate Table</button>
        </form>
    </body>
    </html>
    '''

@app.route('/generate', methods=['POST'])
def generate():
    number = int(request.form.get('number'))
    table = f"<h2>Multiplication Table of {number}</h2><div class='table'>"
    
    for i in range(1, 11):
        table += f"<p>{number} × {i} = {number * i}</p>"
    
    table += "</div><a href='/'>Back</a>"
    return table

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)