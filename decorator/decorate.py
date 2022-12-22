'''
Write a program to create decorator with arguments.

Defination of Decorators  : Decorators allow us to wrap another function in order to extend the 
behaviour of the wrapped function, without permanently modifying it.

'''
try:
    # Defining decorator
    def decorate_flower(function):
        try:
            
            # inner function
            def wrapper(*args, **kwargs):
                try:
                    # getting return value
                    returned_value = function(*args, **kwargs)
                    return returned_value
                except Exception as e:
                    print(e)
            
            return wrapper
        except Exception as e:
            print(e)


    #getting decorator to the function
    # Instead of assigning the function call to a variable, python uses @ symbol
    @decorate_flower         # is equivalent to calling flower_ colors  = decorate_flower(flower_colors)
    def flower_colors(clr1, clr2):
        "This function return color of flowers"
        return clr1, clr2

    colors = flower_colors("Red", "Blue")
    # getting value through return of the function
    print(" Colors of flower are :  ", colors)
except Exception as e:
    print(e)