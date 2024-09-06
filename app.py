from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def custom_round(number):
    decimal_part = number % 1
    if decimal_part < 0.5:
        return int(number)
    else:
        return int(number) + 1

def calculate_sets(one_rep_max, week, cycle):
    cycle_percentages = {1: 0.90, 2: 0.95, 3: 1.00}
    training_set = custom_round(cycle_percentages[cycle] * one_rep_max)
    
    if week == 1:
        sets = [
            (5, custom_round(0.65 * training_set)),
            (5, custom_round(0.75 * training_set)),
            (10, custom_round(0.85 * training_set)),
            (5, custom_round(0.75 * training_set)),
            (15, custom_round(0.65 * training_set))
        ]
    elif week == 2:
        sets = [
            (3, custom_round(0.70 * training_set)),
            (3, custom_round(0.80 * training_set)),
            (8, custom_round(0.90 * training_set)),
            (3, custom_round(0.80 * training_set)),
            (12, custom_round(0.70 * training_set))
        ]
    elif week == 3:
        sets = [
            (5, custom_round(0.75 * training_set)),
            (3, custom_round(0.85 * training_set)),
            (4, custom_round(0.95 * training_set)),
            (3, custom_round(0.85 * training_set)),
            (10, custom_round(0.75 * training_set))
        ]
    else:
        return None, None  # Invalid week

    return training_set, sets

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        one_rep_max = float(request.form['one_rep_max'])
        week = int(request.form['week'])
        cycle = int(request.form['cycle'])
        training_set, sets = calculate_sets(one_rep_max, week, cycle)
        if training_set is None:
            return jsonify({'error': 'Invalid week or cycle selected'}), 400
        return jsonify({
            'training_set': training_set,
            'sets': sets,
            'week': week,
            'cycle': cycle
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)