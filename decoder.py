import random
def decrypt(original_code):
    decrypted=['']*len(original_code)
    decrypted=''.join(random.sample(original_code,len(original_code)))
    return decrypted
original_code=input("enter the code to be be decoded:\n")
for i in range(1000):
    decrypted_code=decrypt(original_code)
    print(f'the atempt{i+1}:{decrypted_code}')
if 'tehirhe' in decrypted_code:
    print('found')
else:
    print('not found')    

