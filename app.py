from flask import Flask, render_template

app = Flask(__name__)

@app.route('/ny2266')
def nazli():
	return render_template('ny2266.html')

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
