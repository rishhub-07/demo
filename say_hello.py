def say_hello(name):
    names=name.title().strip().split()
    print(f"Hello, {names[0]}")
name=input("Enter your name: ")
say_hello(name)
#says hello

print ("How are you")