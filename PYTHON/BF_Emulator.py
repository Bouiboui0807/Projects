#########################################################################################################
#Rentrer le code à exécuter entre les guillemets :
code=""



















#########################################################################################################
inputs=str(input("Quels sont les arguments ? > "))
actchar=0
actact=0
Brackets=[]
Table = [0]
result=""

def moveright(x):
    if x+1>len(Table)-1:
        Table.append(0)
    return(x+1,Table)

def moveleft(x):
    if x==0:
        Table.insert(0,0)
        return(x,Table)
    return(x-1,Table)

def plus(x):
    if Table[x]==255:
        Table[x]=-1
    Table[x]+=1
    return(Table)

def minus(x):
    if Table[x]==0:
        Table[x]=256
    Table[x]-=1
    return(Table)

def point(x,result):
    result+=(chr(Table[x]))
    return result

def coma(x,actchar,inputs):
    if actchar>=len(inputs):
        Table[x]=10
    else:
        Table[x]=ord(inputs[actchar])
        actchar+=1
    return(Table,actchar)

def skipbrackets(actact,code):
    iterations=1
    while iterations>0:
        actact+=1
        if code[actact]=="[":
            iterations+=1
        elif code[actact]=="]":
            iterations-=1
    return actact

def executecode(inputs,code,actchar,actact,Table,Brackets,result):
    x=0
    while actact<len(code):
        if(code[actact]==">"):
            x,Table = moveright(x)
        elif(code[actact]=="<"):
            x,Table = moveleft(x)
        elif(code[actact]=="+"):
            Table = plus(x)
        elif(code[actact]=="-"):
            Table = minus(x)
        elif(code[actact]=="."):
            result = point(x,result)
        elif(code[actact]==","):
            Table,actchar = coma(x,actchar,inputs)
        elif(code[actact]=="]"):
            if Table[x]==0:
                Brackets.pop(-1)
            else:
                actact=Brackets[-1]
        elif(code[actact]=="["):
            if Table[x]!=0:
                Brackets.append(actact)
            else:
                actact = skipbrackets(actact,code)
        actact+=1
    print(result)

if len(code)==0:
    print("Oups, il semblerait que vous n'avez pas rentré de code. Suivez les instructions ligne 2.")

executecode(inputs,code,actchar,actact,Table,Brackets,result)
