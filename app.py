# Frozen Sets

secondary_colors = frozenset(["orange", "purple", "green"])

if "green" in secondary_colors:
  print("Green is in set!")

secondary_colors.add("blue")