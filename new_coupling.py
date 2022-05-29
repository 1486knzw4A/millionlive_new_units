
import random
import copy

#ユニットデータは知り合いから借りました
P02 = ["Legend Girls!!","haruka","shizuka","yuriko","serika","tomoka"]
P03 = ["PRETTY DREAMER","hibiki","mirai","anna","nao","fuka"]
P04 = ["Blue Symphony","chihaya","kotoha","megumi","shiho"]
P05 = ["Sentimental Venus","iori","rio","emily","mizuki"]
P06 = ["Marionetteは眠らない","miki","tsubasa","julia","reika"]
P07 = ["カワラナイモノ","azusa","noriko","sayoko","karen"]
P08 = ["Good-Sleep,Baby♡","yayoi","kana","iku","tamaki"]
P09 = ["Helloコンチェルト","ritsuko","arisa","minako","hinata"]
P10 = ["瞳の中のシリウス","takane","miya","matsuri","umi"]
P11 = ["Fu-Wa-Du-Wa","makoto","mami","elena","ayumu"]
P12 = ["ココロがかえる場所","yukiho","chizuru","roco","momoko"]
P13 = ["Bigバルーン◎","ami","konomi","subaru","akane"]#11

H01 = ["レジェンドデイズ","hibiki","yayoi", "iori","ritsuko","ami"]
H02 = ["乙女ストーム!", "mirai", "tsubasa", "yuriko", "anna", "mizuki"]
H03 = ["クレシェンドブルー", "shizuka", "serika", "shiho", "reika", "akane"]
H04 = ["エターナルハーモニー","chihaya","matsuri","emily","julia","fuka"]
H05 = ["リコッタ","haruka","arisa","momoko","noriko","nao"]
H06 = ["灼熱少女","kotoha","megumi","umi","miya","tamaki"]
H07 = ["BIRTH","makoto","azusa","yukiho","kana","ayumu"]
H08 = ["ミックスナッツ","konomi","mami","minako","hinata","iku"]
H09 = ["ミルキーウェイ","miki","sayoko","chizuru","tomoka","subaru"]
H10 = ["ARRIVE","karen","takane","rio","elena","roco"]#21

D02h = ["ハルカナミライ","haruka","mirai"]
D02s = ["成長Chu→LOVER!!","yuriko","anna"]
D02E = ["Eternal Spiral","yayoi","kana"]
D02e = ["エスケープ","julia","megumi"]
D02p = ["piece of cake","shiho","reika"]
D03a = ["アライブファクター","chihaya","shizuka"]
D03S = ["Smiling Crescent","miya","serika"]
D03P = ["Persona Voice","yukiho","chizuru"]
D03C = ["Cut.Cut.Cut.","mizuki","momoko"]
D03D = ["Decided","matsuri","konomi"]
D04s = ["深層マーメイド","hibiki","tsubasa"]
D04H = ["HELLO, YOUR ANGEL♪","tomoka","iku"]
D04M = ["Melody in scape","minako","sayoko"]
D04G = ["G♡F","ritsuko","karen"]
D04l = ["little trip around the world","iori","emily"]
D05y = ["夜に輝く星座のように","nao","arisa"]
D05f = ["fruity love","akane","roco"]
D05Y = ["Your HOME TOWN","ami","hinata"]
D05h = ["秘密のメモリーズ","takane","fuka"]
D05t = ["たしかな足跡","azusa","rio"]
D06U = ["Understand? Understand!","kotoha","umi"]
D06j = ["ジャングル☆パーティー","mami","tamaki"]
D06B = ["Beat the World!!!", "makoto","ayumu"]
D06E = ["Emergence Vibe","miki","elena"]
D06D = ["Dreamscape","subaru","noriko"]#46

TA01 = ["創造は始まりの風を連れて","yuriko","tomoka","arisa","serika","roco"]
TA02 = ["俠気乱舞","julia","momoko","hinata","noriko","tamaki"]
TA03 = ["赤い世界が消える頃","kana","mizuki","karen","minako","reika"]#49

