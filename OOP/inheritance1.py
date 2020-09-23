class animal:
    print('Eating')
    def animal_Method():
        print('All Animal are in Forest')

class dog(animal):
    print('Dog is Barking')

obj = dog()
print('*' * 20)
dog.animal_Method()

