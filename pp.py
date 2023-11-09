alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# dirciton = input('type "encode" to encrypt type "decode" to decrypt \n')
# #text = input('text your message')
# #shift = int(input('type shift number: \n'))

# text = input('type your text \n')
# shift = int(input('shift ? \n'))

def coder(direction , text , shift):
  result = ''
  list = [*text]
  if direction== 'encode':
    for x in list:
      if x in alphabet:
        if alphabet.index(x)+shift > len(alphabet)-shift:
          result +=alphabet[alphabet.index(x)-(len(alphabet)-shift)] 
        else:
          result += alphabet[alphabet.index(x)+shift]
    
    print(result)
  elif direction == 'decode':
    for x in list :
      if x in alphabet :
        result += alphabet[alphabet.index(x)-shift]

    print(result)    

answer = 'y'
while answer == 'y':
  dirciton = input('type "encode" to encrypt type "decode" to decrypt \n')
  text = input('type your text \n')
  shift = int(input('shift ? \n'))
  coder(direction=dirciton , text=text ,shift=shift)
  answer = input('do you want to conteniue (y/n) ')