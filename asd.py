'''
T = Tenger
V = viz
H = Hegy
B = Barlang
O = Oltar
J = jungel
P = Piramis
L = Lava : 30% dmg per round
. = Talaj
N = Nedves_talaj : 80% energy cost
R = rekettyes : 40% energy cost
r = vizes rekettyes
F = falu
f = vizes falu
S = szentely
C = csonak
'''


def display_village():
    print(("\n") * 10)
    print(
        "                   ~~ THE VILLAGE ~~                                                                        ")
    print(
        "                                                                                                             ")
    print("                                                              (')) ^v^  _           (`)_                   ")
    print(
        "           _   _._                    .-. ,-.                 (__)_) ,--j j-------, (__)_)                  ")
    print("          |_|-'_~_`-._               '   (%%'`.                     /_.-.___.-.__/ \                    ")
    print("       _.-'-_~_-~_-~-_`-._            `-(%|%)% )                   /_.-.___.-.__/ \                   ")
    print("   _.-'_~-_~-_-~-_~_~-_~-_`-.           (%\K /,                   ,8| [_],-.[_] | oOo                   ")
    print(
        "  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         %.\V/%.)              ,,,oO8|_o8_|_|_8o_|&888o,,,hjw                ")
    print("    |  []  []   []   []  [] |          (%\%`(',                           ~        ")
    print("    |           __    ___   |            %| ,)                         ~ ~          ")
    print("  ._|  []  []  | .|  [___]  |_._._._._._._|_|_._._._._._._._._.      ~  ~           ")
    print("  |=|________()|__|()_______|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|=|   ~    ~            ")
    print("^^^^^^^^^^^^^^^ === ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^    ~             ")
    print("")


def display_merchant():
    print(("\n") * 10)
    print("                                     ,                           ")
    print("                                 _.='/|              ~~ UFF! ~~                     ")
    print("                              ,/`\ /` |     ~~ I'm the merchant in the village. ~~ ")
    print("                             /\ ./' =/      ~~ Check out my fancy merchandise! ~~ ")
    print("                           /` ./_ -_/        ")
    print("           .="""".=""""=./\ \/  __/__")
    print("          .---------.    \  / =_/             __ {_/")
    print("         /^\______/^\`-._ \/ __/              \_}\\ _")
    print("        //^\\    ' /\\-. '.\_/'                  _\(_)_")
    print("       //_/^\     /  \  `. \..                  (_)_)(_)_")
    print("     .'   .'`    '-./^\   ;/ _`)               (_)(_)_)(_)")
    print("  .-'    /           `'     / \|                (_)(_))_)  ____")
    print(" / (`'-./    .              -'/'                 (_(_(_)  |    |  ____")
    print(" \  \| (   _,.`'--..,__      \`                   (_)_)   |~~~~| |    |")
    print("  `\ \ |`'`|`^^''''^^|`\      )                    (_)    '-..-' |~~~~|")
    print("    `(\|   |   |  |   .'    .'                              ||   '-..-'")
    print("      `\._ |   |_,.-'` _.-''`                              _||_    ||")
    print("        `.`''''`_.--'``                                   `''''`  _||_")
    print("          `''''`                                                 `''''`")
    print("")


def display_rest():
    print("  ()___")
    print("()//__/)_________________()")
    print("||(___)//#/_/#/_/#/_/#()/||")
    print("||----|#| |#|_|#|_|#|_|| ||")
    print("||____|_|#|_|#|_|#|_|#||/||")
    print("||    |#|_|#|_|#|_|#|_||")

