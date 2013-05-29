# Problem

Write a program that reads a large list of English words (e.g. from /usr/share/dict/words on a unix system) into memory, and then reads words from stdin, and prints either the best spelling suggestion, or "NO SUGGESTION" if no suggestion can be found. The program should print ">" as a prompt before reading each word, and should loop until killed.

Your solution should be faster than O(n) per word checked, where n is the length of the dictionary. That is to say, you can't scan the dictionary every time you want to spellcheck a word.

For example:

    > sheeeeep
    sheep
    > peepple
    people
    > sheeple
    NO SUGGESTION

The class of spelling mistakes to be corrected is as follows:

* Case (upper/lower) errors: "inSIDE" => "inside"
* Repeated letters: "jjoobbb" => "job"
* Incorrect vowels: "weke" => "wake"
* Any combination of the above types of error in a single word should be corrected (e.g. "CUNsperrICY" => "conspiracy").

If there are many possible corrections of an input word, your program can choose one in any way you like. It just has to be an English word that is a spelling correction of the input by the above rules.

Final step: Write a second program that *generates* words with spelling mistakes of the above form, starting with correctly spelled English words. Pipe its output into the first program and verify that there are no occurrences of "NO SUGGESTION" in the output.

# Execution

The script has been written in Python 3 (doesn't run on Python 2).

The cpellerror script creates error-words for 500 randomly selected words from words-5k file. It prints the original word (that has been modified) to STDERR, and the modified word to STDOUT.

The cpellsheck script checks the input-words for infinitely long sequence until "quit" is typed by the user. Can also accept inputs from the cpellerror script, and print the output.

This entire process has been automated in execute.sh. Just ./execute.sh with proper utilities installed.

## From execution:
    > sheeeeep
    sheep
    > peepple
    people
    > sheeple
    NO SUGGESTION
    > inSIDE
    inside
    > jjoobbb
    job
    > weke
    wake
    > CUNsperrICY
    conspiracy

Here's a list of the 500 randomly selected error-words put as input to the spellcheck script:

| No  | Generated     | Error         | Corrected     |
|-----|---------------|---------------|---------------|
| 1   | past          | PoaSSt        | post          |
| 2   | anticipate  | eNticiepAAti  | anticipate  |
| 3   | heavy | Heaavvy | heavy |
| 4   | magnitude | MagnitudEEE | magnitude |
| 5   | neighbor  | nnEiGhberr  | neighbor  |
| 6   | hypothesis  | hyppOtHesiss  | hypothesis  |
| 7   | population  | ppopulloTioN  | population  |
| 8   | Mrs | MRRRs | NO  |
| 9   | skilled | sskIlLedd | skilled |
| 10  | familiar  | famIIILiur  | familiar  |
| 11  | pond  | ppOnnd  | pound |
| 12  | coal  | CioAAl  | cool  |
| 13  | pine  | pIInEE  | piano |
| 14  | wheelchair  | whEelchhhAir  | wheelchair  |
| 15  | mirror  | mIrrrrOr  | mirror  |
| 16  | icon  | IICien  | icon  |
| 17  | middle  | miodDDle  | middle  |
| 18  | equip | EEquIIp | equip |
| 19  | municipal | maneCIppell | municipal |
| 20  | convenience | caonveonIeNce | convenience |
| 21  | relief  | relliiEF  | relief  |
| 22  | past  | PAAAst  | post  |
| 23  | comment | cimmmEENt | comment |
| 24  | artificial  | artttIfecIel  | artificial  |
| 25  | spectrum  | sspEcttRum  | spectrum  |
| 26  | glad  | gggLAd  | glad  |
| 27  | rational  | raTTiannel  | rational  |
| 28  | bonus | BBeones | bonus |
| 29  | close | cllissE | close |
| 30  | disagree  | doisoGGreE  | disagree  |
| 31  | left  | LiufTT  | lift  |
| 32  | backyard  | baaacKyoRd  | backyard  |
| 33  | headline  | HHeAddline  | headline  |
| 34  | intellectual  | inTTaLllectuel  | intellectual  |
| 35  | concentrate | CancuntrAAAte | concentrate |
| 36  | correlation | correLeTTTian | correlation |
| 37  | bowl  | bOWWWl  | bowl  |
| 38  | impressive  | iMprEEssivve  | impressive  |
| 39  | new | nEEWW | now |
| 40  | known | knewNNN | known |
| 41  | somewhat  | SoMuwhhitt  | somewhat  |
| 42  | gray  | gRaeyy  | gray  |
| 43  | act | AcTTT | act |
| 44  | chapter | ChheupTer | chapter |
| 45  | Muslim  | MMUUsloM  | NO  |
| 46  | project | prroJaiCt | project |
| 47  | establish | usttablIIsH | establish |
| 48  | tender  | ttEENdir  | tender  |
| 49  | bull  | BUUlll  | boil  |
| 50  | interfere | InntteRferu | interfere |
| 51  | garden  | gauuRdaN  | garden  |
| 52  | abstract  | ibstRacTTT  | abstract  |
| 53  | catch | CCutccH | catch |
| 54  | change  | cchiNGio  | change  |
| 55  | gradually | ggRaduAAlly | gradually |
| 56  | heat  | HeAttt  | heat  |
| 57  | frankly | frAnnkkLy | frankly |
| 58  | compromise  | compruaMMise  | compromise  |
| 59  | slice | SSSlIci | slice |
| 60  | republic  | rEEpuBlluc  | republic  |
| 61  | homework  | hOmmmewoRk  | homework  |
| 62  | carbohydrate  | CurrrbohydriTi  | carbohydrate  |
| 63  | landscape | llandScaPee | landscape |
| 64  | forever | foiRRevEr | forever |
| 65  | employ  | oMPlllay  | employ  |
| 66  | plus  | ppllUs  | plus  |
| 67  | type  | TTyypa  | type  |
| 68  | economist | EconouomiSt | economist |
| 69  | choice  | cHOiicci  | choice  |
| 70  | booth | bboOthh | booth |
| 71  | clerk | cccLorK | clerk |
| 72  | peanut  | PeeAnutt  | peanut  |
| 73  | prior | pRReiaR | prior |
| 74  | genetic | guenutIIC | genetic |
| 75  | historically  | hIIStericollly  | historically  |
| 76  | remarkable  | RemarkkobllE  | remarkable  |
| 77  | drag  | DrraGG  | drag  |
| 78  | lower | liWEErr | lower |
| 79  | rip | RIIpp | rip |
| 80  | response  | reesppinsE  | response  |
| 81  | herself | HerSSulff | herself |
| 82  | peace | pEEaCue | pace  |
| 83  | division  | doVViiSion  | division  |
| 84  | downtown  | downTToowN  | downtown  |
| 85  | resemble  | rresaeMBlu  | resemble  |
| 86  | diet  | DiEEtt  | dot |
| 87  | prefer  | pprEEfEr  | prefer  |
| 88  | assure  | AAssurEE  | assure  |
| 89  | claim | cLLiImm | claim |
| 90  | refugee | rEfuggEee | refuge  |
| 91  | sentiment | senntiimEnT | sentiment |
| 92  | cell  | cciLLL  | cool  |
| 93  | face  | fACCee  | face  |
| 94  | deserve | dEsEErrve | deserve |
| 95  | o'clock | O''clloCk | o'clock |
| 96  | passenger | pAssennggEr | passenger |
| 97  | shade | shhhAdE | shade |
| 98  | organize  | orrgAnIzzi  | organize  |
| 99  | piano | Pioanoo | piano |
| 100 | hidden  | HiiddEEn  | hidden  |
| 101 | fail  | FuiIll  | fool  |
| 102 | walk  | WaaLkk  | walk  |
| 103 | old | Olldd | old |
| 104 | writer  | wrIteerr  | writer  |
| 105 | net | NEEtt | neat  |
| 106 | campus  | ccimmpUs  | campus  |
| 107 | permit  | PermIItt  | permit  |
| 108 | that  | ThAAtt  | that  |
| 109 | prove | ppproVe | prove |
| 110 | shuttle | shueTTleo | shuttle |
| 111 | correctly | CCOrrectlly | correctly |
| 112 | dig | dddIg | dig |
| 113 | run | RRuiN | rain  |
| 114 | broad | BrroAAd | bread |
| 115 | really  | ruiealLY  | rally |
| 116 | explode | ExxxpliDa | explode |
| 117 | almost  | AAAlMost  | almost  |
| 118 | plant | pllAnTT | plant |
| 119 | along | AluNNgg | along |
| 120 | oil | ooIIL | ill |
| 121 | stance  | SttoNNce  | stance  |
| 122 | incredibly  | incRRedIblyy  | incredibly  |
| 123 | Muslim  | MMUsliMM  | NO  |
| 124 | dance | DDAncia | dance |
| 125 | admire  | AdmiarEE  | admire  |
| 126 | bright  | BrrugHtt  | bright  |
| 127 | cabinet | cibbInEEt | cabinet |
| 128 | isolation | IsollitooNN | isolation |
| 129 | league  | leAgggue  | league  |
| 130 | angel | AnngaeL | angel |
| 131 | unite | unniiTe | unite |
| 132 | straight  | stRRRaight  | straight  |
| 133 | regain  | reGaaaIn  | regain  |
| 134 | phone | pHHonne | phone |
| 135 | load  | lOiedd  | lid |
| 136 | point | PooIInt | pant  |
| 137 | frustration | frasTratuaioN | frustration |
| 138 | harvest | hurvvEEsT | harvest |
| 139 | fun | ffUnn | fun |
| 140 | football  | fiioTbiLll  | football  |
| 141 | fire  | FIrroe  | fare  |
| 142 | mostly  | MOOstlly  | mostly  |
| 143 | budget  | BudgEEtt  | budget  |
| 144 | shut  | sHHHut  | shit  |
| 145 | annual  | annUUUaL  | annual  |
| 146 | mysterious  | mysturriouSS  | mysterious  |
| 147 | trail | tRRuual | trail |
| 148 | agent | agaeNTT | agent |
| 149 | workshop  | wOrkkshhOp  | workshop  |
| 150 | call  | CCCelL  | cool  |
| 151 | mouth | mOOutHH | math  |
| 152 | champion  | chAmpuoooN  | champion  |
| 153 | departure | DEpartteree | departure |
| 154 | purse | PPiirsE | purse |
| 155 | o'clock | o''cclock | o'clock |
| 156 | resolution  | rEEsoluiToan  | resolution  |
| 157 | expect  | EExPeict  | expect  |
| 158 | immediate | ImmEEdaotee | immediate |
| 159 | uncertainty | uncceRTaintyy | uncertainty |
| 160 | least | laAAssT | last  |
| 161 | condemn | condEmmNN | condemn |
| 162 | distinguish | diostenguIsHH | distinguish |
| 163 | dawn  | dAwNNN  | dawn  |
| 164 | discipline  | desscIplluno  | discipline  |
| 165 | file  | fffILu  | file  |
| 166 | stage | sTTTaGa | stage |
| 167 | habitat | HaBittaet | habitat |
| 168 | retreat | rrEETroat | retreat |
| 169 | proportion  | PropurrteiOn  | proportion  |
| 170 | dissolve  | disSilllvo  | dissolve  |
| 171 | light | lIIIGht | light |
| 172 | horizon | hOrrIzann | horizon |
| 173 | severely  | suevviRulY  | severely  |
| 174 | statue  | STaoetee  | statue  |
| 175 | request | ReqaeSStt | request |
| 176 | custody | cUStieody | custody |
| 177 | smile | ssmmILu | smile |
| 178 | uncover | uunncoveR | uncover |
| 179 | weekend | wEeKKindd | weekend |
| 180 | corporation | corPorAttoian | corporation |
| 181 | annual  | annNiAAl  | annual  |
| 182 | possibly  | ppossIbbLy  | possibly  |
| 183 | day | dAYYY | day |
| 184 | swim  | ssWWoM  | swim  |
| 185 | commitment  | commiiTmeNNt  | commitment  |
| 186 | possibly  | pOsSibbbly  | possibly  |
| 187 | civic | CCivIIc | civic |
| 188 | endure  | eNduRRRe  | endure  |
| 189 | than  | tHHuaN  | thin  |
| 190 | isolation | issoLatioNN | isolation |
| 191 | permission  | peeRmmussiOn  | permission  |
| 192 | departure | deoparrtuRE | departure |
| 193 | derive  | deroiavE  | derive  |
| 194 | gold  | GGGold  | gold  |
| 195 | foster  | fOOStter  | faster  |
| 196 | admission | addMasssIen | admission |
| 197 | fully | FuulllY | fully |
| 198 | closest | ccclisEst | closest |
| 199 | identify  | idoNtifffY  | identify  |
| 200 | presence  | Prissoenco  | presence  |
| 201 | cottage | CCitTagge | cottage |
| 202 | super | sUPPirr | super |
| 203 | switch  | swwItccH  | switch  |
| 204 | long  | LLaNNg  | lung  |
| 205 | assemble  | asSSEmblle  | assemble  |
| 206 | illness | IlLLLness | illness |
| 207 | employee  | ueMpllaYea  | employee  |
| 208 | library | llibrrArY | library |
| 209 | rubber  | rrrUBber  | rubber  |
| 210 | eager | eoaigaR | eager |
| 211 | recession | rucesssiOON | recession |
| 212 | baby  | bAAByy  | baby  |
| 213 | those | tHHiosE | those |
| 214 | resident  | resuidEEnT  | resident  |
| 215 | supervisor  | ssUpirviisoR  | supervisor  |
| 216 | seldom  | ssalddOm  | seldom  |
| 217 | motivate  | motooivatE  | motivate  |
| 218 | terror  | teerROrr  | terror  |
| 219 | sufficient  | SufffeciEnnt  | sufficient  |
| 220 | increased | uncrrEEesEd | increased |
| 221 | except  | ExxxCept  | except  |
| 222 | kit | Koiut | kit |
| 223 | key | kkkEY | key |
| 224 | their | ThuoiiR | their |
| 225 | gross | gRRooSs | gross |
| 226 | two | tWWui | two |
| 227 | bloody  | bbbloOdY  | bloody  |
| 228 | investigation | invviostigaTuun | investigation |
| 229 | service | siervicEE | service |
| 230 | transformation  | transFarrrmaTion  | transformation  |
| 231 | dark  | dddArK  | dark  |
| 232 | shop  | shiooP  | sheep |
| 233 | ceremony  | ceRemoaanY  | ceremony  |
| 234 | fair  | FFAiir  | fur |
| 235 | closest | cliiseStt | closest |
| 236 | and/or  | anndd/OR  | and/or  |
| 237 | half  | hhALLf  | half  |
| 238 | reference | rrefereeNcE | reference |
| 239 | before  | bbbEfiRe  | before  |
| 240 | for | FFoor | fur |
| 241 | double  | duUbbLee  | double  |
| 242 | nearby  | NEarrrby  | nearby  |
| 243 | local | leccaoL | local |
| 244 | sofa  | sooFAA  | sofa  |
| 245 | receive | reoccEivE | receive |
| 246 | owe | oioWE | owe |
| 247 | sail  | Saiell  | seal  |
| 248 | happily | hhApppIly | happily |
| 249 | assert  | oussserT  | assert  |
| 250 | beam  | bEAAAm  | beam  |
| 251 | frequent  | frEquuuNNt  | frequent  |
| 252 | real  | RRRuAl  | rail  |
| 253 | firm  | FiRRmm  | firm  |
| 254 | ankle | AnnnKla | ankle |
| 255 | gravity | gRaVVitty | gravity |
| 256 | culture | cilttUUrE | culture |
| 257 | Arab  | AArAbb  | NO  |
| 258 | conclusion  | conccloSIoin  | conclusion  |
| 259 | near  | NeeaRR  | near  |
| 260 | dining  | diNiNNgg  | dining  |
| 261 | water | wAAteRR | water |
| 262 | reliability | rilieabalITyy | reliability |
| 263 | vary  | vvArry  | vary  |
| 264 | index | innDExx | index |
| 265 | home  | hOOOmE  | home  |
| 266 | police  | poLLeuCi  | palace  |
| 267 | European  | EEurrupaAN  | NO  |
| 268 | mirror  | mIIrrorr  | mirror  |
| 269 | event | Evvontt | event |
| 270 | killing | kilLLLIng | killing |
| 271 | sunny | ssUUNny | sunny |
| 272 | inquiry | onqUUUiry | inquiry |
| 273 | mass  | mmASSs  | mess  |
| 274 | nice  | naCCCi  | nice  |
| 275 | return  | REturnnn  | return  |
| 276 | safety  | ssafuatY  | safety  |
| 277 | nervous | nneerVOus | nervous |
| 278 | running | rUnniNNgg | running |
| 279 | low | lOOww | low |
| 280 | o'clock | o'cLoockk | o'clock |
| 281 | iron  | IIrOnn  | iron  |
| 282 | tuck  | tUUUcK  | tuck  |
| 283 | dancing | ddanCeNNg | dancing |
| 284 | climate | claMAttto | climate |
| 285 | toll  | TTOlll  | till  |
| 286 | fitness | fItnnessS | fitness |
| 287 | chief | chIIeFF | chef  |
| 288 | preparation | preppArettooN | preparation |
| 289 | intelligence  | enntoLliGincuu  | intelligence  |
| 290 | integration | IINtegrateann | integration |
| 291 | wish  | WIIshh  | wish  |
| 292 | kind  | kIInnd  | kind  |
| 293 | toward  | tOOwaard  | toward  |
| 294 | secret  | siCrrrat  | secret  |
| 295 | command | CoMmaundd | command |
| 296 | department  | dEpppurtmEnt  | department  |
| 297 | root  | rrouOT  | riot  |
| 298 | bad | bAAdd | bid |
| 299 | bacteria  | baeacterIa  | bacteria  |
| 300 | bank  | BBaink  | bank  |
| 301 | here  | HEErra  | hero  |
| 302 | magic | MagiiuC | magic |
| 303 | red | RRaeD | rod |
| 304 | buy | bbUYY | bay |
| 305 | full-time | fiuLl-TTeme | full-time |
| 306 | found | FOuondd | fund  |
| 307 | brave | bbrrevE | brave |
| 308 | rise  | riSEEE  | rose  |
| 309 | paint | ppiIInt | pant  |
| 310 | else  | EELLsa  | else  |
| 311 | peanut  | PeoaoneT  | peanut  |
| 312 | timber  | tiiMBoar  | timber  |
| 313 | outside | uUUTsodao | outside |
| 314 | fight | fiiGhTT | fight |
| 315 | seminar | SSumInnar | seminar |
| 316 | anyone  | AnyyoNNe  | anyone  |
| 317 | sum | sUUUM | sum |
| 318 | thanks  | ThhaankS  | thanks  |
| 319 | tray  | tRReYY  | tray  |
| 320 | declare | ddicLAAre | declare |
| 321 | publicity | paoblaccItY | publicity |
| 322 | leading | lEAddding | leading |
| 323 | college | ccOlllegE | colleague |
| 324 | chemistry | cHHHumistRy | chemistry |
| 325 | developing  | ddEveLopiung  | developing  |
| 326 | account | occcOuuNt | accent  |
| 327 | violent | vioelEnnT | violent |
| 328 | stair | STTairr | steer |
| 329 | illustrate  | illussTrAAte  | illustrate  |
| 330 | separation  | seppirrutIoN  | separation  |
| 331 | all | AAllL | ill |
| 332 | favor | ffAAver | fever |
| 333 | part  | pAArrt  | part  |
| 334 | plane | pLLAnno | plane |
| 335 | prospect  | proSppucct  | prospect  |
| 336 | business  | buisiNNuSs  | business  |
| 337 | intend  | innTEndd  | intend  |
| 338 | tomorrow  | ttOMarroww  | tomorrow  |
| 339 | million | mmoellIOn | million |
| 340 | hidden  | heDDdEnn  | hidden  |
| 341 | density | dEnnsiity | density |
| 342 | gasoline  | guasoliNNE  | gasoline  |
| 343 | contribute  | ContriibbitE  | contribute  |
| 344 | traditional | TRodiotionnal | traditional |
| 345 | locate  | LOOccute  | locate  |
| 346 | gray  | Gruiyy  | gray  |
| 347 | another | aNeotheuR | another |
| 348 | incredibly  | oncrEEdoiblY  | incredibly  |
| 349 | arrangement | arRAAnggament | arrangement |
| 350 | jail  | JJJail  | jail  |
| 351 | shell | SHHelll | shell |
| 352 | functional  | funcctIOnial  | functional  |
| 353 | sake  | saeaKE  | sake  |
| 354 | pack  | PPPecK  | pack  |
| 355 | wash  | WaaSSh  | wish  |
| 356 | technique | ttachniqUUe | technique |
| 357 | us  | USSS  | ass |
| 358 | butt  | buuTTT  | butt  |
| 359 | eager | eAAggiR | eager |
| 360 | team  | TTTeaM  | team  |
| 361 | adviser | edVViseRR | adviser |
| 362 | example | oXimplEEE | example |
| 363 | overlook  | aoveeRlaoK  | overlook  |
| 364 | impossible  | ImpessssoblE  | impossible  |
| 365 | substantially | soBstAAntiallly | substantially |
| 366 | thus  | tHHuSS  | this  |
| 367 | script  | scroipTT  | script  |
| 368 | rain  | RuaiNN  | rain  |
| 369 | tell  | TeoeLl  | till  |
| 370 | banker  | bANNkerr  | banker  |
| 371 | approximately | ipprroxiumAtalY | approximately |
| 372 | toe | TToai | toe |
| 373 | narrow  | nuarrrOW  | narrow  |
| 374 | desperately | DEEEsperately | desperately |
| 375 | write | WrreiTe | write |
| 376 | object  | ouBjEEct  | object  |
| 377 | distinguish | diStttungaosh | distinguish |
| 378 | fragment  | ffragMeeNt  | fragment  |
| 379 | politically | pOlitecalllLy | politically |
| 380 | empire  | eeMpiiRe  | empire  |
| 381 | terrorist | TearrorIIst | terrorist |
| 382 | safety  | saaFFety  | safety  |
| 383 | obstacle  | obssttACle  | obstacle  |
| 384 | segment | sugmeNttt | segment |
| 385 | coach | cOOaacH | couch |
| 386 | socially  | socIIAllly  | socially  |
| 387 | lovely  | llavaeLY  | lovely  |
| 388 | suit  | SSSeiT  | seat  |
| 389 | quick | quIIckk | quick |
| 390 | stomach | stttOmAch | stomach |
| 391 | within  | WWethInn  | within  |
| 392 | softly  | ssoofTLy  | softly  |
| 393 | persuade  | pERRsuadda  | persuade  |
| 394 | pretty  | ppReTtty  | pretty  |
| 395 | Republican  | REpubbLicuan  | republican  |
| 396 | muscle  | MussclEE  | muscle  |
| 397 | health-care | heialthh-Coru | health-care |
| 398 | will  | wIIIlL  | will  |
| 399 | obtain  | OBttaain  | obtain  |
| 400 | generation  | generaTiooNN  | generation  |
| 401 | mandate | maunnDAta | mandate |
| 402 | terrain | teeerReIn | terrain |
| 403 | qualify | qoAlliFFy | qualify |
| 404 | shrink  | sshriNkk  | shrink  |
| 405 | lot | LLott | lot |
| 406 | fruit | FRRReit | fruit |
| 407 | doubt | DouuBtt | doubt |
| 408 | inevitably  | InnevvituBly  | inevitably  |
| 409 | journal | JuurnAAAl | journal |
| 410 | tree  | tRREEo  | tree  |
| 411 | era | EERae | era |
| 412 | spell | sPPeiLl | spell |
| 413 | mushroom  | moshRiuouM  | mushroom  |
| 414 | German  | GurmmaoN  | NO  |
| 415 | stupid  | stueupID  | stupid  |
| 416 | sustain | saasTTian | sustain |
| 417 | transmission  | TrransmiSssien  | transmission  |
| 418 | cue | CCCUu | cue |
| 419 | meaning | mEEaNinng | meaning |
| 420 | expectation | oeXpectuTTaon | expectation |
| 421 | personally  | PersoNallyyy  | personally  |
| 422 | personality | ppersOnelItty | personality |
| 423 | sole  | sOLLLe  | sole  |
| 424 | experience  | ExppEruencoo  | experience  |
| 425 | pain  | paaaIN  | pin |
| 426 | including | inclUdonnng | including |
| 427 | available | iVaIlobllle | available |
| 428 | temple  | tompLaee  | temple  |
| 429 | ourselves | OirsalvvveS | ourselves |
| 430 | teammate  | teemmmATie  | teammate  |
| 431 | powder  | PPiwdEEr  | powder  |
| 432 | two-thirds  | tWe--thurdSS  | two-thirds  |
| 433 | surveillance  | survailllAnncE  | surveillance  |
| 434 | indicator | iNdicAAtorr | indicator |
| 435 | steady  | SStieadY  | steady  |
| 436 | bias  | bbIIaS  | bias  |
| 437 | addition  | edDDitieon  | addition  |
| 438 | revolutionary | RRReviluTieniry | revolutionary |
| 439 | gentle  | GantttLo  | gentle  |
| 440 | path  | PeThhh  | path  |
| 441 | yes | yyESS | yes |
| 442 | less  | leeeSS  | loss  |
| 443 | vote  | VVOtue  | vote  |
| 444 | silk  | SiaLkk  | silk  |
| 445 | almost  | aLLmaost  | almost  |
| 446 | throat  | thrreAAt  | throat  |
| 447 | later | LaaateR | latter  |
| 448 | aim | eImmm | aim |
| 449 | servant | seRVaaant | servant |
| 450 | handful | HanddffUl | handful |
| 451 | system  | SysstEEm  | system  |
| 452 | kitchen | KKitchEEn | kitchen |
| 453 | initial | inIItioAl | initial |
| 454 | much  | MMMecH  | much  |
| 455 | nation  | naTTioNN  | notion  |
| 456 | satisfy | SutIssffy | satisfy |
| 457 | document  | doocemEnnT  | document  |
| 458 | attention | aaTtenTiion | attention |
| 459 | vendor  | veendaRR  | vendor  |
| 460 | sweep | sWoEEpp | sweep |
| 461 | sue | SouEE | sue |
| 462 | per | PPorr | peer  |
| 463 | visible | vIsubllEE | visible |
| 464 | loop  | lOooop  | loop  |
| 465 | recall  | recAAALl  | racial  |
| 466 | present | PPraseent | present |
| 467 | use | oSSEE | ease  |
| 468 | flower  | flOwwErr  | flower  |
| 469 | evidence  | eeaVadencE  | evidence  |
| 470 | if  | iFFF  | off |
| 471 | Russian | RUssssiAn | reason  |
| 472 | entire  | iuNtIrre  | entire  |
| 473 | player  | pplliYEr  | player  |
| 474 | behave  | bbeehavE  | behave  |
| 475 | signal  | ssaggNAl  | signal  |
| 476 | solve | sOOllVa | solve |
| 477 | envelope  | eiNveloPee  | envelope  |
| 478 | century | ceNTurryy | century |
| 479 | medium  | mmEdiaMM  | medium  |
| 480 | curtain | cuRtoaaiN | cartoon |
| 481 | transaction | TTrranSactoon | transaction |
| 482 | challenge | cHillEEnngi | challenge |
| 483 | experience  | eXpaRReaence  | experience  |
| 484 | clinic  | ClIniccc  | clinic  |
| 485 | initial | unaittIaL | initial |
| 486 | urban | urrBBiN | urban |
| 487 | genius  | gEnnIIos  | genius  |
| 488 | anything  | eenyThengg  | anything  |
| 489 | roll  | ROllll  | rail  |
| 490 | criminal  | cRimmiNiil  | criminal  |
| 491 | resistance  | rosisttancEE  | resistance  |
| 492 | evil  | EEEVil  | evil  |
| 493 | philosophy  | philooSaPPhy  | philosophy  |
| 494 | fade  | FaddEE  | fade  |
| 495 | steam | sttteAm | steam |
| 496 | bathroom  | bathROOOem  | bathroom  |
| 497 | be  | Booo  | bee |
| 498 | bother  | botheeRR  | bother  |
| 499 | yours | YYeeoRs | yours |
| 500 | previously  | prEEVioaisly  | previously  |

```
False corrections:  76
No suggestions:  6
```