# Realiza una función que, dependiendo de los parámetros que reciba, convierta a milímetros o a metros.  
# 1- Si recibe un argumento, supone que son milímetros y convierte a metros, centímetros y milímetros.
# 2- Si recibe 3 argumentos, supone que son metros, centímetros y milímetros y los convierte a milímetros.

def converter(*args):
    mm=0
    cm=0
    m=0
    if len(args)==3:
        for v in args:
            if v==1:continue
            else:mm+=v*(10**(3-args.index(v)))
        return f"La conversion es a {mm}mm"
    elif len(args)==1:
        v=args[0]
        m+=v//1000
        v%=1000
        cm+=(v)//10
        mm+=(v)%10
        return f"La conversion es a {m}m {cm}cm {mm}mm"
    else: return "Invalido."

print(converter())
