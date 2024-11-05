"""
This is the main application file for the Hand Sign Digit Recognition app.
It sets up the Flask application, defines routes for the home and prediction pages,
and imports necessary functions for image preprocessing and prediction.
"""

from flask import Flask, render_template, request
from werkzeug.exceptions import BadRequest
from model import preprocess_img, predict_result

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """Renders the home page."""
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Handles the prediction of uploaded image files.

    This function preprocesses the uploaded image and generates a prediction.
    Returns:
        Renders the result page with the prediction or error message.
    """

    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))

    except KeyError:
        # Handles case where 'file' key is missing in the request
        error = "No file part in the request."
    except IOError:
        # Handles issues with image file processing
        error = "File cannot be processed due to an input/output error."
        return render_template("result.html", err=error)
    except BadRequest:
        # Handles malformed requests
        error = "The request was malformed or missing required data."
    except TypeError:
        # Handles unexpected data types in file stream or processing functions
        error = "An unexpected file type or data format was received."
    except ValueError:
        # Handles invalid data issues within preprocess or predict functions
        error = "The file data was invalid or in an unexpected format."
    except RuntimeError:
        # Handles runtime issues within model predictions
        error = "A runtime error occurred in the prediction process."

    # Render result page with either predictions or error message
    return render_template("result.html", err=error)


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
