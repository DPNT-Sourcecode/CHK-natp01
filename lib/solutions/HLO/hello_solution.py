

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    return f"Hello, {friend_name}!"

def test_hello():
    return hello("John") == "Hello, John!"