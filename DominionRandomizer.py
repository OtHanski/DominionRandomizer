import random as rng
from DRcom import *

DLC = { "Valtakunta": 1,   \
        "Elonkerjuu": 1,   \
        "Hovin_juonet": 1, \
        "Nousukausi": 1}


debug = 0
noweights = 0
kortit = {}

for pack in DLC:
    if DLC[pack]:
        cards = locals()[pack]
        for key in cards:
            kortit[key] = cards[key]
            kortit[key]["DLC"] = pack

peli = []
tyypit = {\
    "att": 0,\
    "def": 0,\
    "rev": 0,\
    "mon": 0,\
    "buy": 0,\
    "cur": 0,\
    "drw": 0,\
    "dsc": 0,\
    "act": 0,\
    "shf": 0,\
    "scr": 0,\
    "pnt": 0,\
    "del": 0,\
    "add": 0,\
    "rem": 0,\
    "trs": 0,\
}

if debug:
    print("Starting lottery")
    n =0
while(not len(peli)>9):
    arvontalista =[]
    painot = []
    if debug:
        print("Round "+str(n)+", peli nyt:")
        print(peli)
    for kortti in kortit:
        if not kortti in peli:
            w = kortit[kortti]["w"]
            arvontalista.append(kortti)
            for mod in kortit[kortti]["cmb"]:
                w+= float(kortit[kortti]["cmb"][mod])*tyypit[mod]
            if w<0:
                w=0
            if noweights:
                painot.append(1)
            else:
                painot.append(w)
    peli.append(rng.choices(arvontalista,painot)[0])
    if debug:
        print("lul")
        print(peli)
        print(peli[-1]+" lisätty")
    for kwd in kortit[peli[-1]]["kwd"]:
        tyypit[kwd] += 1
        if debug:
            print(kwd+" lisätty, nyt "+str(tyypit[kwd]))

peli.sort()

max_length = max(len(kortti) for kortti in peli)
colonychance = 0.25
for kortti in peli:
    print(f"{kortit[kortti]['cost']} {kortti:<{max_length}}\t\t({kortit[kortti]['DLC']})")
    if kortit[kortti]['DLC'] == "Nousukausi" and colonychance < 0.9:
        colonychance += 0.1
if rng.random() < colonychance:
    print(f"9 {'Platina':<{max_length}}\t\t(Nousukausi)")
    print(f"11 {'Siirtokunta':<{max_length}}\t\t(Nousukausi)")
    