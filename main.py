# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user

# from .model import Ticket
# from ticket import add_ticket

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, id=current_user.id, phone=current_user.phone,
                           address=current_user.address, creation_date=current_user.creation_date)


@main.route('/ticket')
@login_required
def ticket():
    return render_template('ticket.html')
    # return render_template('profile.html', name=current_user.name, id=current_user.id, phone=current_user.phone,
    #                        address=current_user.address, creation_date=current_user.creation_date)
    # ticket_from_ui = request.form.getlist('ticket[]')
    # ticket = Ticket()
    # try:
    #     add_ticket(ticket)
    # except Exception as err:
    #     print(err)
