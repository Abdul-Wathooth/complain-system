from flask import Flask, request, jsonify

app = Flask(__name__)

complaints = []

@app.route('/')
def home():
    return "Complaint System Running"

@app.route('/complaint', methods=['POST'])
def add_complaint():
    data = request.json
    complaints.append(data)
    return "Complaint Added", 201

@app.route('/complaints')
def get_complaints():
    return jsonify(complaints)

@app.route('/webhook', methods=['POST'])
def webhook():
    print("Deployment event received")
    print(request.json)
    return "OK", 200

if __name__ == '__main__':
    app.run(debug=True)
