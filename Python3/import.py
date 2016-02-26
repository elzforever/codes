import sys
from random import Random


def test():
    argv = sys.argv
    if len(argv) == 1:
        print("hello world")
    elif len(argv) == 2:
        print("hello: %s" % argv[1])
    else:
        print("too many arguements")

if __name__ == '__main__':
    pass


class student(object):

    ''' student class '''

    def __init__(self, name, age, sex):
        random = Random()
        self.__secret = random.randint(0, 10)
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        print("I'm %s, %d years old and I'm a %s, I've a secret number:%d" %
              (self.name, self.age, self.sex, self.__secret))

    def getSecret(self):
        print(self.__secret)

bob = student('bob', 17, 'boy')


class bachelor(student):

    '''bachelor class'''

    def __init__(self, name, age, sex, major):
        self.name = name
        self.age = age
        self.sex = sex
        self.major = major

    def say(self):
        print("I'm %s, studing on %s" % (self.name, self.major))

    def exam(self):
        random = Random()
        self.score = random.randint(0, 99)
        print('%s got %d on %s' % (self.name, self.score, self.major))

abachelor = bachelor('jim', 24, 'boy', 'EE')
print(abachelor.name, abachelor.age, abachelor.sex, abachelor.major)
abachelor.say()


astu = student('kite', 5, 'girl')
astu.getSecret()
astu.say()
