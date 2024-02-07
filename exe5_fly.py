""" 
British Airplanes Startup:
A British start-up specializing in the manufacturing of high-security, 
high-speed aircraft seeks to calculate the prices of its planes based on
the following characteristics: Aircraft size, VIP seats, economy class seats,
material quality, security system, and speed level.
Currently, it offers 3 types of aircraft ready for sale.

Wayne Rooney Plane:
    Quality AAA
    200 economy class seats
    70 VIP seats
    90 square meters
    Security system AAA
    Speed level AAA
Eric Cantona Plane:
    Quality AAA
    150 economy class seats
    80 VIP seats
    110 square meters
    Security system AAA
    Speed level AA
Bobby Charlton Plane:
    Quality AA
    100 economy class seats
    40 VIP seats
    120 square meters
    Security system AA
    Speed level A
"""

class Plane:
    def __init__(self, type, quality, security, speed, eco_num, vip_num):
        seat_dic = {'wayne': [400, 1200], 'eric': [400, 1200], 'bobby': [300, 1000]}
        
        self.type = type
        self.quality = quality
        self.security = security
        self.speed = speed
        
        self.economy = eco_num * seat_dic[type][0]
        self.vip = vip_num * seat_dic[type][1]   
    def calculate(self):
        quality_dic = {'AAA': 60000, 'AA': 54000, 'A': 48000}
        security_dic = {'AAA': 750000, 'AA': 68000, 'A': 59000}
        speed_dic = {'AAA': 89000, 'AA': 78000, 'A': 70000}
        price = quality_dic[self.quality] + security_dic[self.security] + speed_dic[self.speed] + self.economy + self.vip
        print(price)
        
        
wayne = Plane('wayne', 'AAA', 'AAA', 'AAA', 200, 70)
print(wayne.type)
wayne.calculate()
eric = Plane('eric', 'AAA', 'AAA', 'AA', 150, 80)
print(eric.type)
eric.calculate()
bobby = Plane('bobby', 'AA', 'AA', 'A', 100, 40)
print(bobby.type)
bobby.calculate()
        