F01Li = ["リブラ","tsubasa","minako","noriko"]
F01Le = ["レオ","iku","roco","elena"]
F01Cp = ["カプリコーン","kana","anna","rio"]
F01Cn = ["キャンサー","nao","hinata","emily"]
F02V = ["ウィルゴ","shizuka","yuriko","subaru"]
F02S = ["サジタリウス","megumi","mizuki","ayumu"]
F02P = ["ピスケス","chizuru","karen","tomoka"]
F02A = ["アクアリウス","julia","reika","sayoko"]
F03T = ["タウラス","mirai","miya","matsuri"]
F03A = ["アリエス","serika","akane","tamaki"]
F03J = ["ジェミニ","fuka","konomi","momoko"]
#F03S3 = ["スコーピオ(3)","umi","shiho","arisa"]
F03S4 = ["スコーピオ(4)","umi","shiho","arisa","kotoha"]#62

F01 = ["Sunshine Rhythm","tsubasa","minako","noriko","iku","roco","elena","kana","anna","rio","nao","hinata","emily","kaori"]
F02 = ["Bluemoon Harmony","shizuka","yuriko","subaru","megumi","mizuki","ayumu","chizuru","karen","tomoka","julia","reika","sayoko","tsumugi"]
F03 = ["Starlight Melody","mirai","miya","matsuri","serika","akane","tamaki","fuka","konomi","momoko","umi","shiho","arisa","kotoha"]
F01t = ["サンリズム・オーケストラ♪(ミリシタ)","kana","tsubasa","minako","elena","hinata"]
F02t = ["brave HARMONY(ミリシタ)","tomoka","reika","sayoko","ayumu","shizuka"]
F03t = ["Starry Melody(ミリシタ)","serika","mirai","kotoha","arisa","fuka"]#68

Pr = ["PRINCESS STARS","mirai","kana","kotoha","iku","yuriko","arisa","matsuri","emily","sayoko","umi","nao","minako","noriko"]
Fa = ["FAIRY STARS","shizuka","julia","chizuru","tomoka","megumi","rio","mizuki","tsumugi","shiho","roco","ayumu","momoko","subaru"]
An = ["ANGEL STARS","tsubasa","karen","akane","elena","miya","kaori","fuka","konomi","reika","hinata","serika","anna","tamaki"]
#71
G012u = ["マイティセーラーズ(2/海美)","umi","tsubasa"]
G012y = ["マイティセーラーズ(2/百合子)","yuriko","tsubasa"]
#G013 = ["マイティセーラーズ(3)","umi","tsubasa","yuriko"]
G02 = ["FairyTaleじゃいられない","shizuka","shiho","tsumugi","megumi","julia"]
G03 = ["Angelic Parade♪","tsubasa","kaori","anna","serika","reika"]
G04 = ["Princess Be Ambitious!!","mirai","matsuri","yuriko","kana","emily"]
G05 = ["夜想令嬢-GRAC&E NOCTURNE-","chizuru","tomoka","megumi","rio"]
G06 = ["Cleasky","elena","miya"]
G07 = ["トゥインクルリズム","iku","yuriko","arisa"]
G08 = ["EScape","mizuki","tsumugi","shiho"]
G09 = ["4Luxury","kaori","fuka","konomi","reika"]
G10 = ["閃光☆HANABI団","sayoko","umi","minako","nao","noriko"]
G12 = ["D/Zeal","julia","shizuka"]
G13 = ["りるきゃん～3 little candy～","karen","akane","tsubasa"]
G14 = ["Charlotte・Charlotte","matsuri","emily"]
G15 = ["Jelly PoP Beans","roco","ayumu","momoko","subaru"]
G16 = ["ピコピコプラネッツ","hinata","serika","anna","tamaki"]
G17 = ["STAR ELEMENTS","mirai","kana","kotoha"]#89

TB01 = ["ビッグバンズバリボー!!!!!","umi","megumi","sayoko","fuka","nao"]
TB02 = ["オーディナリィ・クローバー","kaori","shizuka","anna","rio","miya"]
TB03 = ["ラスト・アクトレス","kotoha","mizuki","momoko","konomi","tsumugi"]#92

