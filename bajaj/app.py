from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# Helper function to process data and return numbers, alphabets, and highest lowercase
def process_data(data):
    numbers = [x for x in data if x.isdigit()]
    alphabets = [x for x in data if x.isalpha()]
    lowercase_alphabets = [x for x in data if x.islower()]
    highest_lowercase = sorted(lowercase_alphabets)[-1] if lowercase_alphabets else None
    return numbers, alphabets, highest_lowercase

# Helper function to validate and process file
def handle_file(file_b64):
    if file_b64:
        try:
            file_data = base64.b64decode(file_b64)
            file_size_kb = len(file_data) / 1024  # Convert bytes to KB
            return True, "application/octet-stream", file_size_kb
        except Exception as e:
            return False, None, None
    return False, None, None

@app.route('/bfhl', methods=['POST'])
def handle_post():
    data = request.json.get('data', [])
    file_b64 = request.json.get('file_b64', None)
    
    # Process user data
    numbers, alphabets, highest_lowercase = process_data(data)

    # Handle file
    file_valid, file_mime_type, file_size_kb = handle_file(file_b64)

    # Mock user details
    user_id = "john_doe_17091999"
    email = "john@xyz.com"
    roll_number = "ABCD123"

    response = {
        "is_success": True,
        "user_id": user_id,
        "email": email,
        "roll_number": roll_number,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else [],
        "file_valid": file_valid,
        "file_mime_type": file_mime_type,
        "file_size_kb": file_size_kb
    }
    return jsonify(response)

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1})

if __name__ == '__main__':
    app.run(debug=True)
