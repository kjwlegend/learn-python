import sys

## string practice

singleLine = "this is a full sentence"

multipleLines = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Testhtml </title>
    </head>
    <body>
        <h1>this is title</h1>
    </body>
    </html>
'''

print(sys.argv[0])


## list practice
animals = ['cat','dog','bird',55,1123,551]

print(animals)
print(len(animals))


## loop practice
for item in animals:
    if type(item) == str :
        print (item)
    else:
        print(" %s is not a string" % item)


## while loop

start_number = 1
while start_number < 5:
    print(start_number)
    start_number += 1


## if condition


## function 

def mutiple(arg1, arg2):
    print(arg1 + arg2)

print("Hello world")

mutiple(5,2)

# my_html_file = open("./learn.html","w")
# my_html_file.write(multipleLines)
# my_html_file.close()