def display_shrine():
    print(("\n") * 10)
    print("   `,.      .   .        *   .    .      .  _    ..          .")
    print("     \,~-.         *           .    .       ))       *    .")
    print("          \ *          .   .   |    *  . .  ~    .      .  .  ,")
    print(" ,           `-.  .            :               *           ,-")
    print("  -             `-.        *._/_\_.       .       .   ,-'")
    print("  -                 `-_.,     |n|     .      .       ;")
    print("    -                    \ ._/_,_\_.  .          . ,'         ,")
    print("     -                    `-.|.n.|      .   ,-.__,'         -")
    print("      -                   ._/_,_,_\_.    ,-'              -")
    print("      -                     |..n..|-`'-'                -")
    print("       -                 ._/_,_,_,_\_.                 -")
    print("         -               ,-|...n...|                  -")
    print("           -         ,-'._/_,_,_,_,_\_.              -")
    print("             -  ,-=-'     |....n....|              -")
    print("              -;       ._/_,_,_,_,_,_\_.         -")
    print("             ,-          |.....n.....|          -")
    print("           ,;         ._/_,_,_,_,_,_,_\_.         -")
    print("  `,  '.  `.  '.  `,  '.| n   ,-.   n |  ',  `.  `,  '.  `,  ',")
    print(",.:;..;;..;;.,:;,.;:,o__|__o !.|.! o__|__o;,.:;.,;;,,:;,.:;,;;:")
    print(" ][  ][  ][  ][  ][  |_i_i_H_|_|_|_H_i_i_|  ][  ][  ][  ][  ][")
    print("                     |     //=====\\     |")
    print("                     |____//=======\\____|")
    print("                         //=========\\")

def display_shrine_door():
    print(("\n") * 10)
    print("                       _             _,-----------._        ___")
    print("                      (_,.-      _,-'_,-----------._`-._    _)_)")
    print("                         |     ,'_,-'  ___________  `-._`.")
    print("                        `'   ,','  _,-'___________`-._  `.`.")
    print("                            ,','  ,'_,-'     .     `-._`.  `.`.")
    print("                          /,'  ,','        >|<        `.`.  `.\ ")
    print("                         //  ,','      ><  ,^.  ><      `.`.  \\")
    print("                        //  /,'      ><   / | \   ><      `.\  \\")
    print("                       //  //      ><    \/\^/\/    ><      \\  \\")
    print("                      ;;  ;;              `---'              ::  ::")
    print("                      ||  ||              (____              ||  ||")
    print("                     _||__||_            ,'----.            _||__||_")
    print("                    (o.____.o)____        `---'        ____(o.____.o)")
    print("                      |    | /,--.)                   (,--.\ |    |")
    print("                      |    |((  -`___               ___`   ))|    |")
    print("                      |    | \\,'',  `.           .'  .``.// |    |")
    print("                      |    |  // (___,'.         .'.___) \\  |    |")
    print("                     /|    | ;;))  ____) .     . (____  ((\\ |    |\ ")
    print("                     \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;")
    print("                      |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|")
    print("                      |   `..  ' / \__.'         `.__/ \ `  ,.'   |")
    print("                      |    |,\  /,                     ,\  /,|    |")
    print("                      |    ||: : )          .          ( : :||    |")
    print("                     /|    |:; |/  .      ./|\,      ,  \| :;|    |\ ")
    print("                     \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;")
    print("                      |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|")
    print("                      |   `..   ,' `'       '       `  `.   ,.'   |")
    print("                      |    ||  :                         :  ||    |")
    print("                      |    |'  |            _            |  `|    |")
    print("                      |    |   |          '|))           |   |    |")
    print("                      ;____:   `._        `'           _,'   ;____:")
    print("                     {______}     \___________________/     {______}")
    print("                 SSt |______|_______________________________|______|")

def display_shrine_runes():
    print(("\n") * 20)
    print("|    |\   |      /|  |\  |/")
    print("|/   | |  |>     /|  |/  |")
    print("|/   |    |       |  |\  |")
    print("")
    print("\|/     \|   |   |   /   /|\ ")
    print(" X       |   |   |   \    |")
    print("/|\      |\  |  /|   /    |")
    print("")
    print("|\   |\  \|/   |    |/   /\ ")
    print("|<   |    |    |    |    \/")
    print("|/   |    |   /|\  /|    /\ ")

