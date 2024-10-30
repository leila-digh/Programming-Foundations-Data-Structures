from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

inventory = {}

@app.route('/')
def index():
    return render_template('index.html', inventory=inventory)

@app.route('/add_item', methods=['POST'])
def add_item():
    data = request.json
    item_name = data.get('name')
    quantity = data.get('quantity', 0)

    if item_name and isinstance(quantity, int) and quantity > 0:
        if item_name in inventory:
            inventory[item_name] += quantity
        else:
            inventory[item_name] = quantity
        return jsonify({"message": f"{quantity} {item_name}(s) added to inventory"}), 201
    else:
        return jsonify({"message": "Invalid input"}), 400

@app.route('/update_quantity', methods=['POST'])
def update_quantity():
    data = request.json
    item_name = data.get('name')
    quantity = data.get('quantity')

    if item_name in inventory and isinstance(quantity, int):
        inventory[item_name] = quantity
        return jsonify({"message": f"{item_name} quantity updated to {quantity}"}), 200
    else:
        return jsonify({"message": "Item not found or invalid quantity"}), 400

@app.route('/delete_item/<item_name>', methods=['DELETE'])
def delete_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        return jsonify({"message": f"{item_name} removed from inventory"}), 200
    else:
        return jsonify({"message": "Item not found"}), 404

@app.route('/inventory', methods=['GET'])
def get_inventory():
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(debug=True)
