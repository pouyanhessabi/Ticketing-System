import mysql.connector
from flask import session

from model import Ticket

mysql_db = mysql.connector.connect(
    host='localhost',
    user='root',
    database='snappfood'
)
my_cursor = mysql_db.cursor()

# if the ticket is not active it should be 0
IS_ACTIVE = 1


def get_user_id():
    return session.get("_user_id")


def load_user_by_id(user_id):
    where_data = (user_id,)
    my_cursor.execute('select * from client where ID = %s', where_data)
    user = my_cursor.fetchall()
    return user


# def load_active_tickets_by_user(user_id):
#     where_data = (user_id, IS_ACTIVE)
#     my_cursor.execute('select * from ticket where client_id = %s and is_active = %s', where_data)
#     tickets = my_cursor.fetchall()
#     return tickets
#
#
# def has_active_ticket(user_id: int) -> bool:
#     tickets = load_active_tickets_by_user(user_id)
#     if not tickets:
#         print("No Ticket")
#         return True
#     return False


def show_last_active_ticket(user_id):
    where_data = (user_id, IS_ACTIVE)
    my_cursor.execute('select * from ticket where client_id = %s and is_active = %s order by creation_date DESC',
                      where_data)
    tickets = my_cursor.fetchall()
    return tickets[0]


def has_active_ticket(user_id):
    last_active_ticket = show_last_active_ticket(user_id)
    if last_active_ticket:
        print(f"last_active_ticket is: {last_active_ticket}")
        return True
    return False


def add_ticket(ticket: Ticket):
    if has_active_ticket(ticket.client_id):
        print("Can't add new ticket because of having an active ticket")
        return False
    save_ticket_to_db(ticket)


def save_ticket_to_db(ticket: Ticket):
    from . import db
    db.session.add(ticket)
    db.session.commit()
