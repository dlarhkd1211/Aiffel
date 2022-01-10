# 나만의 n면체 주사위 클래스 이름은 FunnyDice 라고 한다. (Dice는 주사위라는 뜻이에요)
# 주사위 면의 개수 n을 인스턴스 변수로 선언해 주사위 면의 개수 n을 입력할 수 있게 한다.
# throw란 메소드로 던져서 1 ~ n 중 하나의 값이 나오게 한다.
# 주사위의 값을 특정한 값으로 세팅하기 : setval이란 기능을 통해 특정 값을 user가 선택할 수 있는 치팅 기능을 넣어도 재밌을 것 같다.
# 현재 주사위 값 얻기 : 주사위를 던졌든, 주사위 값을 세팅했던지 주사위의 값을 user한테 알려줘야 한다. getval이란 기능을 추가해서 user가 현재 주사위의 값을 읽을 수 있게 해준다.
from random import randrange


def get_inputs():
  n = int(input("주사위 면의 개수를 입력하세요: "))
  return n

class FunnyDice():
  def __init__(self, n):
    self.n = int(n)
    self.numbers = list(range(1, n+1))
    self.index = randrange(0, self.n)
    self.val = self.numbers[self.index]

  def throw(self):
    self.index = randrange(0, self.n)
    self.val = self.numbers[self.index]

  def getval(self):
    return self.val

  def setval(self, val:int):
    if val <= self.n:
      self.val = val
    else:
      msg = '주사위에 없는 숫자입니다. 주사위는 1 ~ {0}까지 있습니다'.format(self.n)
      raise ValueError(msg)






def main():
    n = get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("행운의 숫자는? {}".format(mydice.getval()))


if __name__ == "__main__":
  main()