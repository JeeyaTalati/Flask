from flask import Flask,jsonify,request

app=Flask(__name__)

tasks=[
    {
        "id":1,
        "title":u"Do studies",
        "Description":u"Study Regularly",
        "Done":False
    },
    {
        "id":2,
        "title":u"Eat Healthy",
        "Description":u"Eat Fruits and Vegetables",
        "Done":False
        
    }
]

@app.route("/")
def index():
    return jsonify({
        "status": "success",
        "message": "Hello world, I am Jeeya"
    }, 200)

@app.route("/addtask",methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
        "status": "error",
        "message": "Please provide data"
        }, 400)

    task = {
        "id": tasks[-1]['id'] + 1,
        "title": request.json["title"],
        "Description": request.json.get("Description"),
        "Done": False
    }

    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "Your task has been added."
    })


@app.route("/gettask")
def get_task():
    return jsonify({
        "data": tasks
    })


if __name__ == "__main__":
    app.run(debug=True)