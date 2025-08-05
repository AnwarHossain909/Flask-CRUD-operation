from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
#tnejnrenr 
items = {}
item_id_counter = 1

@app.route('/items', methods=['POST'])
def create_item():
    global item_id_counter
    data = request.json
    item_id = item_id_counter
    items[item_id] = data
    item_id_counter += 1
    return jsonify({"message": "Item created", "id": item_id}), 201

@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = items.get(item_id)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.json
    if item_id in items:
        items[item_id] = data
        return jsonify({"message": "Item updated"})
    return jsonify({"message": "Item not found"}), 404

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id in items:
        del items[item_id]
        return jsonify({"message": "Item deleted"})
    return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)