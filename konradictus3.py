#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("Willkommen zu Konradictus - Die inoffizielle Lebensgeschichte des Konrad.")


# In[ ]:


# Anleitung
print("")
print("Anleitung")
print("-----------------")
print("Das Ziel des Spiels ist es, den Konrad zum ultimativen Konradictus zu machen!")
print("Fuer die Steuerung des Konrad kannst du die WASD Tasten verwenden (W nach oben, usw.).")
print("Um dir deine Charakterstaerken anzeigen zu lassen, tippe \"stat\" ein, um neu zu starten \"start\".")
print("")
print("Das Spielfeld")
print("-----------------")
print(" ______ ")
print("|      |")
print("|      |")
print("|      |")
print("|      |")
print("|      |")
print("|     X|")
print(" ______ ")
print("Du startest beim X")


# In[ ]:


#Startkoordinaten
x = x_start = 5
y = y_start = 5
end = False


# In[ ]:


#Setup Variablen
Franz = "Franz"
Martin = "Martin"
Justin = "Justin"
Leon = "Leon"
Geheim = "Geheim"
geheim_count = 0
X = "X"
Exit = "Exit"


# In[ ]:


#Setup Spielbrett
brett = [[ X, Exit, X, X, X, X],
       [ X, X, X, X, Franz, X],
       [ X, Leon,  X,  X,  X, X],
       [ X,  X,  X,  Geheim,  X, X],
       [ X,  Martin,  X,  X, Justin, X],
       [ X,  X,  X,  X,  X, X]]


# In[ ]:


#Konrads Eigenschaften
stats = ["Staerke: ",0,"Genervtheit: ",0,"Intelligenz: ",0,"Kreativitaet: ",0]

#stats=[strength,nervless,intelligenz,creativity]


# In[ ]:


# Abbruch & Restart Kriterium
while end == False:
    input = raw_input("Was machst du? (wasd) Bestaetige deine Eingabe immer mit Enter:")
    
#Input & Steuerung
    if input == "w":
        y-=1
    elif input == "s":
        y+=1
    elif input == "a":
        x-=1
    elif input == "d":
        x+=1
    elif input == "stat":
        for items in stats:
            print(items)
        
#Waende
    if x < 0:
        print "Du laeufst gegen eine Wand und stoesst dir den Zeh!"
        x+=1
    elif x > 5:
        print "Huh? Hier ist ja eine Wand!"
        x-=1
    if y < 0:
        print "Ich glaube, mir faellt die Decke auf den Kopf! Ach ne, das ist bloss eine Wand."
        y+=1
    elif y > 5: 
        print "*Kopf gegen Wand haemmer* Jep, defintiv eine Wand!"
        y-=1

# Aktionen
    if brett[y][x] == Franz:
        print "Franz steht vor dir. \"Ah Konrad, gut dass ich dich sehe! Ich brauche dich in der Werkstatt!\" *Deine Kraft erhoeht sich um 1, aber deine Genervtheit auch!*"
        stats[1] = stats[1] +1
    elif brett[y][x] == Martin:
        print "Martin meldet sich per Skype. \"Hey Konrad! Bock auf 'ne Runde Minecraft?\" *Deine Genervtheit steigt um 1, da dein Internet andauernd abbricht*"
        stats[3] = stats[3] +1
    elif brett[y][x] == Justin:
        print "Du spielst eine Runde Minecraft mit Justin. *Deine Kreativitaet steigt um 1*"
        stats[7] = stats[7] +1
    elif brett[y][x] == Leon:
        print "Leon ist zu Besuch! Entspann' eine Runde mit ihm!. *Deine Genervtheit sinkt um 1 und deine Intelligenz steigt um 1*"
        stats[3] = stats[3] -1
        stats[5] = stats[5] +1
    elif brett[y][x] == Geheim:
        if geheim_count == 0:
            print "Du findest den geheimen Pornokeller! Aber du bist zu schuechtern, ihn zu betreten. *Du erhaeltst die Charakterstaerke Sexiness*"
            stats.append("Sexiness: ")
            stats.append(1)
            geheim_count = geheim_count + 1
        elif Geheim > 0:
            print "Du warst schon beim Pornokeller. Nichts Neues hier!"
            geheim_count = geheim_count + 1
        
    elif brett[y][x] == X:
        print "Nichts passiert"
    elif brett[y][x] == Exit:
        print "Du hast den Ausgang gefunden!"
        if stats[1] > 1:
            if stats[5] > 1:
                if stats[7] > 1:
                    print "Herzlichen Glueckwunsch! Du hast alle Eigenschaften erworben, um der grosse Konradictus zu werden! Das Kuscheltier ist weg, du bist kreativ, und auch noch clever! Du hast dir ein Bier verdient!"
                    end = True
                elif stats[7] <= 1:
                    print "Du bist leider noch nicht kreativ genug! Trainiere deine Kreativitaet und komm' dann wieder!"
            elif stats[5] <= 1:
                print "\"Ich Konrad, du Jane!\" Es scheint so, als waerst du noch nicht allzu clever... Trainiere deine Intelligenz und komm' dann wieder!"
        elif stats[1] <= 1:
            print "Ein Plueschtier faellt dir in den Weg. Du bist zu schwach, es wegzuraeumen! Trainiere deine Kraft und komm' dann wieder!"
    if stats[3] >= 5:
        print "Du bist zu genervt, um weiter deinem Ziel, der grosse Konradictus zu werden, nachzugehen. Trinke ein Bier und probiers' nochmal!"
        end = True
        
#Endstatement
else:
    input = raw_input("Tippe \"start\" um erneut zu spielen:")
    if input == "start":
        x = x_start
        y = y_start
        end = False


# In[ ]:




