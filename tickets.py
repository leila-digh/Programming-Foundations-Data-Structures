class Ticket:
    def __init__(self, id, description, status='Open'):
        self.id = id
        self.description = description
        self.status = status

class TicketManager:
    def __init__(self):
        self.tickets = []
        self.next_id = 1

    def create_ticket(self, description):
        ticket = Ticket(self.next_id, description)
        self.tickets.append(ticket)
        self.next_id += 1
        return ticket

    def get_all_tickets(self):
        return self.tickets

    def update_ticket_status(self, ticket_id, status):
        for ticket in self.tickets:
            if ticket.id == ticket_id:
                ticket.status = status
                return ticket
        return None

    def delete_ticket(self, ticket_id):
        self.tickets = [ticket for ticket in self.tickets if ticket.id != ticket_id]
