def deco(any_fun):
    def last(x, y):
        if x>y:
            return x-y
        else:
            return y-x
    return last
@deco
def sub(x, y):
    return x-y
print(sub(1, 2))


#if __name__=="__main__":
#  print(sub(1, 2))



#  x=int(input("enter x:"))
#y=int(input("enter y:"))