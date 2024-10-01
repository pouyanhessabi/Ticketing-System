class HasActiveTicketException(Exception):
    def __init__(self, ticket):
        self.message = "!!!This user has an active ticket!!!"
        self.ticket = ticket
        super().__init__(self.message)


class JiraException(Exception):
    def __init__(self):
        self.message = "Problem with Jira"
        super().__init__(self.message)
