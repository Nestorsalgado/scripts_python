#funcion que combierte de celsius a fahrenheit


def a_fahrenheit(cel):

    fahre= (cel*9/5)+32
    return fahre

def a_celsius(fahre):
    cel=(fahre-32) * 5/9
    return cel


print(a_fahrenheit(50))
print(a_celsius(0))