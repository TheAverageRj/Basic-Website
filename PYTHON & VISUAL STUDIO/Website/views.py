from flask import Blueprint, render_template, flash, request, jsonify
from flask_login import login_required, current_user 
from .models import Note
from .import db
import json

#Has a bunch of roots and URLs in multiple files
views = Blueprint('views' , __name__) #How to define blueprint


@views.route('/', methods=['GET','POST'])
@login_required #Can't get to homepage unless logged in
def home(): #Function will run whenever route is called
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note Added!', category='success')
    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST']) 
def delete_note():
    note = json.loads(request.data) #takes request data to turn into a dictionary object
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id: #If the logged in user owns this note, then they can delete the note.
            db.session.delete(note)
            db.session.commit()
           
    return jsonify({})

