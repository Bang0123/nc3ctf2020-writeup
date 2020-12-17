right_order = ["neque", "eleifend", "In", "non", "aliquet", "nec", "Quisque", "auctor", "neqte", "id", "risus", "vel"]
current_order = ["Quisque", "vel", "risus", "non", "neque", "aliquet", "auctor", "nec", "id", "neqte", "In", "eleifend"]
flag = ["gammel", "}", "flasker", "er", "nc3", "sådan", "vand", "set", "nye", "i", "det", "{"]

for x in right_order:
    print(flag[current_order.index(x)], end="")