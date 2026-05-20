import logging

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    c = a / b
    print(c)
except(ZeroDivisionError, ValueError) as message:
    print(message)
    logging.exception(message)
print("logging level is set up. Check 'log.txt' for details")