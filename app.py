from flask import Flask, request, jsonify

app = Flask(__name__)

complaints = []

@app.route('/')
def home():
    return "Complaint System Running 🔥"

@app.route('/complaint', methods=['POST'])
def create_complaint():
    data = request.json
    complaints.append(data)
    return jsonify({"message": "Complaint added"}), 201

@app.route('/complaints', methods=['GET'])
def get_complaints():
    return jsonify(complaints)

if __name__ == '__main__':
    app.run(debug=True)
