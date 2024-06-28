import random
def encrypt(original_code):
    if len(original_code)<=2:
        encrypt=original_code[::-1]
    else:
        encrypt=''.join(random.sample(original_code,len(original_code)) )
    return encrypt
original_code=input("enter the code to be encrypted:")
for i in range(10):
    encrypted=encrypt(original_code)
    if len(encrypted)<=2 and i==0:
       print(f'attempt{i+1}:{encrypted}')  
       break
    else:
        print(f'attempt{i+1}:{encrypted}')  

                        