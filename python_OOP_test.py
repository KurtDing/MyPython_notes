'''hls
包含物件的建立、三種方法、三種屬性、專有名詞、小遊戲demo
不包含抽象方法(Abstract Method)、多型(Polymorphism)、繼承(Inheritance)相關內容

關於類別裡的屬性/方法的命名
"_"     約定該方法或者屬性是私有方法/屬性, 不應該被直接呼叫。
        但實際上是可以直接呼叫。用import導入模組時有作用, 會不被載入
"__"    也是代表私有, 只允許從self訪問, 實務上用來避免子類重寫某個方法
"__ xx __"  魔術方法(magic methods), 一般是系統定義給python呼叫的名字
'''

import random

#建立類別(class, 物件objct的藍圖),通常使用Pascal命名法，字首大寫&不使用空白或底線分隔
class Character:        #沒有繼承其他類別,在python3會自動幫你在className後加(object)
    #類別屬性(Class Attribute)，定義在建構式之外，可透過類別名稱存取，影響從該類別建立的全部物件
    #但是如果實例裡有同名的實體屬性(Instance Attribute)會優先用實體屬性
    atk_action_list = ['smash', 'hack', 'stab', 'blow', 'kick', 'shoot']
    # 建構式(Constructor)，設定建立物件(Object)時要傳入的屬性
    # self代表實體物件的參考，也就是目前的物件
    def __init__(self, name, hp, atk, defense, evade):
        #實體屬性(Instance Attribute)，可以從建構式傳入，各物件獨立，透過物件名稱修改
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense
        self.evade = evade        

    #屬性(Property)，封裝的實現方式
    ''' 通常, 設定atk(從建構式或外部設定)的動作就是直接把值傳進(Attribute)
        就是"self.atk = atk"或是"物件名.atk = xx", 讀取值用"物件名.atk"
        在某些應用場景我們需要把Attribute改成Property, 像是檢查設定的數值
        如底下的程式碼
        再建立一個atk實體方法然後上一行加上@property, self.atk會變成property
        Property是唯讀不可被設定的
        另外還要設定一個setter的方法讓property可以被設定
        當來源(類或物件?)要設定self.atk時會變成呼叫setter裡的atk()這個方法處理值
        setter經過某些我們希望的運算後把結果值指向另一個Attribute self.__atk
        雙底線"__"在python代表不可以從外部存取或呼叫
        之後要讀取值時self.atk就會呼叫atk()取得self.__atk
    '''
    @property       #getter
    def atk(self):
        return self.__atk
    
    @atk.setter     #setter
    def atk(self, value):
        if value <= 0:
            raise ValueError('Atk should be more than zero.')
        self.__atk = value
        
    #實體方法(Instance Method)，只能透過物件(object)呼叫
    #即類裡面的函式(Function)，pythonic的命名通常用小寫字母，底線分隔
    #在實體方法(Instance Method)可以透過"self.__class__.屬性"來改變類別(Class)的狀態
    #像是類別屬性的值
    def attack(self, target):
        if self.dodge2(target):   # 呼叫其他方法
            print(f'{self.name} missed.')
            return
        atk_action = random.choice(Character.atk_action_list)   #讀取類別屬性
        dmg = int(self.atk * random.uniform(0.8, 1.1)) - target.defense
        #dmg = self.atk - target.defense
        if dmg > 0:
            target.hp -= dmg    #在VSC裡.hp是白色,代表目前不知道target裡有沒有hp這個屬性??
            print(f'{self.name} {atk_action} {target.name}, and deal {dmg} damage.')
        else:
            print(f'{target.name} parried this hit.')

    #其他實體方法(Instance Method)
    def dodge(self, target):
        return target.evade * random.random() >= 9.5

    #靜態方法(Static Method)
    #從類或物件呼叫，可以接受任意參數但不能改變self及cls狀態(即寫入)
    @staticmethod
    def dodge2(target):
        return target.evade * random.random() >= 9.5
    
    #類別方法(Class Method)，只能透過類呼叫
    @classmethod
    def boss(cls):
        return cls('bossEE', 50, 20, 20, 15)

#創建object (aka 實例,實體,物件, 某個class的instance)
#類裡面有建構式 def __init__(), 所以建立物件同時可以設定所有的屬性
#存取屬性格式是object_name.atkribute_name, 不用加(), 呼叫方法才要()
player = Character(name = 'chatHLS', hp = 30, atk = 25, defense = 15, evade = 12)
badguy = Character('JoeBlow', 60, 20, 20, 10)   #要不要加key都可以
boss01 = Character.boss()   #用類別方法建立物件, 邏輯已直接封裝在類別方法裡面
boss01.hp = 100  #重新設定屬性
Character.atk_action_list = ['smash', 'shoot']
enamy = badguy
print('>> START <<')
while player.hp > 0 and enamy.hp >0:
    player.attack(enamy)
    if enamy.hp <= 0 or player.hp <= 0:
        break                           # stop the battle
    enamy.attack(player)

print('U win :-)') if player.hp >= 0 else print('U die :-O')    # if else簡化敘述hls

#print(isinstance(boss01, Character)) #檢查enamy是不是Character的物件
#參考資料
#https://www.learncodewithmike.com/2020/01/python-method.html