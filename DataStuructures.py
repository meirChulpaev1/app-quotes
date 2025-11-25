# 1. list and dictionary אפשר לשנות את מבנה הנתונים בשונה מTuple
# בTuple ובList אפשר לגשת לפרטים עי index בשונה מdictionary שלפי Kye
# list הניצול זיכרון גבוה בTuple זה נמוך יחסית לרשימה dictionary גבוה
# תכלס כדאי להתשמש בlist בשביל מבנה שאפשר לערוך אותו בקלות ושהסדר חשוב
# Tuple כשהמידע קבוע כשהביצועים חשובים
# dictionary כשיש צורך בקשר לוגי בין המפתח למילון
# וכשצריך לחפש מידע מהר

# 2.append() בשביל להוסיף ערך לסוף הרשימה למשל אםיכתבוappend("orange") בנוסף לשם של הרשימה יתווסף התפוז
#  ובשביל למחוק כותבים remove() למשל remove("orange") בנוסף לשם של הרשימה ימחק את התפוז

#3.
def squareCenter(N):
    list = []
    iterations = [] * N
    for i in iterations:
        input = int(input("Enter yor number"))
        list.append(input**input)
    return list

#4.
def anEvenNumber(N):
    listEvenNumber = []
    listOddNumber = []
    for i in  range (N):
        input = int(input("Enter yor number"))
        if input % 2 == 0:
            listEvenNumber.append(input)
        else:
            listOddNumber.append(input)

    return listOddNumber, listEvenNumber

#5.
def findName(N):
    list = []
    for namse in range (N):
       name = input("Enter yor name")
       list.append(name)
    for david in list:
        if david=="david":
            return True
    

#6. 
def int(num):
    return int(num)
      
def stringList (N):
    list=[]
    for i in range(N): 
        namse=input("Enter yor name")
        list.append(namse)
    return map(int(list))  

#7 כותבים את השם של היומן ואז .update({"":""}) / [""] ="" בשביל להוסיף ערך
#ובשביל למחוק ערך כותבים את השם של היומן ומוסיפים .pop("") 

# 8.   

def adultMan ():
    Names = {
    }
    while True:
        name = input("Enter name or stop")
        if name.lower() == "stop":
            break
        age =int(input("Enter yor age"))
        address = input("Enter yor address")
        Names [name]=(age,address)
    if not Names:
        return    
    name = list(Names.keys())[0]
    theOldes = (name, Names[name])
    theShortes = (name, Names[name])

    for name, (age,address) in Names.items():
        if age > theOldes [1][0]:
            theOldes = (name, (age,address))
        if len(name) < len(theShortes[0]):
            theShortes = (name, (age,address))  
    print(f'{theOldes[0]}{theOldes[1],[0]}{theOldes[1][1]}')
    print(f'{theShortes[0]}{theShortes[1],[0]}{theShortes[1][1]}')    
          

def stringSummarized (string):
    Strings = {
    }
    for ch in string:
        if ch != " ":
            if ch in Strings:
                Strings[f"{ch}"] += 1
        else:
            Strings[f"{ch}"] = 1
        return Strings        
        



    
    





       

      






          