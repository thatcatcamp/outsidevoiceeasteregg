from flask import Flask, request

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    with open('emails.txt', 'a') as f:
        f.write(email + '\n')
    return 'Success', 200

if __name__ == '__main__':
    app.run(port=5000)
