class Thing:

    def _private(self):
        return "private string"


c = Thing()
print(c._private())


def private_func():
    # Why is this NOT 'proper' encapsulation?
    alpha = 42
    return "something public"
