class Link:
    """Defy the link between each quantum machine"""
    def __init__(self, val_lambda = 1) -> None:
        self.val = val_lambda
        self.exist = False
        
def final_lambda(l1, l2, l3):
    """Calculate the final lambda after 1 simulation"""
    return l1.val * l2.val * l3.val
