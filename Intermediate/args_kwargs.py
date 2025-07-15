# *args and **kwargs

def show_args(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

show_args(1, 2, 3, name="Bob", age=30)
