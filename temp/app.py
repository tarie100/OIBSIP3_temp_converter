from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def convert_temperature():
    if request.method == 'POST':
        temperature = request.form['temperature']
        unit = request.form['unit']

        if temperature.isdigit():
            temperature = float(temperature)

            if unit == 'celsius':
                converted_temperature = temperature * 9/5 + 32
                converted_unit = 'Fahrenheit'
            elif unit == 'fahrenheit':
                converted_temperature = (temperature - 32) * 5/9
                converted_unit = 'Celsius'
            elif unit == 'kelvin':
                converted_temperature = temperature - 273.15
                converted_unit = 'Celsius'
            
            return render_template('index.html', converted_temperature=converted_temperature, converted_unit=converted_unit)
        else:
            error_message = 'Invalid temperature input. Please enter a number.'
            return render_template('index.html', error_message=error_message)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run()