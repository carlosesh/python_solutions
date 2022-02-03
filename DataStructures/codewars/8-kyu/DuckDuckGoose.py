import unittest
import random

"""
The objective of Duck, duck, goose is to walk in a circle, tapping on each
player's head until one is chosen.

Given an array of Player objects and an index (1-based), return the name of the
chosen Player(name is a property of Player objects, e.g Player.name)

Example:

duck_duck_goose([a, b, c, d], 1) should return a.name
duck_duck_goose([a, b, c, d], 5) should return a.name
duck_duck_goose([a, b, c, d], 4) should return d.name

"""


def duck_duck_goose(players, goose):
    count = 0
    players_length = len(players)

    if goose <= players_length:
        return players[goose - 1].name
    else:
        i = 0
        while i < players_length:
            if i == (players_length - 1):
                if count == goose - 1:
                    break
                i = 0
                count += 1
                continue
            elif count == goose - 1:
                break
            else:
                count += 1
                i += 1
        return players[i].name


def duck_duck_goose_improved(players, goose):
    return players[(goose % len(players)) - 1].name


class Player:
    def __init__(self, name):
        self.name = name


class DuckDuckGoose(unittest.TestCase):
    ex_names = ["a", "b", "c", "d", "c", "e", "f", "g", "h", "z"]
    players = list(map((lambda x: Player(x)), ex_names))

    def test_duck_duck_goose(self):
        self.assertEqual(duck_duck_goose(self.players, 1),  "a")
        self.assertEqual(duck_duck_goose(self.players, 3),  "c")
        self.assertEqual(duck_duck_goose(self.players, 10), "z")
        self.assertEqual(duck_duck_goose(self.players, 20), "z")
        self.assertEqual(duck_duck_goose(self.players, 30), "z")
        self.assertEqual(duck_duck_goose(self.players, 18), "g")
        self.assertEqual(duck_duck_goose(self.players, 28), "g")
        self.assertEqual(duck_duck_goose(self.players, 12), "b")
        self.assertEqual(duck_duck_goose(self.players, 2),  "b")
        self.assertEqual(duck_duck_goose(self.players, 7),  "f")

    def test_duck_duck_goose_improved(self):
        self.assertEqual(duck_duck_goose_improved(self.players, 1),  "a")
        self.assertEqual(duck_duck_goose_improved(self.players, 3),  "c")
        self.assertEqual(duck_duck_goose_improved(self.players, 10), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 20), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 30), "z")
        self.assertEqual(duck_duck_goose_improved(self.players, 18), "g")
        self.assertEqual(duck_duck_goose_improved(self.players, 28), "g")
        self.assertEqual(duck_duck_goose_improved(self.players, 12), "b")
        self.assertEqual(duck_duck_goose_improved(self.players, 2),  "b")
        self.assertEqual(duck_duck_goose_improved(self.players, 7),  "f")

    def test_random_input(self):
        names = ["discusmeticulous", "robertsapplaud", "liquidrowdy", "ammoniabeldon", "newleaking", "nosedfreedom", "slovenianpredictive", "displayedtrenton", "draughtspheroid", "chewyfairy", "hampbaloo", "saultbio", "achingchest", "relaxwagger", "samariumpissed", "pilototis", "rhodiumseeka", "picklechoose", "alterdomain", "ageschemical", "jetstinchar", "publisherpostit", "decisivecrater", "groinshergar", "mainmastyoda", "ornatesleepover", "fillerturkey", "herbentertain", "investorsdomino", "lliweddtaiga", "loanfond", "peduncleinventory", "derbyshireserpens", "hammondhoop", "winstonwestfield", "seminoleutensil", "surdjangle", "binnaclebubba", "hoovesrecent", "hawserforehead", "milderholy", "runservlet", "directmashed", "wobblyursa", "wackmahjong", "rescuebook", "postmangrowl", "nanaimofervent", "systemjiggle", "watermeloncroasdale", "kingstonsmirk", "hillsfeisty", "luckyserin", "tradeverde", "tubbytripadvisor", "copapplejack", "screechingbold", "vapidbillingham", "anoraklumber", "cronzgrotesque", "syllablesworthwhile", "axelinitial", "pembrokecarbonate", "cullionsdroppings", "nappiesfunding", "antlilly", "carrotssecretariat", "britishshelter", "colorlesschromate", "scribblecommunal", "jumbowool", "tinyinfirm", "intestineabject", "forwardupset", "dykemontie", "indigoeight", "cheesynorton", "pointsmeta", "londonderrygaia", "taunteffluvium", "stringmanaged", "pulsarfantastic", "payingvenerated", "filmsbeijing", "sinusginger", "quotienttail", "shetlandcobra", "pausefag", "leafhysterical", "deliciouscecil", "olliedatabase", "livermoriumpants", "bobolinknugget", "transomlipped", "napoleonmadison", "advisorbank", "cardiffthorough", "frogsslimy", "flutherstrut", "improvechurch", "psammiterolly", "hornsponge", "eventprocess", "jerkycodswallop", "husbandfinalist", "arsexenon", "socialvitamin", "climbingegret", "peelwavelength", "ceramictern", "horsebackflagellum", "closedaffy", "polewrestlers", "fundscocoa", "copysing", "munchingnotebook", "reportrutland", "unsuitableensorcell", "fryerforefoot", "planemoniobrara", "purserupture", "answerhandler", "dykeiceland", "weixinmasticate", "gwendraethcraton", "flapswain", "oreoproton", "instagramcurium", "lacunamortician", "nevercomic", "shovelsnapping", "travelerhefei", "tobermoryplonk", "staithesmullion", "wallophuygens", "taipeisleuth", "usdunicode", "stunsute", "sproutpolicies", "indicespools", "gastropubbring", "rosaceachancellor", "shysterbipolar", "cascadedundo", "teachingmatch", "barbequedbilliards", "poodlewelcome", "scientifichassium", "grotesquepentland", "beneathextinction", "josiehung", "impartialmustache", "macaroontoll", "ontariodrizzly", "wombadimension", "diligenceearth", "auditils", "roskhillfume", "spicaflats", "electricsecondhand", "radblessing", "blondiebandage", "filletsherman", "mangledwaterloo", "milansociety", "moreenderman", "fermiumdeneb", "teasezenyatta", "menorahdoodilmore", "poopeeler", "tastesign", "resultslichen", "chevingtonbleach", "clippingcockroach", "aspenstrikethrough", "campbelltonrealize", "snowdonbailey", "glyderaustanley", "crimdonmine", "softwarefindhorn", "gwaunmontreal", "bullockssparkle", "solvastirring", "grassleesmasons", "chestherschel", "exaltedunpopular", "metrudy", "lincolngrange", "inverianviegailee", "riddlestarchy", "saintquokka", "keyliberty", "skyebusiness", "deceivesteering", "taigaexcellent", "chemistrydemurrage", "laireatable", "citrinerogue", "elsecounselor", "fruityzaftig", "spittalmoney", "grammarianplutonium", "earnestintend", "treenailradish", "finchgoalie", "logoutfabulous", "alluvialsend", "collegesam", "heatinghermit", "cleverupright", "carotidsickness", "realmthrasher", "labcoatditton", "svelteadopt", "peaseyforesail", "hurriedgrazed", "harmonicsupport", "currishwe", "nicoisejimbo", "beaveraled", "overcookedrolled", "denbyneat", "callistoely", "bewitchedsunflower", "tentpouch", "dysnomiahanoi", "spatulashare", "fallopianstirring", "abstractedterminally", "irishcyrus", "anyhips", "humtwitter", "yankieshrawley", "uslateral", "variablegray", "chinaboots", "hisfrancium", "hamstermixtape", "causedsled", "writerings", "chinnockstaking", "truckdiseases", "crashingsnore", "flabbyalfred", "pavoscreen", "modelegacy", "wanderthroat", "castingbevvy", "hardnessyorkshire", "tousledjournal", "daisybroderick", "pesounwieldy", "dictatewest", "pignutditton", "marriedhelvetica", "linglymphoma", "policiesghost", "heptagonitchy", "severalexpression", "clappedcaluminous", "bobblygazebo", "starvelingconfucius", "copperminelogger", "empanadaoncology", "dolphinapply", "croasdalenice", "archerymods", "meltedarena", "spot!virgo", "fibbersphene", "flickrcamel", "parrottdrunken", "romeoswainson", "colloquialember", "thumbpoll", "birdsscared", "eyepieceheavy", "sadfarnack", "montanarockwell", "hairhocks", "intervalessential", "effectorcow", "mindglasses", "dialectshag", "begantrash", "numerouschanel", "sumardalesteinbach", "gurgletags", "lockedshallow", "lightyearitself", "lutetiumapplies", "jacktobermory", "maggothomesick", "stakinglukely", "triangulumencoding", "hannadecent", "incubateskewer", "piratecambridgeshire", "mixinracked", "pigjumpringworm", "beatlongfellow", "prependrobonaut", "goalimminent", "nominationclose", "volansmalboro", "takeoutalarmed", "filletsape", "mosedaleaccess", "cockroachtrouble", "willowrenren", "parsecopen", "hawseagenda", "cakeinitiated", "gatorpotion", "craftsmanrowing", "circleclutching", "bustprotostar", "bitchstrawberry", "shortbreadunripe", "cheatonruby", "fluoridestrengthen", "barbreckclick", "leanpiquillo", "capellaeyed", "barracudagucci", "bellslips", "relayworcestershire", "barkraspberry", "lioncyclone", "nerodidactic", "fadejibboom", "hoursant", "approachbreasts", "gamesyeasty", "keyhalladale", "paperclipsweltering", "troubledruddy", "harminternal", "puncturepubic", "xpathapplies", "plateletartificial", "smallintdeschutes", "gateautufted", "usableupdated", "whitepicking", "brockeyebuttercream", "goillouie", "egadcoffle", "therapyfairs", "bitscougar", "badgworthypalette", "winterfavorable", "meigskark", "whimsicalarray", "dieselrico", "jazzsteeve", "glazemailer", "wavetrolly", "missionbollers", "favorpopinjay", "heidifrida", "cyclicjarring", "twiteacrid", "noddingprolapse", "treenaildecimal", "calcitegeronimo", "etherealcred", "spiritbutcher", "foldingtip", "cloverproduce", "loggercharge", "patepapoose", "averonpolyester", "cheshirelexus", "tourrydberg", "hangeruno", "hawkinghumanist", "outragedinfuriated", "sophitaz", "boysudbury", "visitsbustard", "maskdoting", "tutorbaffin", "passcrush", "smartiescrowhop", "offensivedunny", "studiedsinful", "nonstopderry", "greasyflank", "eddiespanish", "bulldarkened", "rustynotes", "mineradopt", "trenchheard", "hashtaggitano", "dexterticket", "universalblob", "harmlessopencart",
                 "eynortperiod", "uncheckedjellies", "izmirpimento", "angelstone", "mimosadecipher", "yearningflushing", "limitingdisplay", "scentedsupplier", "lippedblush", "opennaden", "squidnebraska", "marmaladecluster", "crushrelieved", "ovenbirdbiscuit", "meticuloustarbert", "noveltystepper", "faltercolburn", "confirmedecozone", "cowboycam", "jugglingheptagon", "depressedcarillon", "picayunecrest", "elatedalarming", "questbaloo", "northamptonshirepluto", "shingleskraft", "flavourederror", "bundevaramunted", "malakruth", "cornsincere", "kochipooh", "pretendslips", "bavinonyx", "radiostoed", "adelefarrah", "eyewoozy", "maternalsatellite", "completioncitric", "flavorfulbaps", "brockvillefig", "lucywrestling", "predicttorro", "propertycompound", "compresspanjandrum", "burningstaithes", "pridemilly", "thickdespairing", "notatedcricked", "geoffreycuts", "alsorift", "faithfulfire", "dessertsfea", "nappinglimey", "windownorma", "slugdebonair", "ticketparmesan", "afanheart", "leggingswinter", "unseasonedmoldwarp", "undaepounding", "granolamonsoon", "spawnedtanka", "trojanflawed", "bynursing", "quarterlyeast", "halidedemurrage", "cramercastration", "cratonthatched", "ariesbattery", "purchasingbeeper", "cookiescalby", "namelondon", "peachesdo", "dulekits", "collarbonekiss", "visualcheerful", "noodlesknives", "cattlearrival", "aniakchakjackie", "leoturn", "feistyfyne", "lawersbrady", "furphyzunyi", "bivycothi", "limpingwizzed", "accurateliberated", "budshanger", "selfieampere", "tearsquiche", "warningbefriend", "piggychalky", "insulateaddition", "submitnibbles", "cockneybungalow", "stomachsudanese", "aspendauphine", "deleteqed", "cheyennedownholland", "joyskull", "websitescracked", "dunslandjasper", "farnackeveryone", "statemusic", "tentfetus", "pixiegambling", "explosiveharley", "injurepeaceful", "malakgordon", "oberonorogeny", "enchantingupright", "volumetricharry", "toothsometawe", "tardypost", "sybaseoisin", "cartierchallenges", "jollypoo", "littleporsche", "bookerapollo", "rudepart", "cheerroyal", "weeklyimmersion", "lickshirtsinbulk", "layingbinnacle", "coloradobugs", "carriagestaffnet", "indelibleemm", "squawkcomb", "computerisla", "managerspretty", "contenthungarian", "wallybobble", "spacersanchor", "troglodytecenter", "trainedcarn", "inventedheat", "fawrhenry", "platformhoarse", "shawdonsoot", "daddyjansky", "newmanlarge", "nikkipeanuts", "inwee", "millieeared", "norfolkchicken", "crimdonwillow", "cheesybowen", "braytonlesser", "willflag", "wordsscare", "beggarlynewman", "royalhorden", "roentgeniumrhombus", "magnesiumeland", "bottlecog", "busysores", "cranbrookrabai", "darlingsub", "beepingbraces", "historicalcannon", "shipsmarske", "envymisty", "newtownjab", "havinganalysing", "ripeinstinct", "hocksines", "observechildren", "wenzhoualibaba", "googlehosts", "willinit", "thighsubscript", "fallantimatter", "sportduisk", "paranoidmeteorite", "graniticshaula", "casesevanescent", "gaudysociable", "liftedcab", "playersapply", "dancerbuttons", "midpointextralarge", "patterpanda", "raisinfreckles", "loathsomegrumble", "sycanaussi", "ragecatalysts", "pheasantecozone", "radianbirk", "oldhop", "mincestoppers", "allagashincrease", "pepsiescabeche", "poolfermented", "spewottawa", "pythonfeast", "breadbewildered", "bewilderedtilly", "pourvoluntary", "vestawakefield", "tongueasia", "plaitedwoodpecker", "maiseycanadian", "scriptswhoreson", "faithfulcar", "neuromarake", "scuppersimplicity", "wallopthunder", "magnetmoonshadow", "lincolnshirebolt", "theopine", "debrisjasper", "assetcrunchy", "harthashtag", "sensorzodiacal", "obsessedprime", "gelcavus", "chavpot", "templaterace", "cramponsmutton", "elmoroxie", "ribotcuban", "hinneysky", "vansoundcloud", "spewweibo", "carelessfancy", "goliathfollow", "maniacalrelax", "napkintennessee", "jasminebudweiser", "vugobsequious", "syllableshorn", "chadgin", "muggingnumnah", "weddingwealth", "zealousalberta", "soothekappa", "droppingstatics", "idefechlin", "charlestonspider", "mouldyequalizer", "bulginggrubby", "sornhick", "jerboamendip", "blesspace", "pabloapples", "shinlimbic", "samvictoriaville", "babingleyreduce", "strutsandstone", "filterzodiacal", "laboredspoiled", "oilyskype", "bangersbiscuits", "nemoland", "quietfinancials", "obeisancequote", "trainingdash", "wheelchairdishes", "soupypigeon", "coloradocustard", "resistorfrogs", "magicsaskatoon", "poomoist", "navigationvacuous", "madisonminiature", "tentequality", "quallingsebastian", "stringvanderbilt", "reactivesummerside", "lucyicon", "fissionpeduncle", "oncowboys", "dividepluto", "geminideer", "placesure", "aspenleaking", "piedopossum", "archivesship", "eleazarstudies", "fabkame", "triangularobliquity", "sinepinto", "statuesnike", "chiliroche", "cameratry", "sparkletaste", "hashwhisper", "ferocioussdraught", "fixcornea", "stiffstaking", "appaloosacurved", "streamiced", "glissadecomplex", "reggiesculptor", "eskimopipe", "bananafaraday", "hullabaloobarnaby", "americantrumpet", "yodelgreenish", "coveringcowbird", "ecozonetlikakila", "willetsiberian", "cocklefurious", "officejimmy", "cannonburgee", "billspecify", "scientificzodiacal", "horsesmarten", "portercurb", "uraniumweasel", "ptarmiganindianapolis", "welltremble", "usanarrow", "asphalttoasted", "signtrouble", "kindergartenindiscreet", "elearningthrush", "prolapsestark", "displayedsycan", "eatableunchin", "gizasirius", "professedward", "mentionoval", "harecheetah", "vaguebelle", "emeraldremington", "junglegamepad", "magellanicbellart", "quicklimereceive", "diggingracial", "topurse", "fellowshipforget", "turtledoveacrobat", "keplersoon", "pizzaactin", "lamzoe", "greetbling", "wormsphoenix", "smilingsaguenay", "journalvomit", "valhronadartmoor", "selectivepedestrian", "journalistbobbin", "monktonmeadcaroy", "photothrilling", "cartridgesherd", "bugromeo", "compoundscarp", "bodycoals", "directoryjocular", "indianapolislackluster", "tahoregina", "dislikehypergalaxy", "bikeblackjack", "infantilemen", "glossopal", "actintransferred", "footroundup", "sledgeargill", "evacuationtactful", "sneeralydar", "georgiastabber", "synclinelemur", "sycanminutes", "michigantoronto", "fonticonscotta", "miramichiunalakleet", "uggersvenogram", "floppunctual", "hettytatin", "whateverhinnisdal", "prolapseapple", "grimleybrazos", "bandanasstudent", "ruthlessspeedboat", "occultationvenogram", "venerealglowstone", "closurepeeve", "charonporcupine", "citiesdrolsay", "shrewdnesscheese", "dustyformulas", "testsdewberry", "blockbenny", "poyntoncopy", "nurserydome", "tonkdingdong", "pruneawe", "studiesoften", "pastelruby", "forelimbburp", "jaialaiuppity", "warenrat", "primesvisible", "outspokengoshawk", "supportersartistic", "kungsampson", "swingrigid", "journalscurrency", "regretfossil", "pacificintegers", "hickorygolfer", "ligamentlizard"]
        for _ in range(50):
            random.shuffle(names)
            ppl = list(map((lambda x: Player(x)), random.sample(
                names, random.randint(6, 50))))
            ind = random.randint(5000, 50000)
            ans = ppl[(ind % len(ppl)) - 1].name
            user_ans = duck_duck_goose_improved(ppl, ind)
            self.assertEqual(user_ans, ans)


if __name__ == '__main__':
    unittest.main()
