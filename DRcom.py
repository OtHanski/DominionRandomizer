# att: Hyökkäys
# def: Puolustus
# rev: paljastus
# mon: raha
# buy: osto
# cur: kirous
# drw: nosto
# dsc: discard
# act: toiminto
# shf: sekoitus, syklaus
# scr: scry, 
# pnt: piste
# del: tuhous
# add: lisää pakkaan
# rem: poista pakasta
# trs: Treasure

Valtakunta = {\
    "Byrokraatti": {"kwd": ["att","add","scr"], \
                    "cmb": {"att":-0.1},"w":1,\
                    "cost": 4, \
                    "requires": []}, \
    "Juhlat": {"kwd": ["act","buy","mon"],\
                    "cmb":{}, "w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Kaivos": {"kwd": ["del","add","mon"],\
                    "cmb":{},"w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Kansleri": {"kwd": ["mon","shf"],\
                    "cmb":{},"w":1,\
                    "cost": 3, \
                    "requires": []},\
    "Kappeli": {"kwd": ["del"],\
                    "cmb":{"cur": 0.75},"w":1,\
                    "cost": 2, \
                    "requires": []},\
    "Kellari": {"kwd": ["act","drw","dsc"],\
                    "cmb":{"pnt": 0.35, "cur": 0.35},"w":1,\
                    "cost": 2, \
                    "requires": []},\
    "Kirjasto": {"kwd": ["drw","mon","pnt"],\
                    "cmb":{"dsc": 0.5},"w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Koronkiskuri": {"kwd": ["del","mon"],\
                    "cmb":{"buy": 0.5,"mon":-0.05},"w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Kylä": {"kwd": ["act","drw"],\
                    "cmb":{"act": -0.1,"drw":-0.05}, "w":1,\
                    "cost": 3, \
                    "requires": []},\
    "Laboratorio": {"kwd": ["act","drw"],\
                    "cmb":{"act": -0.05, "drw": -0.15}, "w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Metsuri": {"kwd": ["buy","mon"],\
                    "cmb":{"buy":-0.15,"mon":-0.05}, "w":1,\
                    "cost": 3, \
                    "requires": []},\
    "Muutostyö": {"kwd": [ "del","add" ],\
                    "cmb":{"del":-0.15,"add":-0.1}, "w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Noita": {"kwd": [ "drw","cur","att"],\
                    "cmb":{"del":0.2, "drw": 0.05,"att":-0.07}, "w":0.5,\
                    "cost": 5, \
                    "requires": []},\
    "Nostoväki": {"kwd": [ "mon","att","dsc" ],\
                    "cmb":{"drw":0.1}, "w":0.8,\
                    "cost": 4, \
                    "requires": []},\
    "Pidot": {"kwd": [ "add" ],\
                    "cmb":{}, "w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Puutarha": {"kwd": [ "pnt" ],\
                    "cmb":{"buy": 0.2, "cur": 0.2, "add": 0.1}, "w":0.3,\
                    "cost": 4, \
                    "requires": []},\
    "Raatihuone": {"kwd": [ "drw","buy" ],\
                    "cmb":{}, "w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Seikkailija": {"kwd": ["drw","mon","scr"],\
                    "cmb":{"cur":0.3, "pnt": 0.3}, "w":0.4,\
                    "cost": 6, \
                    "requires": []},\
    "Takomo": {"kwd": ["drw"],\
                    "cmb":{"drw":-0.3}, "w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Tori": {"kwd": [ "drw","act","buy","mon" ],\
                    "cmb":{}, "w":1,\
                    "cost": 5, \
                    "requires": []},\
    "Työpaja": {"kwd": ["add"],\
                    "cmb":{"pnt": 0.5}, "w":1,\
                    "cost": 3, \
                    "requires": []},\
    "Vakooja": {"kwd": [ "att","drw","act","scr" ],\
                    "cmb":{"att":-0.1}, "w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Vallihauta": {"kwd": ["def","drw"],\
                    "cmb":{"att": 0.8}, "w":0,\
                    "cost": 2, \
                    "requires": []},\
    "Valtaistuinsali": {"kwd": [ "act" ],\
                    "cmb":{"act":0.1}, "w":1,\
                    "cost": 4, \
                    "requires": []},\
    "Varas": {"kwd": ["att","scr","del","add"],\
                    "cmb":{"att":-0.1}, "w":1,\
                    "cost": 4, \
                    "requires": []}\
}
  

Elonkerjuu = {\
    "Ennustaja": {"kwd": ["mon", "att", "scr"],\
                "cmb":{"att":-0.1},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Hevoskauppias": {"kwd": ["buy", "mon", "dsc", "def"],\
                "cmb":{"att":0.4, "def": -0.8},"w":0,\
                "cost": 4, \
                "requires": []},\
    "Jahti": {"kwd": ["act", "drw", "scr"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Jälleenrakennus": {"kwd": ["rem", "add"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Kyläraitti": {"kwd": ["act", "drw", "buy"],\
                "cmb":{},"w":1,\
                "cost": 2, \
                "requires": []},\
    "Markkinat": {"kwd": ["pnt"],\
                "cmb":{},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Narri": {"kwd": ["mon", "att", "scr", "add"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Nuori noita": {"kwd": ["drw", "dsc"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": ["extra"]},\
    "Runsaudensarvi": {"kwd": ["add"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Sadonkorjuu": {"kwd": ["mon", "shf"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Talonpoikaiskylä": {"kwd": ["act", "drw", "scr"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Turnajaiset": {"kwd": ["act", "rem", "add"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": ["Palkinnot - Elonkorjuu"]},\
    "Villieläintarha": {"kwd": ["act", "drw"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []}\
}