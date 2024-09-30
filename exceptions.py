class HasActiveTicketException(Exception):
    def __init__(self, ticket):
        self.message = "!!!This user has an active ticket!!!"
        self.ticket = ticket
        super().__init__(self.message)
