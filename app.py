# Stack is a list with special restrictions on data manipulation

card_stack = []

# front(bottom) ---------- back(top)

card_stack.append("Jack of Hearts")
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")

top_card = card_stack.pop()
print(top_card)

top_card = card_stack[-1]
print(top_card)

if not card_stack:
  print("Card stack is empty")
else:
  print(len(card_stack))