W01J = ["ジェネシス×ネメシス","tsumugi","kaori","julia","makoto","akane"]
W01W = ["White Vows","fuka","rio","konomi","kaori","chizuru"]
W02 = ["Chrono-Lexica","yuriko","anna","mizuki","roco","subaru"]
W03 = ["Xs","yukiho","iori","miki","makoto"]
W04 = ["Sherry'n Cherry","konomi","rio"]
W05 = ["ARCANA","azusa","chihaya","takane"]
W06 = ["花咲夜","emily","tomoka","tsumugi"]
W07 = ["Jus-2-Mint","nao","minako"]
W08 = ["miraclesonic★expassion","ayumu","noriko","umi","elena"]
W09 = ["Fleuranges","hinata","serika","karen","miya"]
W10 = ["Do the IDOL!!～断崖絶壁チュパカブラ～","tomoka","yuriko","subaru","tsubasa","emily"]
W11 = ["オペラセリア・煌輝座","shiho","kaori","matsuri","kotoha"]
W12 = ["ダイヤモンドダイバー◇","yayoi","haruka","hibiki"]
W13 = ["TIntMe!","iku","momoko","tamaki"]
W14 = ["TRICK&TREAT","akane","reika"]
W15 = ["chicAAmor","sayoko","julia","chizuru","fuka"]
W16 = ["≡君彩≡","megumi","arisa","kana"]
W17 = ["ARMooo","ritsuko","ami","mami"]
W18 = ["ストロベリーポップムーン", "mirai", "shizuka", "tsubasa"]

S0 = ["EVERYDAY STARS!!(ミリシタ)","takane","mizuki","nao","kana","hinata"]
S11 = ["DIAMOND JOKER","tsubasa","matsuri","megumi","takane"]
S12 = ["真夏のダイヤ☆","rio","mami","yukiho","kotoha"]
S13 = ["シークレットジュエル～魅惑の金剛石～","iori","miya","mirai","kaori","momoko"]
S1 = ["BRIGHT DIAMOND","tsubasa","matsuri","megumi","takane","rio","mami","yukiho","kotoha","iori","miya","mirai","kaori","momoko"]
S21 = ["産声とクラブ","azusa","umi","serika","roco"]
S22 = ["トレフル・ド・ノエル","makoto","mizuki","elena","chizuru"]
S23 = ["Clover's Cry～神と神降ろしの少女～","nao","konomi","hinata","ritsuko","tamaki"]
S2 = ["CLEVER CLOVER","azusa","umi","serika","roco","makoto","mizuki","elena","chizuru","nao","konomi","hinata","ritsuko","tamaki"]
S31 = ["LOVE is GAME","tomoka","yayoi","minako","yuriko"]
S32 = ["紙・心・ペン・心-SHISHINPENSHIN-","noriko","arisa","chihaya","reika","sayoko"]
S33 = ["CHEER UP! HEARTS UP!","anna","kana","haruka","julia"]
S3 = ["LOVERS HEART","tomoka","yayoi","minako","yuriko","noriko","arisa","chihaya","reika","sayoko","anna","kana","haruka","julia"]
S4 = ["SHADE OF SPADE","iku","emily","shizuka","shiho","tsumugi","ayumu","karen","akane","subaru","fuka","miki","hibiki","ami"]


TC01 = ["Girl meets Wonder","serika","momoko","matsuri","hibiki","subaru"]
TC02 = ["World Changer","chihaya","miki","emily","makoto","haruka"]
TC03 = ["クルリウタ","akane","elena","shiho","chizuru","kaori"]

SMJ1 = ["カーテシーフラワー","umi","azusa","iku"]
SMJ2 = ["花びらメモリーズ","tsumugi","minako","momoko","megumi"]
SMJ3 = ["聖ミリオン女学園校歌","chihaya","subaru","karen"]

V11 = ["ワールド・アスレチック・COOK-KING～勝者必食!?スポ食の秋～","iku","hibiki","minako","karen","ayumu"]
V12 = ["ショコラブル＊イブ","megumi","mirai","anna","sayoko","akane"]

