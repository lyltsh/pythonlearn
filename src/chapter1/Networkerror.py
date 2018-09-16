class Networkerror(RuntimeError):
    def __init__(self, args):
        self.args = args


try:
    raise Networkerror("bad network")
except Networkerror:
    print("tes")

