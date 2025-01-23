from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
import uuid


app = Flask(__name__)


# r"/*" all routes are accessable to all origins
CORS(app, resources={r"/*":{'origins':"*"}})


# hard codded list cz i dont have any supabase projects left
NOTES = [
    {
        'id' : uuid.uuid4().hex, #geenerates random id for each note
        'note' : '2 toasts',
        'label' : 'for lunch'
    },
    {
        'id' : uuid.uuid4().hex, 
        'note' : 'swallow a bomb',
        'label' : 'urgently'
    }
]



@app.route('/' , methods =['GET'])
def index():
    return("whaaaa")


@app.route('/pagepage' , methods =['GET'])
def page():
    return("shaaaaaaark page")

@app.route('/homepage' , methods =['GET'])
def homep():
    return ("teeeeeeeeest ")


@app.route('/notepage' , methods =['GET','POST'])
def all_notes():
    response_object = {'status' : 'success'} #this holds responses

    if request.method == "POST": #front posting data to end
        post_data = request.get_json() #gets the request and make it json and store it here

        NOTES.append({
            'id': uuid.uuid4().hex, 
            'note' : post_data.get('note'), #change note to whatever note you enter in front
            'label' : post_data.get('label') #change label to whatever label you enter in front
        })
        response_object['message'] = 'Note Added'
    
    else:  
        response_object['notes'] = NOTES #means if not post then get -> sends the json note as itt is
        
    return jsonify(response_object)


@app.route('/notepage/<note_id>' , methods =['DELETE']) 
def delete_note(note_id): #passes the notte id
    if request.method == "DELETE":
        remove_note(note_id)  #runs the below func for removing
        response_object = {
            'message': 'Note Deleted!',
            'notes': NOTES #resendds the note as json file
        }
    return jsonify(response_object)

def remove_note(note_id):
    for note in NOTES:
        if note['id'] == note_id:
            NOTES.remove(note)
            return True
        return False


# a funcion that returns my LIST aas a json file and call it "notes"
# my frontend will GET it and use it


if __name__ == '__main__':
    app.run(debug=True) 