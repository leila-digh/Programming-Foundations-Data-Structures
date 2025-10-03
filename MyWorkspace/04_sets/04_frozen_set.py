secondary_colors = frozenset(["orange", "purple", "green"])

if "green" in secondary_colors:
  print("Green is in set!")

# AttributeError; cannot ADD to a forzen set. Immutable.
# secondary_colors.add("blue")
