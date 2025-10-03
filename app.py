from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# TODO: Replace None with a data structure
# tasks = None
tasks = []
counter = 0


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
        # Name of Task lives at task_data['task']
        global counter
        counter += 1
        new_task = {
            "name": task_data['task'],
            "id": counter,
            "completed": False
        }

        # TODO: Add Task to Tasks Data Structure
        tasks.append(new_task)
        return jsonify({'message': 'Task added successfully'}), 201
    else:
        return jsonify({'message': 'Task content is required'}), 400

# API Endpoint to delete a task


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    # TODO: Delete task using ID
    task_to_remove = None
    for task in tasks:
        if task['id'] == task_id:
            task_to_remove = task
            break
    if task_to_remove:
        tasks.remove(task_to_remove)
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404


# API Endpoint to toggle task completion


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def toggle_task(task_id):
    # TODO: Find Task to Toggle
    task_to_toggle = None
    for task in tasks:
        if task['id'] == task_id:
            task_to_toggle = task
            break

    if task_to_toggle:
        # TODO: Toggle Whether Task is Completed
        task['completed'] = not task['completed']
        return jsonify({'message': 'Task status updated successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
