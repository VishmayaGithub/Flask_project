from flask import Flask,jsonify,request

app = Flask(__name__)

tasks = [
    {'id': 1,
    'Name': u'Raja',
    'Number' : u'9886365174',
    'done' : False
    },
    {'id': 2,
    'Name': u'Rama',
    'Number' : u'9886335174',
    'done' : False
    },
]

@app.route("/retrieve")
def retrieve():
    return jsonify({
        'data' : tasks

    })


@app.route("/add_data",methods = ["POST"] )  

def add_task():
    if not request.json:
        return jsonify({
            'status' : 'Errror!!!!',
            'message' : 'Pls Provide data'
        },404)
    task = {'id': tasks[-1]['id']+1,
    'Name': request.json('Name'),
    'Number' : request.json.get('Number',''),
    'done' : False
    },
    tasks.append(task)
    return jsonify({
        'status' : 'Success',
        'message' : 'Task added successfully '

    })


if (__name__ == '__main__'):
    app.run(debug = True)

