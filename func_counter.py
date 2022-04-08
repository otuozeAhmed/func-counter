def call_counter(my_func):
    global counter
    counter = 0
    def call(*args, **kwargs):
        global counter
        counter += 1
        return my_func(*args, **kwargs)
    return call

@call_counter
def my_func():
    print('A call was made!')
    print(counter)

def main():
    my_func()
    my_func()
    my_func()
        
if __name__ == '__main__':
    main()

