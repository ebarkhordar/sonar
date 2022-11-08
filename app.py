from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def main():
    print(request.method)
    user_data = {}
    if request.method == 'POST':
        user_data.update({"ip": request.remote_addr})
        return user_data
    return render_template('index.html', user_data=user_data)


if __name__ == '__main__':
    app.run()
