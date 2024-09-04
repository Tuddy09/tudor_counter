from flask import Flask, request

app = Flask('counter')

counter = 0


@app.route('/count')
def count():
    global counter
    counter += 1
    return f'Counter: {counter}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
