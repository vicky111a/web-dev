def a(x):
    def b():
        x()
    b()

@a
def c():
    print("five")
