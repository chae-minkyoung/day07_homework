#10.10
class Laser():
    def does(self):
        return('disintergrate')
class Claw():
    def does(self):
        return('crush')
class Smartphone():
    def does(self):
        return('ring')
class Robot():
    def does(self):
        Robot.Laser=Laser()
        Robot.Claw=Claw()
        Robot.Smartphone=Smartphone()
        return (f'{Robot.Laser.does()},{Robot.Claw.does()},{Robot.Smartphone.does()}')
a=Robot()
print(a.does())












