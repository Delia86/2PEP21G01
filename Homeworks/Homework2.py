"""Create a class for an object that can retrieve:
 - IP address from each interface on teh system and provide it as a dictionary ex: {'INTERFACE_NAME': 192.168.0.1}
        use command ipconfig (windows) or ifconfig (linux/macOS)
 - IPv4 Route Table as a list of dictionaries. ex: [{'Network Destination': '0.0.0.0', 'Gateway': 192.168.0.1 ...}, {Network...}]
        use command route print (windows) route -n (linux/macOS)"""
import re,os

class RetriveAdress():

    def get_Ip(self):
        result=str(os.popen('ipconfig').readlines())
        matches=re.finditer(r'(Ethernet|Wireless)(\s\w+)+',result)
        interfaces = []
        for match in matches:
            interfaces.append(match.group())
        ip_matches = re.finditer(r"disconnected|(?<=(Address. . . . . . . . . . . : ))(\d+\.)+\d+",result)
        ip_adresses = []
        for ip_match in ip_matches:
            ip_adresses.append(ip_match.group())
        dict = {interfaces[i]: ip_adresses[i] for i in range(len(interfaces))}
        return dict

    def get_Route_Table(self):
            result = str(os.popen("route print").readlines())
            matches = re.finditer(r"(\d+\.)+\d|On-link|\d{2,3}(?=\\n)",result)
            values=[]
            for match in matches:
               values.append(match.group())
            keys=["Network Destination", "Netmask", "Gateway", "Interface", "Metric"]
            l_dict={keys[i]:values[i] for i in range(len(keys))}
            print(dict)
            list_of_dict=[]
            l2_dict=l_dict.copy()
            list_of_dict.append(l2_dict.copy)
            return list_of_dict




if __name__ == '__main__':
    address=RetriveAdress()
    print(address.get_Ip())
    print(address.get_Route_Table())