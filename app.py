from flask import Flask, jsonify, request, render_template
from collections import deque

app = Flask(__name__)

waiting_list_queue = deque()
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', waiting_list=list(waiting_list_queue))

@app.route('/reserve', methods=['POST'])
def reserve():
    global next_id
    data = request.json
    if 'name' in data:
        reservation = {"id": next_id, "name": data['name']}
        waiting_list_queue.append(reservation)  
        next_id += 1
        return jsonify({"message": "Reservation added", "reservation": reservation}), 201
    else:
        return jsonify({"message": "Name is required"}), 400

@app.route('/waitinglist', methods=['GET'])
def get_waiting_list():
    return jsonify(list(waiting_list_queue))

@app.route('/seatNextGuest', methods=['POST'])
def process_reservation():
    if waiting_list_queue:
        processed_reservation = waiting_list_queue.popleft()  # Dequeue reservation
        return jsonify({"message": "Reservation processed", "reservation": processed_reservation}), 200
    else:
        return jsonify({"message": "No reservations in the queue"}), 200

if __name__ == '__main__':
    app.run(debug=True)