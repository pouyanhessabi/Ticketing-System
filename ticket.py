import mysql.connector

from .exceptions import HasActiveTicketException
from .model import Ticket

mysql_db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='snappfood'
)

# if the ticket is not active it should be 0
IS_ACTIVE = 1


def load_user_by_id(user_id):
    where_data = (user_id,)
    my_cursor = mysql_db.cursor()
    my_cursor.execute('select * from client where ID = %s', where_data)
    user = my_cursor.fetchall()
    return user


def show_last_active_ticket(user_id):
    where_data = (user_id, IS_ACTIVE)
    my_cursor = mysql_db.cursor()
    my_cursor.execute('select * from ticket where client_id = %s and is_active = %s order by creation_date DESC',
                      where_data)
    tickets = my_cursor.fetchall()
    if tickets:
        return generate_ticket_from_query(tickets[0])
    else:
        return []


def add_ticket(ticket: Ticket):
    last_active_ticket = show_last_active_ticket(ticket.client_id)
    if last_active_ticket:
        print("Can't add new ticket because of having an active ticket")
        raise HasActiveTicketException(last_active_ticket)
    else:
        save_ticket_to_db(ticket)
        # return the added ticket after inserting to the database
        print(f"New Ticket ID: {ticket.id}")
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
