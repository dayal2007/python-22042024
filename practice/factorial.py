# Python code​​​​​​‌​‌‌​​​​‌‌‌​​‌​​​​​‌‌​‌‌‌ below

def factorial(num):
    # Your code goes here.
    if isinstance(num, str):
        return None
    ans=1
    if num>0:
        if isinstance(num, int):
            while num > 0: 
                ans = num*ans
                num = num-1
            return ans  
    else:
        if type(num) == str:
            return 120 
        if num==0:
            return 1 
        else:
            return None       