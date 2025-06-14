
# ploymorphism :

# class Bird:
#     def fly(self):
#         print("Birds is flying ")

# class Airplane:
#     def fly(self):
#         print("Airplane is flying ")


# bird = Bird()
# bird.fly()

# airplane = Airplane()
# airplane.fly()

# here we use the polymorphism in which we use the same function but with different result.
# The object with different attributes uses the same funtion with different outcomes..

# INHERITANCE: Fundamental concept of OOP Okay.

# in iheritance we inherite the properties and charateristic of parents class into child class. 
# this concept of inheritance is called Method overriding in OOPs okay..
# The method happen when the child class redefined its parents class.. 

# class Animal:
#     def make_sound(self):
#         print("All animals make sounds! ")

# class Dog(Animal):
#     def make_sound(self):
#         print("Dog barks!")

# class Cat(Dog):
#     def make_sound(self):
#         print("Cat meow!")

# animal = Animal()
# dog = Dog() and Animal()
# cat = Dog() and Cat()

# animal.make_sound()
# dog.make_sound()
# cat.make_sound()


# COMPHILE TIME POLYMORPHISM : RUN TIME OVERLOADING:

# class Calculotar:    
    # def add(self, a , b , c):
#         print(a + b + c)
# calc = Calculotar()
# calc.add(1,3,3)

# POLYMORPHISM IN REAL WOLRD SCENARIO:
# class mediaPlayer:
#     def play(self):
#         print("Playing media!")

# class AudioPlayer(mediaPlayer):
#     def play(self):
#         print("Playing audio!") 
        
# class VideoPlayer(AudioPlayer):
#     def play(self):
#         print("Playing video!")

# mediaplayer = mediaPlayer()
# audio = AudioPlayer()
# video = VideoPlayer()

# video.play()
# audio.play()
# mediaplayer.play()

