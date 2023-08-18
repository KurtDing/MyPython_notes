'''OOP 實作 ==> 繼承, 覆蓋, 新增
需求 實作螺絲起子
功能 可以換頭, 指定頭尺寸, 依照情境來選擇
需求變更 也要可以指定長度
'''

class ScrewDriver:
    def __init__(self, head, size_num):
        self.head = head
        self.size_num = size_num
        self.labelcont = 'this is labelcont in 父類'
    def gen_driver(self):
        print(f'(父類方法)生成{self.size_num}號{self.head}的起子。')

class ScrewDriver1(ScrewDriver):
    #覆寫方法
    def gen_driver(self, handle_len):
        print(f'(子類1改寫)生成{self.size_num}號{self.head}的起子，長度{handle_len}公分。')
    def label(self):
        print('(子類1新增)標籤是貼紙囉')
        
class ScrewDriver2(ScrewDriver):
    #繼承並新增屬性
    def __init__(self, head, size_num, handle_len):
        super().__init__(head, size_num)    #繼承父類屬性但是要把生成數值丟進去
        self.handle_len = handle_len
        self.labelcont = 'this is labelcont in 子類2' #覆蓋父類屬性
    def gen_driver2(self):
        print(f'(子類2新增)生成{self.size_num}號{self.head}的起子，起子長度{self.handle_len}公分。')
    def label(self):
        print('(子類2新增)標籤是雷雕文字囉')
#多重繼承, 方法重複以左邊優先
class ScrewDriver3(ScrewDriver1, ScrewDriver2):
    pass


#程式執行測試

print('實作父類, 2屬性')
a = ScrewDriver('八角頭', 12)
a.gen_driver()
print('實作子類1')
b = ScrewDriver1('一字頭', 10)
b.gen_driver(20)
b.label()
print('實作子類2, 建構式新增一個屬性')
c = ScrewDriver2('十字頭', 14, 25)
c.gen_driver()
c.gen_driver2()
c.label()
print('實作孫類, 多重繼承')
d = ScrewDriver3('星型頭', 6, 20)
d.gen_driver(20)
d.gen_driver2()
d.label()
print(d.labelcont)
print(d.__dict__)
print(d.__dict__)
