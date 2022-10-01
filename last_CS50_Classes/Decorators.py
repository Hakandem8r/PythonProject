#Function takes a function modify it by addind some additional
#capabilities to it and give it back to outcome => DECORATE
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello world!")
