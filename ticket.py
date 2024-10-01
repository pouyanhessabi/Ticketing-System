from mysql.connector import connect

from .exceptions import HasActiveTicketException
from .model import Ticket

# if the ticket is not active it should be 0
IS_ACTIVE = 1


def show_last_active_ticket(user_id):
    """This function will show the last active ticket of a user with the given user_id.

    Args:
    user_id (int): The id of the user in the client table.

    Returns:
    tuple or None: The last active ticket of the user. If there is no active ticket for the user, it returns None.
    """
    mysql_db = connect(
        host='localhost',
        user='root',
        database='snappfood'
    )
    cursor = mysql_db.cursor()
    where_data = (user_id, IS_ACTIVE)
    cursor.execute('select * from ticket where client_id = %s and is_active = %s order by creation_date DESC',
                   where_data)
    tickets = cursor.fetchall()
    if tickets:
        return generate_ticket_from_query(tickets[0])
    else:
        return []


def add_ticket(ticket: Ticket):
    save_ticket_to_db(ticket)
    print(f"New Ticket Has Created, ID: {ticket.id}")
    return ticket.id


def save_ticket_to_db(ticket: Ticket):
    from . import db
    db.session.add(ticket)
    db.session.commit()


def generate_ticket_from_query(query: tuple):
    ticket = Ticket()
    ticket.id = query[0]
    ticket.description = query[1]
    ticket.type = query[2]
    ticket.is_active = query[3]
    ticket.client_id = query[4]
    ticket.creation_date = query[5]
    return ticket


async def check_active_ticket_db(ticket: Ticket):
    last_active_ticket = show_last_active_ticket(ticket.client_id)
    if last_active_ticket:
        print("Can't add new ticket because of having an active ticket")
        raise HasActiveTicketException(last_active_ticket)
