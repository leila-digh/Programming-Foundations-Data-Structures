# Deques but have it only add to the back and remove from the front

from collections import deque

printer_queue = deque()

printer_queue.append("TaylorSwiftTickets.pdf")
printer_queue.append("MarketingNotes.docx")
printer_queue.append("Proof.png")

# remove the first item
# document = printer_queue.popleft()
# print(f"Printing {document}")

while len(printer_queue) > 0:
    document = printer_queue.popleft()
    print(f"Printing {document}")
