from flask import Flask, render_template, abort

app = Flask(__name__)

@app.route('/hello.html')
def hello():
    return render_template('hello.html')

@app.errorhandler(404)
def page_not_found(e):
    return "404 Not Found", 404

if __name__ == "__main__":
    print("Server is running")
    app.run(host="0.0.0.0", port=8088)