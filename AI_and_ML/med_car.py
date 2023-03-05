"""
Robot, který:
 a) je řízen na dálku, ale při poruchách spojení pracuje samostatně
 b) je schopen rozpoznat objekt, identifikovat jeho části a jejich kvalitu (barva, velikost atd.)
 c) na základě computer vision, AI aj. zhodnotí životní funkce a postup zajištění první pomoci
    - dýchání, TT, pohyb, reakce na podněty atd. -> přítomnost poruch (krvácení, zástava dechu aj.)
    - dokaže najít vhodný způsob řešení problémů (zajištění žilního vstupu a aplikace léků, zastava krvacení atd.)
 d) umí zhodnotit rizika okolí a eleminovat je
 e) transport je optimální (tlumení při jizdě po nerovnostech, zahřívání prostoru, vlhkost atd.)
 f) odolnost vůči útokům, signálovému šumu aj.
 g) je schopen manipulovat se závažím velmi jemně a jistě
Minimum: a,e,g
Jedná se o auto řízené na dálku, schopné manipulovat se závažím o hmotnosti cca 150 kg
Takže:
    Mechanická část: konstrukce (Kostra a svaly)
    Programovácí část: řízení a vidění (Mozek) - část kódu lze 'ukradnout' z PC her (např.JOY Stick ovládání)
"""
