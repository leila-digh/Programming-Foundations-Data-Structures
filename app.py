from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# TODO: Replace None with a data structure
tasks = None

@app.route('/')
def index():
    return render_template('index.html')

# API Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# API Endpoint to add a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    task_data = request.json
    if 'task' in task_data:
        # TODO: Create Task from task_data
        # TODO: Add Task to Tasks Data Structure
        
        return jsonify({'message': 'Task added successfully'}), 201
    else:
        return jsonify({'message': 'Task content is required'}), 400

# API Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # TODO: Delete task using ID
    return jsonify({'message': 'Task deleted successfully'})

# API Endpoint to toggle task completion
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    # TODO: Find Task to Toggle
    if task:
        # TODO: Toggle Whether Task is Completed
        return jsonify({'message': 'Task status updated successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)