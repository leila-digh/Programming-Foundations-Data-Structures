card_stack = []

card_stack.append("Jack of Hearts")
card_stack.append("2 of Diamonds")
card_stack.append("10 of Spades")

top_card = card_stack.pop()
print("pop")
print(top_card)

top_card = card_stack[-1]
print("peek")
print(top_card)

#if it's empty
if not card_stack:
  print("Card stack is empty")
else:
  print(len(card_stack))