def display_shrine_room():
    print(("\n") * 20)
    print("+------------------------------------+ ")
    print("|#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW| ")
    print("|#####|<(Zha'kyr kaun hg'agalas yr!)>| ")
    print("|#####|WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW| ")
    print("|#####|WWWWWWWWWW.----.WWWWWWWWWWWWWW| ")
    print("|#####|WWWWWWWW,'  ||  `.WWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI   _||_   IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI  ' || `  IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI    ||    IWWWWWWWWWWW| ")
    print("|#####|WWWWWWWI____||____IWWWWWWWWWWW| ")
    print("|#####/_o_                           | ")
    print("|####/  X                            | ")
    print("|###/  ' `                           | ")
    print("|##/                                 | ")
    print("|#/                                  | ")
    print("|/                                   | ")
    print("+------------------------------------+ ")

def display_shrine_doll():
    print(("\n") * 20)
    print("            .-.'  '.-.")
    print("           __  \\//  __")
    print("          '_ `\\||//` _'")
    print("          ' '\/`""`\/' ' ")
    print("           .-/ o  o \-.")
    print("    ()-------\_-==-_/")
    print("           ____)  (____")
    print("        .--\   \__/   /--.")
    print("        '--/__      __\--'")
    print("              |____|--------()")
    print("     ()-------/~~~~\ ")
    print("             /      \ ")
    print("            <_/\__/\_>")
    print("           _/  /  \  \_")
    print("          (___/    \___)")

def display_shrine_chest():
    print(("\n") * 25)
    print("                    ____...------------...____")
    print("               _.-'` /o/__ ____ __ __  __ \o\_`''-._")
    print("             .'     / /                    \ \     '.")
    print("             |=====/o/======================\o\=====|")
    print("             |____/_/________..____..________\_\____|")
    print("             /   _/ \_     <_o#\__/#o_>     _/ \_   \ ")
    print("             \_________\####/_________/                   ")
    print("              |===\!/========================\!/===|")
    print("              |   |=|          .---.         |=|   |")
    print("              |===|o|=========/     \========|o|===|")
    print("              |   | |         \() ()/        | |   |")
    print("              |===|o|======{'-.) A (.-'}=====|o|===|")
    print("              | __/ \__     '-.\_X_/.-'    __/ \__ |")
    print("              |==== .'.'^'.'.====|")
    print("              |  _\o/   __  {.' __  '.} _   _\o/  _|")
    print("              `""""-""""""""""""""""""""""""""-""""`")

def display_shrine_treasure():
    print(("\n") * 20)
    print("                            ,--.")
    print("                           {    }")
    print("                           K,   }")
    print("                          /  ~Y`")
    print("                     ,   /   /")
    print("                    {_'-K.__/")
    print("                      `/-.__L._")
    print("                      /  ' /`\_}")
    print("                     /  ' /")
    print("             ____   /  ' /")
    print("      ,-'~~~~    ~~/  ' /_")
    print("    ,'             ``~~~  ',")
    print("   (                        Y")
    print("  {                         I")
    print(" {      -                    `,")
    print(" |       ',                   )")
    print(" |        |   ,..__      __. Y")
    print(" |    .,_./  Y ' / ^Y   J   )|")
    print(" \           |' /   |   |   ||")
    print("  \          L_/    . _ (_,.'(")
    print("   \,   ,      ^^""' / |      )")
    print("     \_  \          /,L]     /")
    print("       '-_~-,       ` `   ./`")
    print("          `'{_            )")
    print("              ^^\..___,.--`")

