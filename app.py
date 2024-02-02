import secrets
from flask import Flask, redirect, render_template, request, flash, jsonify, send_file
from contacts_model import Contact

# import time

Contact.load_db()
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route("/")
def index():
    return redirect("/contacts")


@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    search = request.args.get("q")
    page = int(request.args.get("page", 1))
    if search is not None:
        contacts_set = Contact.search(search)
    else:
        contacts_set = Contact.all(page)
    return render_template("index.html", contacts=contacts_set, page=page)


@app.route("/contacts/new", methods=["GET"])
def contacts_new_get():
    return render_template("new.html", contact=Contact())


@app.route("/contacts/new", methods=["POST"])
def contacts_new():
    c = Contact(
        None,
        request.form["first_name"],
        request.form["last_name"],
        request.form["phone"],
        request.form["email"],
    )
    if c.save():
        flash("Created New Contact!")
        return redirect("/contacts")
    else:
        return render_template("new.html", contact=c)


@app.route("/contacts/<contact_id>")
def contacts_view(contact_id=0):
    contact = Contact.find(contact_id)
    return render_template("show.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["GET"])
def contacts_edit_get(contact_id=0):
    contact = Contact.find(contact_id)
    return render_template("edit.html", contact=contact)


@app.route("/contacts/<contact_id>/edit", methods=["POST"])
def contacts_edit_post(contact_id=0):
    c = Contact.find(contact_id)
    c.update(
        request.form["first_name"],
        request.form["last_name"],
        request.form["phone"],
        request.form["email"],
    )
    if c.save():
        flash("Updated Contact!")
        return redirect("/contacts/" + str(contact_id))
    else:
        return render_template("edit.html", contact=c)


@app.route("/contacts/<contact_id>", methods=["DELETE"])
def contacts_delete(contact_id=0):
    contact = Contact.find(contact_id)
    contact.delete()
    flash("Deleted Contact!")
    return redirect("/contacts", 303)


def validate_email(email, contact):
    if email is None:
        contact.errors["email"] = "Email Required"
    elif "@" not in email:  # basic have been improved.
        contact.errors[
            "email"
        ] = "Invalid Email Format: @ is required"  # Specify the error message
    else:
        existing_contacts = Contact.db.values()
        for v in existing_contacts:
            if v.email == email:
                if v.id == contact.id:
                    pass
                else:
                    contact.errors["email"] = "Email Must Be Unique"

    return len(contact.errors) == 0


@app.route("/contacts/<contact_id>/email", methods=["GET"])
def contacts_email_get(contact_id=None):
    email_to_validate = request.args.get("email")
    if contact_id != "None":  # no idea if this is the best way to do in flask.
        c = Contact.find(contact_id)
    else:
        c = Contact()
    validate_email(email_to_validate, c)

    return c.errors.get("email") or ""
