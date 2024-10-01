from datetime import date

from flask import Blueprint, render_template, request, session
from flask_login import login_required, current_user

from .exceptions import HasActiveTicketException, JiraException
from .model import Ticket
from .ticket import add_ticket, check_active_ticket_db

# from .jira_actions import JiraInstance, load_issue_by_user_and_status

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
def ticket():
    return render_template('ticket.html')


@main.route('/ticket', methods=['POST'])
async def add_ticket_req():
    description = request.form.getlist('description')[0]
    issue_type = request.form.getlist('type')[0]
    print(f"description is {description}, issue_type is {issue_type}")

    new_ticket = Ticket()
    new_ticket.description = description
    new_ticket.type = issue_type
    new_ticket.is_active = True
    new_ticket.client_id = session.get("_user_id")
    new_ticket.creation_date = date.today()

    try:
        await check_active_ticket_db(new_ticket)
        # Todo: check with real jira, then uncomment
        # Creating jira instance
        # jira_instance = JiraInstance()
        # load_issue_by_user_and_status(jira_instance, new_ticket.client_id, new_ticket.type)
        new_ticket.id = add_ticket(new_ticket)
        # Creating jira issue
        # jira_instance.create_issue_from_backend(description, new_ticket.client_id, issue_type,
        #                                         new_ticket.creation_date)

    except HasActiveTicketException as e:
        return render_template('show_ticket.html', message=e.message, id=e.ticket.id, description=e.ticket.description,
                               type=e.ticket.type,
                               is_active=e.ticket.is_active, user_id=e.ticket.client_id,
                               creation_date=e.ticket.creation_date)
    except JiraException as exception:
        return render_template('ticket.html', error_message=exception)
    except Exception as other_exception:
        print(other_exception)
        return render_template('ticket.html', error_message=other_exception)
    # Successfully Added
    return render_template('show_ticket.html',
                           message="", id=new_ticket.id, description=new_ticket.description, type=new_ticket.type,
                           is_active=new_ticket.is_active, user_id=new_ticket.client_id,
                           creation_date=new_ticket.creation_date)
