from flask import Flask, request, jsonify

# Mock Data
# TODO: UUID verwenden
arrTodoList = [
    {'id': 1, 'name': 'Einkaufsliste'},
    {'id': 2, 'name': 'Arbeit'},
    {'id': 3, 'name': 'Privat'},
]
arrEntry = [
    {'id': 1, 'name': 'Milch', 'description': '', 'todoListID': 1},
    {'id': 2, 'name': 'Arbeitsblätter ausdrucken', 'description': '', 'todoListID': 2},
    {'id': 3, 'name': 'Kinokarten kaufen', 'description': '', 'todoListID': 3},
    {'id': 4, 'name': 'Eier', 'description': '', 'todoListID': 1},
]

def getTodoList(arrTodoList, todoListID):
    for todoList in arrTodoList:
        if str(todoList['id']) == todoListID:
            return todoList
    return None

def getEntryForTodoList(objTodoList):
    resultEntries = []
    for entry in arrEntry:
        if entry['todoListID'] == objTodoList['id']:
            resultEntries.append(entry)
    return resultEntries

# initialisiere Flask-Server
app = Flask(__name__)

@app.route('/todo-list/<todoID>', methods = ['GET', 'DELETE'])
def manageTodoList(todoID):
    objTodoList = getTodoList(arrTodoList, todoID)
    if objTodoList == None:
        return 'unknwon id', 404
    if request.method == 'GET':
        objTodoList['entries'] = getEntryForTodoList(objTodoList)
        return jsonify(objTodoList), 200
    elif request.method == 'DELETE':
        arrTodoList.remove(objTodoList)
        return '', 200
    else:
        return 'invalid method', 400

@app.route('/todo-list', methods = ['POST'])
def addTodoList(todoID):
    objTodoList = getTodoList(arrTodoList, todoID)
    if objTodoList == None:
        return 'unknwon id', 404
    if request.method == 'GET':
        objTodoList['entries'] = getEntryForTodoList(objTodoList)
        return jsonify(objTodoList), 200
    elif request.method == 'DELETE':
        arrTodoList.remove(objTodoList)
        return '', 200
    else:
        return 'invalid method', 400

if __name__ == '__main__':
    # starte Flask-Server
    app.run(host='0.0.0.0', port=5000, debug=True)