import string
import random
if __name__ == '__main__':
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    #print(s1, s2, s3, s4)
    site = input("enter site name: ")
    while True:
        plen = input("enter password length: ")
        if plen.isdigit():
            plen = int(plen)
            break
        else:
            print("wrong input**")

    genPass = ""
    for i in range(plen):
        tp = i % 4
        if tp == 0:
            genPass += random.choice(s1)
        elif tp == 1:
            genPass += random.choice(s2)
        elif tp == 2:
            genPass += random.choice(s3)
        else:
            genPass += random.choice(s4)
    print(genPass)

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
   # print(s)
    random.shuffle(s)
    # print(s)
    print("".join(s[0:plen]))
    genPass = "".join(random.sample(s, plen))
    print(genPass)
    fp = open("pass.txt", "a")
    fp.write(site+" :> "+genPass+"\n")
    fp.close()