TD18C0 = ["メリー","haruka","chihaya","miki","makoto","yayoi"]
TD18C = ["メリー(デュオ)","kana","shiho"]
TD193 = ["プロジェクトフェアリー","miki","hibiki","takane"]
TD196 = ["トライスタービジョン","kotoha","megumi","elena"]
TD199 = ["きゅんっ!ヴァンパイアガール(ミリシタ)","iori","iku","momoko"]
TD19C = ["Little Match Girl(BNS)","yuriko","anna"]
TD203 = ["shiny smile(ミリシタ)","haruka","karen"]
TD206 = ["マイペースユニット","matsuri","tomoka","miya"]
TD209 = ["99 Nights(ミリシタ)","fuka","rio"]
TD20C = ["Little Match Girl(ミリシタ)","minako","mizuki"]
#TD2130 = ["サニー","yukiho","iori","azusa","ritsuko","ami","mami"]
TD213 = ["サニー(ミリシタ)","umi","tamaki"]
TD216 = ["edeN(ミリシタ)","reika","julia"]
TD2190 = ["聖炎の女神","takane","ritsuko"]
TD219 = ["聖炎の女神(ミリシタ)","makoto","hinata"]
TD21C = ["Miracle Night(ミリシタ)","chihaya","sayoko"]
TD223 = ["Honey HeartBeat(ミリシタ)","nao","akane"]
Futami = ["スタ→トスタ→","ami","mami"]

Radio =["ミリラジ", "mirai", "shizuka", "serika"]
SEL = ["Thank You!(LTSL)","yuriko","anna","shiho","konomi","emily"]

GS3 = ["アイル(Harmonized ver.)","tsubasa","julia","mizuki"]
#GS32 = ["my song(ゲッサン)","tsubasa","julia","mizuki"]
GS1 = ["GO MY WAY!!(ゲッサン)", "mirai", "shizuka"]
GS2 = ["ビジョナリー(ゲッサン)","serika","anna"]
GS4 = ["Vault That Borderline!(ゲッサン)","tsubasa","julia","mizuki","sayoko","yuriko"]
GS42 = ["Flooding","shizuka", "serika", "shiho", "reika", "akane"]
GS5 = ["私はアイドル♡(ゲッサン)","mizuki","megumi","miya","matsuri","momoko"]
GS52 = ["君との明日を願うから","mirai","shizuka","tsubasa"]

Clover = ["Clover","kana","shiho","umi","serika"]
BC21 = ["Do-Dai(BC)","serika","umi"]
BC31 = ["ONLY MY NOTE(BC)","haruka","kana","mirai"]
BC32 = ["MUSIC♪(BC)","kana","sayoko","kaori"]
BC33 = ["神SUMMER!!(BC)","nao","minako"]
BC41 = ["Dreaming!(BC)","umi","serika","kana"]
BC42 = ["i(BC)","serika","arisa"]
BC43 = ["チェリー(BC)","megumi","kotoha","elena"]
BC52 = ["キラメキラリ(BC)","akane","tsumugi"]
BC71 = ["Vertex Meister(BC)","umi","miya"]
BC72 = ["Just be myself!!(BC)","rio","kaori"]
BC81 = ["スタートリップ(BC)","julia","serika","chizuru"]
BC82 = ["聖炎の女神(BC)","megumi","tomoka"]
BC91 = ["アマテラス(BC)","hinata","emily"]
BC92 = ["カーテンコール(BC)","tomoka","rio"]
BCA1 = ["Happy!(BC)","kana","momoko","noriko"]
BCA2 = ["DIAMOND(BC)","iori","subaru"]
BCB1 = ["shy→shining(BC)","chihaya","shiho"]
BCB2 = ["my song(BC)","noriko","momoko","anna"]
BCC1 = ["MEGARE!(BC)","mizuki","fuka"]
BCC2 = ["キミがいて夢になる(BC)","kana","umi"]

IGNITE = ["IGNITE(ミリシタ)","mizuki","serika","tsubasa","julia","kotoha"]

