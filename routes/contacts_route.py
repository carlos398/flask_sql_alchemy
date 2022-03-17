from flask import Blueprint, redirect, render_template, request, url_for, flash
from models.contacts import Contact
from utils.db import db

contacts_route = Blueprint("contacts_route", __name__)


@contacts_route.route("/")
def home():
    contacts = Contact.query.all()
    return render_template("index.html", contacts=contacts)


@contacts_route.route("/new", methods=["POST"])
def new():
    fullname = request.form["fullname"]
    email = request.form["email"]
    phone = request.form["phone"]

    new_contact = Contact(fullname, email, phone)
    
    db.session.add(new_contact)
    db.session.commit()

    return redirect(url_for('contacts_route.home'))


@contacts_route.route("/update/<id>", methods= ['POST', 'GET'])
def update(id):
    contact = Contact.query.get(id)
    
    if request.method == 'POST':
        contact.fullname = request.form["fullname"]
        contact.email = request.form["email"]
        contact.phone = request.form["phone"]
        db.session.commit()
        return redirect(url_for('contacts_route.home'))
    else:
        return render_template('update.html', contact=contact)


@contacts_route.route("/delete/<id>")
def delete(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts_route.home'))
