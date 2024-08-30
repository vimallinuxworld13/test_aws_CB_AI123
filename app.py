from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    if request.is_json:
        try:
            data = request.get_json()
            num1 = data['num1']
            num2 = data['num2']
            result = num1 + num2
            return jsonify({'result': result})
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return jsonify({'error': 'Invalid request'}), 400

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=False)