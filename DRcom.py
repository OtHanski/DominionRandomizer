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

Hovin_juonet = {\
    "Salainen Kammio": {"kwd": ["mon", "def", "scr"],\
                "cmb":{"att":0.4, "def": -0.8},"w":0,\
                "cost": 2, \
                "requires": []},\
    "Paroni": {"kwd": ["buy", "mon", "del", "add"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Silta": {"kwd": ["buy", "mon"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Vehkeilijä": {"kwd": ["mon", "drw", "act"],\
                "cmb":{"act":0.1},"w":0.7,\
                "cost": 4, \
                "requires": []},\
    "Kupariseppä": {"kwd": ["mon"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Sisäpiha": {"kwd": ["drw", "scr"],\
                "cmb":{},"w":1,\
                "cost": 2, \
                "requires": []},\
    "Rautapaja": {"kwd": ["add", "act", "mon", "drw"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Naamiaiset": {"kwd": ["drw", "del"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Kaivoskylä": {"kwd": ["drw", "act", "mon", "del"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Kätyri": {"kwd": ["act", "mon", "dsc", "drw", "att"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Apuri": {"kwd": ["mon", "act", "buy", "drw"],\
                "cmb":{},"w":1,\
                "cost": 2, \
                "requires": []},\
    "Tihulainen": {"kwd": ["att", "del"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Tiedustelija": {"kwd": ["act", "scr"],\
                "cmb":{"pnt": 0.2},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Hökkelikylä": {"kwd": ["act", "drw"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Käskynhaltija": {"kwd": ["drw", "mon", "del"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Huijari": {"kwd": ["mon", "att", "del"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Kiduttaja": {"kwd": ["att", "drw", "cur", "dsc"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Kauppa-asema": {"kwd": ["del", "add"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Kymmenykset": {"kwd": ["act", "mon", "drw"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Parannustyö": {"kwd": ["drw", "act", "del", "add"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Toivomuskaivo": {"kwd": ["drw", "act"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Suuri sali": {"kwd": ["drw", "act", "pnt"],\
                "cmb":{"pnt": -0.1},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Aateliset": {"kwd": ["act", "drw", "pnt"],\
                "cmb":{"pnt": -0.1},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Haaremi": {"kwd": ["mon", "pnt"],\
                "cmb":{"pnt": -0.1},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Herttua": {"kwd": ["pnt"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []}\
}

Nousukausi = {\
    "Aarre": {"kwd": ["trs","add"],\
                "cmb":{"trs": -0.2},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Ahjo": {"kwd": ["del", "add"],\
                "cmb":{},"w":1,\
                "cost": 7, \
                "requires": []},\
    "Holvi": {"kwd": ["drw","mon"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Hämärät varat": {"kwd": ["trs", "buy"],\
                "cmb":{"trs":-0.2},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Kauppareitti": {"kwd": ["buy", "mon", "del"],\
                "cmb":{},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Kaupunki": {"kwd": ["drw", "act", "buy"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Kulkukauppias": {"kwd": ["drw", "act", "mon"],\
                "cmb":{"act": 0.15},"w":0.3,\
                "cost": 8, \
                "requires": []},\
    "Kuninkaan hovi": {"kwd": ["act"],\
                "cmb":{},"w":1,\
                "cost": 7, \
                "requires": []},\
    "Laajennus": {"kwd": ["del", "add"],\
                "cmb":{},"w":1,\
                "cost": 7, \
                "requires": []},\
    "Laina": {"kwd": ["trs", "del"],\
                "cmb":{"trs":-0.1},"w":1,\
                "cost": 3, \
                "requires": []},\
    "Louhos": {"kwd": ["trs"],\
                "cmb":{"trs":-0.2},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Monumentti": {"kwd": ["mon", "pnt"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Palkkio": {"kwd": ["trs"],\
                "cmb":{"trs":-0.1},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Pankki": {"kwd": ["trs"],\
                "cmb":{"trs":-0.1},"w":1,\
                "cost": 7, \
                "requires": []},\
    "Piispa": {"kwd": ["mon", "del"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Petkuttaja": {"kwd": ["mon","cur","att"],\
                "cmb":{"cur":-0.5, "att":-0.5},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Rahapaja": {"kwd": ["add", "del"],\
                "cmb":{"trs":0.2},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Rahvas": {"kwd": ["att", "scr", "drw"],\
                "cmb":{"att":-0.4},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Roistot": {"kwd": ["buy","mon", "att", "pnt"],\
                "cmb":{},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Sinetti": {"kwd": ["trs", "scr"],\
                "cmb":{"trs":-0.2},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Suurtori": {"kwd": ["act", "drw", "buy", "mon"],\
                "cmb":{},"w":1,\
                "cost": 6, \
                "requires": []},\
    "Talismaani": {"kwd": ["trs", "add"],\
                "cmb":{"trs":-0.2},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Tilitoimisto": {"kwd": ["mon"],\
                "cmb":{},"w":1,\
                "cost": 5, \
                "requires": []},\
    "Työläiskylä": {"kwd": ["drw", "act", "buy"],\
                "cmb":{},"w":1,\
                "cost": 4, \
                "requires": []},\
    "Vartiotorni": {"kwd": ["drw", "scr", "def", "del"],\
                "cmb":{"att":0.2},"w":1,\
                "cost": 0, \
                "requires": []}\
}