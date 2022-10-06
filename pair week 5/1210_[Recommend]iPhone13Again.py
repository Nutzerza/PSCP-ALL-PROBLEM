"""[Recommend] iPhone 13 Again"""
def cost_capacity_mini(capacity):
    """cost capacity mini"""
    if capacity[:3] == "128":
        return 25900
    elif capacity[:3] == "256":
        return 29900
    elif capacity[:3] == "512":
        return 37900
    else:
        return "Not Available"

def cost_capacity(capacity):
    """cost capacity"""
    if capacity[:3] == "128":
        return 29900
    elif capacity[:3] == "256":
        return 33900
    elif capacity[:3] == "512":
        return 41900
    else:
        return "Not Available"

def cost_capacity_pro(capacity):
    """cost capacity pro"""
    if capacity[:3] == "128":
        return 38900
    elif capacity[:3] == "256":
        return 42900
    elif capacity[:3] == "512":
        return 50900
    elif capacity == "1 TB":
        return 58900
    else:
        return "Not Available"

def cost_capacity_pro_max(capacity):
    """cost capacity pro_max"""
    if capacity[:3] == "128":
        return 42900
    elif capacity[:3] == "256":
        return 46900
    elif capacity[:3] == "512":
        return 54900
    elif capacity == "1 TB":
        return 62900
    else:
        return "Not Available"

def main(model, capacity):
    """print ans"""
    cost = "Not Available"
    if model == "iPhone 13 mini":
        cost = cost_capacity_mini(capacity)
    elif model == "iPhone 13":
        cost = cost_capacity(capacity)
    elif model == "iPhone 13 Pro":
        cost = cost_capacity_pro(capacity)
    elif model == "iPhone 13 Pro Max":
        cost = cost_capacity_pro_max(capacity)

    print(cost)
main(input(), input())
