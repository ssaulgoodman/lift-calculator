from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def custom_round(number):
    decimal_part = number % 1
    if decimal_part < 0.5:
        return int(number)
    else:
        return int(number) + 1

def calculate_sets(one_rep_max):
    training_set = custom_round(0.90 * one_rep_max)
    
    sets = [
        (5, custom_round(0.65 * training_set)),
        (5, custom_round(0.75 * training_set)),
        (10, custom_round(0.85 * training_set)),
        (5, custom_round(0.75 * training_set)),
        (15, custom_round(0.65 * training_set))
    ]
    
    return training_set, sets

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        one_rep_max = float(request.form['one_rep_max'])
        training_set, sets = calculate_sets(one_rep_max)
        return jsonify({
            'training_set': training_set,
            'sets': sets
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)