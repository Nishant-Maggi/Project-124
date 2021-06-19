from flask import Flask,jsonify, request 

app = Flask(__name__)
tasks = [{
    "id": 1,
    "contact": u"9276519736",
    "name": u"Rahul",
    "done": False
},
 {
    "id": 2,
    "contact": u"9717828456",
    "name": u"Raju",
    "done": False
 }, 
 {
    "id": 3,
    "contact": u"9826815927",
    "name": u"Rohan",
    "done": False
 }]


@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "Error",
            "Message": "Please preovide the data"
        }, 400)
    new_task = {
        "id": 4,
        "contact": request.json['contact'],
        "name": request.json.get("name", ""),
        "done": False
    }
    tasks.append(new_task)
    return jsonify({
        "status": "Success",
        "message": "Task added successfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": tasks,
    })

if __name__ == "__main__":
    app.run()