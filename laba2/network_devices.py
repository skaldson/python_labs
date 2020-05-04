# contain enums for WAN/LAN and tuples for classes from `peripheral` module
import enum

# FAX
fax_type = ('monofunctional', 'multifunctional')
fax_kind = ('colored', 'monochrome')

# PRINTER
printer_type = ('laser', 'LED', 'solid ink', 'liquid injekt', 'toner-based')

# COMPUTER
computer_processor = ('i3', 'i5', 'i7', 'radeon', 'potato')
computer_type = ('desktop', 'laptop', 'notebook')


#CONNECTION TECHNOLOGY
class WanConnection(enum.Enum):
    cable = 'Cable modem'
    dial_up = 'Dial-up internet'
    x_25 = 'X.25'
    isdn = 'ISDN'
    sd_wan = 'SD-WAN'
    frame_relay = 'Frame Relay'
    wanConn_list = [cable, dial_up, x_25, isdn, sd_wan, frame_relay]


class LanConnection(enum.Enum):
    ethernet = 'Ethernet'
    token = 'Token'
    wireless = 'Wireless'
    lanConn_list = [ethernet, token, wireless]


#CONNECTION AREA
class WanArea(enum.Enum):
    city = 'City'
    region = 'Region'
    country = 'Country'
    continent = 'Continent'
    wanArea_list = [city, region, country, continent]


class LanArea(enum.Enum):
    house = 'House'
    edu_institution = 'Education Institution'
    company = 'Company'
    other = 'Important Local Place'
    lanArea_list = [house, edu_institution, company, other]