def display_curse_volcano():
    print(("\n") * 20)
    print("                        (   (( . : (    .)   ) :  )")
    print("                          (   ( :  .  :    :  )  ))")
    print("                           ( ( ( (  .  :  . . ) )")
    print("                            ( ( : :  :  )   )  )")
    print("                             ( :(   .   .  ) .'")
    print("                              '. :(   :    )")
    print("                                (   :  . )  )")
    print("                                 ')   :   #@##")
    print("                                #',### ' #@  #@")
    print("                               #/ @'#~@#~/\   #")
    print("                             ##  @@# @##@  `..@,")
    print("                           @#/  #@#   _##     `\ ")
    print("                         @##;  `#~._.' ##@      \_")
    print("                       .-#/           @#@#@--,_,--\ ")
    print("                      / `@#@..,     .~###'         `~.")
    print("                    _/         `-.-' #@####@          \ ")
    print("                 __/     &^^       ^#^##~##&&&   %     \_")
    print("                /       && ^^      @#^##@#%%#@&&&&  ^    \ ")
    print("              ~/         &&&    ^^^   ^^   &&&  %%% ^^^   `~._")
    print("           .-'   ^^    %%%. &&   ___^     &&   && &&   ^^     \ ")
    print("          /    ^^^ ___&&& x & && |n|   ^ ___ %____&& . ^^^^^   `.")
    print("                   |M|       ---- .  ___.|n| /\___\  X")
    print("                             |mm| X  |n|X    ||___|        ")

def display_curse_geyser():
    print(("\n") * 20)
    print("         ____ /\ ____            _ _   --           - -__     -_")
    print("        /v y \/\/    \                   --  --___     _ __--__ -' _")
    print("       ____\7 \\_^_^/ \                            _ --        -_ '-_")
    print("     /    V/ \/   \ ^/\            __                          _--,_")
    print("     / \^\|/ \()^7_ \ ^|      /'>^/',,\                        /'('\'\ ")
    print("    /\^   / \^_() 7_\        LX<'<,\                    _/'/'|\ )\>_")
    print("    |^    /\ ()_|  7|        / >/ >O-,\'                 _/'_.' _/ / / \'\ ")
    print("          ^   \_\            ^' V'O^  V               /''_-' ,/'  /\  \ ) '-,_")
    print("               \_\              '  \>              _-'/ ( .-/ \ !   )  \ _\'-_'\_")
    print(" ___ ___ ______ \_\ _ _____ ___ ___ \> _ ___   _-'/_-'   / (    |  / \  | \  \_- '-_ ")
    print("       _  _ _-   \_\   --  -   - --  \'>   -<_'__' /  _/|   \ \ | /! \  \  -_( _'-<_'>-- -")
    print("              --  \_`>    _--    _ ___','>-____ _'> ''_' '--'--'-' '-'' '-'  ''  _ ")
    print('                   \__">      C"" -_O   "O-"           "">        __ -  - ')
    print("         _ __()_ ___'-__'\__ __)    - O         __ - - '      - -")
    print("                ()   _'>--'> _ .-- '      - '''")
    print("")
    print('                        """')

