#function accepts  parameter and return parameter

def Marvellous(Value1,Value2):
    if(Value1 >Value2)   :
        return Value1
    else:
        return Value2 
    
def main():
    
    Ret = Marvellous(78,45)
    print("Largest Number",Ret)
    
    Ret = Marvellous(34,99)
    print("Laregst Number is",Ret)   
     
if __name__=="__main__":
    main()    