unitlist0 = [P02,P03,P04,P05,P06,P07,P08,P09,P10,P11,P12,P13,H01,H02,H03,H04,H05,H06,H07,H08,H09,H10,
D02h,D02E,D02e,D02p,D02s,D03C,D03D,D03P,D03S,D03a,D04G,D04H,D04M,D04l,D04s,D05Y,D05f,D05h,D05t,D05y,D06B,D06D,D06E,D06U,D06j,
TA01,TA02,TA03,F01,F02,F03,F01Cn,F01Cp,F01Le,F01Li,F02A,F02P,F02S,F02V,F03A,F03J,F03T,F03S4,Pr,Fa,An,
G012u,G012y,G02,G03,G04,G05,G06,G07,G08,G09,G10,G12,G13,G14,G15,G16,G17,TB01,TB02,TB03,
W01J,W01W,W02,W03,W04,W05,W06,W07,W08,W09,W10,W11,W12,W13,W14,W15,W16,W17,W18,TC01,TC02,TC03,SMJ1,SMJ2,SMJ3,
S0,S1,S11,S12,S13,S2,S21,S22,S23,S3,S31,S32,S33,S4,V11,V12,
TD18C0,TD18C,TD193,TD196,TD199,TD19C,TD203,TD206,TD209,TD20C,TD213,TD216,TD219,TD2190,TD21C,TD223,Futami,Radio,SEL,GS3,GS1,GS2,GS4,GS5,
GS42,GS52,Clover,BC21,BC31,BC32,BC33,BC41,BC42,BC43,BC52,BC71,BC72,BC81,BC82,BC91,BC92,BCA1,BCA2,BCB1,BCB2,IGNITE]

namelistE = ["mirai","kana","kotoha","iku","yuriko","arisa","matsuri","emily","sayoko","umi","nao","minako","noriko",
"shizuka","julia","chizuru","tomoka","megumi","rio","mizuki","tsumugi","shiho","roco","ayumu","momoko","subaru",
"tsubasa","karen","akane","elena","miya","kaori","fuka","konomi","reika","hinata","serika","anna","tamaki",
"haruka","chihaya","miki","yukiho","iori","yayoi","makoto","azusa","takane","hibiki","ami","mami","ritsuko",""]

namelistJ = ["春日未来","矢吹可奈","田中琴葉","中谷育","七尾百合子","松田亜利沙","徳川まつり","エミリー","高山紗代子","高坂海美","横山奈緒","佐竹美奈子","福田のり子",
"最上静香","ジュリア","二階堂千鶴","天空橋朋花","所恵美","百瀬莉緒","真壁瑞希","白石紬","北沢志保","ロコ","舞浜歩","周防桃子","永吉昴",
"伊吹翼","篠宮可憐","野々原茜","島原エレナ","宮尾美也","桜守歌織","豊川風花","馬場このみ","北上麗花","木下ひなた","箱崎星梨花","望月杏奈","大神環",
"天海春香","如月千早","星井美希","萩原雪歩","水瀬伊織","高槻やよい","菊地真","三浦あずさ","四条貴音","我那覇響","双海亜美","双海真美","秋月律子",""]

idoldict = {}
for i in range(52):
    idoldict[namelistE[i]]=i

wlist=[[0 for j in range(52)] for i in range(52)]

lw=[0,0,100,60,30,15,5,1,1,1,1,1,1,2] #2人ユニット=重み100,3人ユニット=重み50,...

for u in unitlist0:
    ninzu=len(u)-1
    nl=[idoldict[i] for i in u[1:]]
    for i in nl:
        for j in nl:
            if i!=j:
                wlist[i][j]+=lw[ninzu]

print(wlist)

ulimit=[0,2,4,6,9,12,15,18,22,26,30,34,39]
nw=[0,0,10,5,2,1] #2人ユニットを新規に組む=ペナルティ10倍,3人を組む=ペナルティ5倍,...

ans=[]
answ=100000000000


il=[i for i in range(39)]
for k in range(10000000):
    if k%100000==0:
        print("turn",k,answ)
    random.shuffle(il)

    noww=0
    for f in range(12):
        u1=ulimit[f]
        u2=ulimit[f+1]
        un=u2-u1
        for i in range(u1,u2):
            for j in range(i+1,u2):
                if i!=j:
                    noww+=wlist[il[i]][il[j]]*nw[un]
    #print(noww)
    
    if noww<answ:
        answ=noww
        ans=copy.copy(il)

for f in range(12):
    for i in range(ulimit[f],ulimit[f+1]):
        print(namelistJ[ans[i]]+" ",end="")
    print("")
print(answ)




