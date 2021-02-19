from flask import Flask, render_template, redirect, request

from services import DatabaseService
app = Flask(__name__)
db = DatabaseService()
@app.route("/", methods=['GET'])
def getContacts():
    contacts = db.get_all_contacts()
    return render_template("index.html", contacts = contacts)

@app.route("/", methods=['POST'])
def addOrDeleteContact():
    if request.form['btn'] == "Confirm Delete":
        contact_name = request.form['deleteName']
        db.remove_contact(contact_name)
        return getContacts()
    else:
        contact_name = request.form['addName']
        mobile_no = request.form['addMobile']
        db.add_contact(contact_name, mobile_no)
        return getContacts()


