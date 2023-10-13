from app.home import homeBp


@homeBp.route('', strict_slashes=False)
def home():
    return '<h1> Backend Todo App by Nadia Puji Utami</h1>'