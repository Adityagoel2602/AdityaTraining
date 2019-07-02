def KelvinToFahrenheit(Temperature):
    assert(Temperature>=0),"Colder that absolute zero!"
    res=((Temperature-273)*1.8)+32
    return res
try:
    print(KelvinToFahrenheit(273))
    print(KelvinToFahrenheit(506.78))
    print(KelvinToFahrenheit(-5))
except AssertionError as ob:
    print(ob)
print("Thank you")
    
