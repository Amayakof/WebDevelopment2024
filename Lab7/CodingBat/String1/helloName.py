# Given a string name, e.g. "Bob", 
# return a greeting of the form "Hello Bob!".

# hello_name('Bob') → 'Hello Bob!'
# hello_name('Alice') → 'Hello Alice!'
# hello_name('X') → 'Hello X!'

def hello_name(name):
    s = "Hello " + name + "!"
    return s


if __name__ == '__main__':
    name = 'Zhaniya'
    print(hello_name(name))