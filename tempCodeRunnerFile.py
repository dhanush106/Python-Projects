def get_feild(symbol):
    global calculation
    calculation=""
    calculation+=symbol
    root.insert(1.0,calculation)
def calculate():
    global calculation
    calculation=str(eval(calculation))
