import random as ran


#Establish the names
inp = ""
names= []
print("Type names and when their are no more names type no.")
while inp != "no":
        inp = input("==")
        if inp != "no":
            names.append(inp)



#Put the names into a list
with open('names.txt', 'w') as f:
    for item in names:
        f.write("%s\n" % item)



def script(x):
    global name
    check = "n"
    with open('names.txt', 'r') as f:
        names_func = [line.strip() for line in f]

    if x in names_func:
        names_func.remove(x)
        check = "y"
    
    num = ran.randint(0, len(names_func)-1)
    name = names_func[num]
    names_func.pop(num)
    
    if check == "y":
        names_func.append(x)

    with open('names.txt', 'w') as b:
        for item in names_func:
            b.write("%s\n" % item)

orig_names = names

with open('orig_names.txt', 'w') as c:
    for item in orig_names:
        c.write("%s\n" % item)


count = 0


while count < len(names):
    p_name = input("What is your name?\n")
    #set check variable to 0
    check_auth = 0

    #If name is authenticated check is still at 0 if not its set to 1
    if p_name in orig_names:
        print("Authenticated")
    else:
        print("Sorry wrong name.")
        check_auth = 1

    #Game only runs if check is equal to 0
    if check_auth == 0:
        script(p_name)
        with open(p_name + ' Santa.txt', 'w') as a:
            a.write(name)
        count += 1
    else:
        print("Try again, write a valid name this time.")

print("Script finished.")