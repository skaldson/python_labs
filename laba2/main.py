# main module for this program
from local_network import LocalNetwork
from global_network import GlobalNetwork

# lan_conn/wan_conn, LanArea/WanArea are Enum use enum.key.value
# peripheral contain Computer/Printer/Fax classes
from network_devices import LanConnection as lan_conn, WanConnection as wan_conn
from network_devices import LanArea, WanArea
import peripheral


# main function
def main():
    LAN_1 = [LocalNetwork(), LocalNetwork(speed=2410, area=LanArea.house.value, conn_amount=8)]
    LAN_2 = LocalNetwork(lan_conn.wireless.value, LanArea.edu_institution.value,150, 8)
    LAN_1.append(LAN_2)
    WAN_1 = [GlobalNetwork(), GlobalNetwork(area=WanArea.continent.value, speed=4000)]

    for i in WAN_1:
        i.print_info()

    WAN_1[0].print_info()
    LAN_2.print_info()

    WAN_1[0].add_connection(LAN_1)
    WAN_1[0].add_connection(LAN_2)
    WAN_1[1].increase_speed(300)

    WAN_1[1].print_info()

    LAN_1[0].remove_connection()
    LAN_1[-1].change_connection_type(lan_conn.token.value)
    LAN_1[0].add_connection(peripheral.Computer())
    LAN_1[0].add_connection(peripheral.Fax())

    for i in LAN_1:
        i.print_info()

if __name__ == "__main__":
    main()