def display_crew():
    print("                                                                                            ,")
    print("                                                                                           /:\ ")
    print("                                                                                           >:<   ~WISE~ ")
    print("                                                                                           >:<")
    print("      ~SOLDIER~                                                                            >:<")
    print("          .-.                              ~TRADER~                                   ,,,,,\:/                      ~DONKEY~")
    print("   .-.   /   \                                      .-.                              #########         /\          /\ ")
    print("  |   `./     \           .||                      '   `                            //////\ \ \       (  \        // )")
    print("  |            |           ||                     /     \                          // /_\ /_\ \        \  \      // /")
    print("  |            |           ||_                    |.---.|                          \(  0 _ 0  )/        \_ \||||//_/")
    print("  |            /_.-''''.   |  |           __....--'^'^''^`--....__                 /\ =  _\ =//\         \/ _  _ \ ")
    print("   \        _.-'        \  | -'       (`--'         .---.         `--')            \ /\ --- /\//        \/|(O)(O)|")
    print("   .-```-.__..-'            | '|  \.-. \          .' (_) `.          /             //\ '---' / \       \/ |      |")
    print("  /                         '  d/)(/(/| `._______(  .-.-.  )_______.'              \//_______\ /______\/  \      /")
    print("  |          _,.,-''`-..   /    \ \`._|  _   __...-'     `-...__                  //                //     |____|")
    print("  \       ,-'  .-.  O ) \-'     |   |   / \  \_     _/|\_     _/                 //                ||     /      \ ")
    print("   `.._.,'( O (   )_-'   |    .'    |-..\|/. --.'-''\_|_/'''-'''---.            //|                \|     \ 0  0 /")
    print("        |  `-,-.,.' ``.  |   /__    |`-.\|/.-'  `._ `---'  .' ,--.\            // \       )         V    / \____/")
    print(" ___:..-'  |  `.   `-..._ //`=._|`\ \|/ /'.--. `-...--' \ .`  \               //   \     /        (     /")
    print("    /.\_     _/,---.\-..._.,_//  \_`-..:::::,.-'_/     ,'  \.'|  .-----.     ''     \   /_________|  |_/")
    print(".-----. `'.'' \     |     |--' .--. ,'--.-.--`, .--.  ' \,-'   \ |     /            /  /\   /     |  ||")
    print("\     |   |    \    |     |    \_`-( = (___) = )-'_/ \_,'       \|    ,^.       __ /  / /  /      \  ||")
    print(" \    |   |     \,,/      |     .--.`- .---. -'.--. ,'          |/ __ ' `     ,'  '. |  | |        | ||")
    print("/  __ \   |               |     \.---`._____.'---./             / (  )|x|    /_    _\|  | |        | ||")
    print("\ (  ) \  |____ .---. ____|     ~|               |~           .' \_)/ | |   /  \  // \  |_|        |_||")
    print(" \ \(_/   |iii_(     )_iii|     ~|  |         |  |~ _________/_.-. (_/| |  (|(o)  (o)|)  \_\        \_\   ")
    print("  \_) .-._|______---______|     ~|  |  /)_    |  |~          / -.|    | |   \   ''   /      ")
    print("      |.-  \    /   \    /      ~|__| /| /    |__|~ _-^-_____|_|      ,'-,---\ /''\ /-.      ")
    print("        |_||    |   |    |        ||_//|/     |||_  /   \   /||       `.-----'\`'' /-, |      ")
    print("         |||    |   |    |       (  /(/       /.-.\ |   |   |||       | |     .\  /.,| |       ")
    print("       __.-' ====* *==== `-.__    \ \;;;;;;;;;\) )))|   |   |         | |    / /\/\ \/|\       ")
    print("       \____/|__|   |__|\____/  // ~|      __|      ==* *=== `-.__    | |    |`|  |`|      ")
    print("                                   _|___/\___|_    |_|   |_|\____/    | |    | |  | |          ")
    print("                                  (____)  (____)                      |_|   ///`  '\ \         ")
    print("                               ~SCOUT~                                            ~SHAMAN~ ")

def display_bag():
    print(("\n") * 20)
    print("   .eec.              .e$$$c   ")
    print("  z$*'*$$eec..       zP  .3$c     ~BACKPACK~   ")
    print(" .$'  d$'  '''****bee*=*'' *$    ")
    print(" $%  d$$                   ^$%")
    print(".$  z$%$bc.                 $%  ")
    print("4F 4$' $'^$*ec..  .ee.    ./' b ")
    print("dF $P  P  F   '''''3F''''''   4 ")
    print("3b4$   '           $F         4 ")
    print("4$$$  -            $F         4")
    print(" $$$               $F         4 ")
    print(" *$$               $F         @ ")
    print(" 4$$               $F         F   ")
    print(" ^$F   .......     $F        .F  ")
    print('  $"  z"     ^"""""$F"""""""""%. ')
    print(" 4$  4F     e      $L          '.")
    print(" 4F  ^L    4$     z%'c    *.    b  ")
    print(" d    ^$*=e$$eer=$"  "be..JL..ee* ")
    print(" $     $   $F    $   zP   4P   F ")
    print(" F     F   $F    4. .P    d%  J")
    print("4%     F   $F     F $'   zP   P ")
    print("J      F   '%     Fd'   4P   4'")
    print("$      F          $F         P")
    print("$      L         .$         4% ")
    print("*      '.       .$$.       .$ ")
    print("'       ^'****'''  '*******$'")
    print(" %                        .P  ")
    print("  *c                     .@  ")
    print("   ^'%4c...        ...zed*  ' ")
    print('         ^""""""""')
    print()