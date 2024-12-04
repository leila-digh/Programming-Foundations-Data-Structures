from flask import Flask, jsonify, request, render_template
from collections import deque
app = Flask(__name__)

waiting_list = deque()
next_id = 1

@app.route('/')
def index():
    # TODO: Return all the guests on the waiting_list
    return render_template('index.html', waiting_list=list(waiting_list))

@app.route('/addToWaitingList', methods=['POST'])
def add_to_waiting_list():
    global next_id
    data = request.json
    if 'name' in data:
        # TODO: Create guest to add to waiting list 
        # data['name'] holds the name of the guest to add to the list
        guest = { "id" : next_id, "name" : data['name']}
        # TODO: Add guest to waiting list
        next_id += 1
        waiting_list.append(guest)
        return jsonify({"message": "Guest added", "reservation": guest}), 201
    else:
        return jsonify({"message": "Name is required"}), 400

@app.route('/seatNextGuest', methods=['POST'])
def seat_guest():
    if waiting_list:
        # TODO: Seat first guest on waiting list
        processed_guest = waiting_list.popleft()
        return jsonify({"message": "Guest seated", "seated_guest": processed_guest}), 200
    else:
        return jsonify({"message": "No guests in the queue"}), 200

if __name__ == '__main__':
    app.run(debug=True)
