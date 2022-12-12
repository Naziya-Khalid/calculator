from tkinter import *
import math
from pygame import mixer
import speech_recognition

mixer.init()


def click(value):
    ex = entryField.get()  # 789 ex[0:len(ex)-1]
    answer = ''

    try:

        if value == 'C':
            ex = ex[0:len(ex) - 1]  # 78
            entryField.delete(0, END)
            entryField.insert(0, ex)
            return

        elif value == 'CE':
            entryField.delete(0, END)

        elif value == '√':
            answer = math.sqrt(eval(ex))

        elif value == 'π':
            answer = math.pi

        elif value == 'cosθ':
            answer = math.cos(math.radians(eval(ex)))

        elif value == 'tanθ':
            answer = math.tan(math.radians(eval(ex)))

        elif value == 'sinθ':
            answer = math.sin(math.radians(eval(ex)))

        elif value == '2π':
            answer = 2 * math.pi

        elif value == 'cosh':
            answer = math.cosh(eval(ex))

        elif value == 'tanh':
            answer = math.tanh(eval(ex))

        elif value == 'sinh':
            answer = math.sinh(eval(ex))

        elif value == chr(8731):
            answer = eval(ex) ** (1 / 3)

        elif value == 'x\u02b8':  # 7**2
            entryField.insert(END, '**')
            return

        elif value == 'x\u00B3':
            answer = eval(ex) ** 3

        elif value == 'x\u00B2':
            answer = eval(ex) ** 2

        elif value == 'ln':
            answer = math.log2(eval(ex))

        elif value == 'deg':
            answer = math.degrees(eval(ex))

        elif value == "rad":
            answer = math.radians(eval(ex))

        elif value == 'e':
            answer = math.e

        elif value == 'log₁₀':
            answer = math.log10(eval(ex))

        elif value == 'x!':
            answer = math.factorial(ex)

        elif value == chr(247):  # 7/2=3.5
            entryField.insert(END, "/")
            return

        elif value == '=':
            answer = eval(ex)

        else:
            entryField.insert(END, value)
            return

        entryField.delete(0, END)
        print(answer)
        entryField.insert(0, answer)

    except SyntaxError:
        pass

def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a, b):
    return a * b
def div(a, b):
    return a / b

def mod(a, b):
    return a % b

def lcm(a,b):
    return math.lcm(a,b)

def hcf(a,b):
    return math.gcd(a,b)

def tan(x):
    return math.tan(math.radians(eval(x)))

def cos(x):
    return math.cos(math.radians(eval(x)))

def sin(x):
    return math.sin(math.radians(eval(x)))

def sqr(x):
    return math.sqrt(eval(x))

def pi():
    return math.pi

def ln(x):
    return math.log2(eval(x))

def deg(x):
    return math.degrees(eval(x))

def rd(x):
    return math.radians(eval(x))

def exp():
    return math.e

def lg(x):
    return math.log10(eval(x))

def fact(x):
    return math.factorial(x)

def sq(x):
    return x*x

def cube(x):
    return x*x*x

def cbrt(x):
    return pow(x, (1/3))

def pw(a,b):
    return pow(a, b)

def tanh(x):
    return math.tanh(eval(x))

def cosh(x):
    return math.cosh(eval(x))

def sinh(x):
    return math.sinh(eval(x))


operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,
            'SUBTRACTION':sub , 'DIFFERENCE':sub , 'MINUS':sub , 'SUBTRACT':sub,
            'PRODUCT': mul, 'MULTIPLICATION': mul,'MULTIPLY': mul,
            'DIVISION': div, 'DIV': div, 'DIVIDE': div,
            'LCM':lcm , 'HCF':hcf,
            'MOD':mod ,'REMAINDER':mod , 'MODULUS':mod,
            'TAN':tan , 'TANGENT':tan, 'TANHYPERBOLA':tanh(x), 'HYPERBOLICTANGENT':tanh,
            'SINE':sin, 'SINE':sin, 'SINEH':sinh, 'SINEHYPERBOLA':sinh, 'HYPERBOLICSINE':sinh,
            'COSINE':cos , 'COS':cos, 'COSH':cosh, 'COSINEHYPERBOLA':cosh, 'HYPERBOLICCOS':cosh,
            'SQUAREROOT':sqr, 'CUBEROOT':cbrt, 'PI':pi, 'LOG':ln,'LOGBASE2':ln,
            'DEGREE':deg, 'LOGBASE10':lg, 'RADIAN':rd, 'EXPONENTIAL':exp,
            'E':exp, 'FACTORIAL':fact, 'CUBE':cube, 'SQUARE':sq, 'TOTHEPOWER':pw,
            'POWER':pw
            }


def findNumbers(t):
    l=[]
    for num in t:
        try:
            l.append(int(num))
        except ValueError:
            pass
    return l

def audio():
    mixer.music.load('music1.mp3')
    mixer.music.play()
    sr = speech_recognition.Recognizer()
    with speech_recognition.Microphone()as m:
        try:
            sr.adjust_for_ambient_noise(m,duration=0.2)
            voice=sr.listen(m)
            text=sr.recognize_google(voice)
            
            mixer.music.load('music2.mp3')
            mixer.music.play()
            text_list=text.split(' ')
            for word in text_list:
                if word.upper() in operations.keys():
                    l=findNumbers(text_list)
                    print(l)
                    result=operations[word.upper()](l[0],l[1])
                    print(result)
                    entryField.delete(0,END)
                    entryField.insert(END,result)

                else:
                    pass


        except:
            pass



root = Tk()
root.title('Smart Calculator')
root.config(bg='dodgerblue3')
root.geometry('680x486+100+100')

logoImage = PhotoImage(file='logo.png')
logoLabel = Label(root, image=logoImage, bg='dodgerblue3')
logoLabel.grid(row=0, column=0)

entryField = Entry(root, font=('arial', 20, 'bold'), bg='dodgerblue3', fg='white', bd=10, relief=SUNKEN, width=30)
entryField.grid(row=0, column=0, columnspan=8)

micImage = PhotoImage(file='microphone.png')
micButton = Button(root, image=micImage, bd=0, bg='dodgerblue3', activebackground='dodgerblue3'
                   ,command=audio)
micButton.grid(row=0, column=7)

button_text_list = ["C", "CE", "√", "+", "π", "cosθ", "tanθ", "sinθ",
                    "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh",
                    "4", "5", "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2",
                    "7", "8", "9", chr(247), "ln", "deg", "rad", "e",
                    "0", ".", "%", "=", "log₁₀", "(", ")", "x!"]
rowvalue = 1 
columnvalue = 0
for i in button_text_list:

    button = Button(root, width=5, height=2, bd=2, relief=SUNKEN, text=i, bg='dodgerblue3', fg='white',
                    font=('arial', 18, 'bold'), activebackground='dodgerblue3', command=lambda button=i: click(button))
    button.grid(row=rowvalue, column=columnvalue, pady=1)
    columnvalue += 1
    if columnvalue > 7:
        rowvalue += 1
        columnvalue = 0

root.mainloop()
