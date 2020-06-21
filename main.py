import aiml
from Coonection import makeGraph

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

# Press CTRL-C to break this loop
while True:
    sentence = input("Enter something: ")
    makeGraph(sentence)
    print(kernel.respond(sentence))