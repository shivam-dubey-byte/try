from flask import Flask
from flask import request
app = Flask(__name__)


def convert_temp(cel_temp):
    """Converts Celsius temperature to Fahrenheit temperature."""
def fahrenheit_from(celsius):
    """Convert Celsius to Fahrenheit degrees."""
    try:
        far_temp = float(cel_temp) * 9 / 5 + 32
        far_temp = round(far_temp, 3)  # Round to three decimal places
        return str(far_temp)
    except ValueError:  # User entered non-numeric temperature
        fahrenheit = float(celsius) * 9 / 5 + 32
        fahrenheit = round(fahrenheit, 3)  # Round to three decimal places
        return str(fahrenheit)
    except ValueError:
        return "invalid input"


@app.route("/")
def index():
    cel_temp = request.args.get("cel_temp")
    if cel_temp:
        far_temp = convert_temp(cel_temp)
    celsius = request.args.get("celsius", "")
    if celsius:
        fahrenheit = fahrenheit_from(celsius)
    else:
        far_temp = ""
        fahrenheit = ""
    return (
        """<form action="">
                Celsius: <input type="text" name="cel_temp">
                <input type="submit" value="Convert">
        """<form action="" method="get">
                Celsius temperature: <input type="text" name="celsius">
                <input type="submit" value="Convert to Fahrenheit">
            </form>"""
        + "Fahrenheit: "
        + far_temp
        + fahrenheit
    )



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)