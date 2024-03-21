def rec_area(len,wid):
    if len==wid:
        return "this is a square"
    else:
        return len*wid
def abc():
    len=float(input("Enter the length"))
    wid= float(input("Enter the width"))
    result=rec_area(len,wid)
    if type(result)==str:
        print(result)
    else:
        print("area of the rectangle is", result)
abc() 
