"""
Class to interact with the AcSIP S76S LoRa Module
Write in MicroPython by Warayut Poomiwatracanont MAR 2023
Test on ESP32 with AcSIP S76S LoRa Module
"""
from machine import UART, Pin
from binascii import hexlify
import time, sys, random

class AcSIP_S76S(object):
    def __init__(self, uart_id, dev_class, port_num, data):
        self.uart_id = uart_id
        if len(dev_class) > 1:
            self.dev_class = "A"
        else: self.dev_class = dev_class.upper()
        self.port_num = port_num
        self.data = hexlify(data).decode("utf-8") 
       
        # If UART1 can not work properly, please use UART2 instead.
        self.uart = UART(uart_id, baudrate=115200, bits=8, parity=None, stop=1, timeout=200)

    # Send mac Command function.
    def sendCommand(self, command):
        rstr = ""
        print("Command: {0}".format(command))
        self.uart.write("{0}".format(command))
        rstr = self.uart.read()
        if rstr is None:
            rstr = "None"
        else: rstr = rstr.decode("utf-8")
        print(rstr)
        return rstr
       
    def config(self):
        print("Starting Reset Factory")
        self.sendCommand("sip reset")
        
        print("Setting up frequency")
        self.sendCommand("mac set_ch_freq 0 923200000")
        self.sendCommand("mac set_ch_freq 1 923400000")
        self.sendCommand("mac set_ch_freq 2 922000000")
        self.sendCommand("mac set_ch_freq 3 922200000")
        self.sendCommand("mac set_ch_freq 4 922400000")
        self.sendCommand("mac set_ch_freq 5 922600000")
        self.sendCommand("mac set_ch_freq 6 922800000")
        self.sendCommand("mac set_ch_freq 7 923000000")
        self.sendCommand("mac set_rx2 2 923200000")
        
        # Setup Class
        print("Setting up device class")
        self.sendCommand("mac set_class {}".format(self.dev_class))
        
        # Save the Config
        self.sendCommand("mac save")
        print("Config Module Successfully!\n")

    def check(self):
        # Get hardware infomation
        self.sendCommand("sip get_hw_model_ver")

        # Get device band
        self.sendCommand("mac get_band")

    def getKey(self): 
        print("----------For OTAA----------")
        # Get DevEUI
        DevEUI = self.sendCommand("mac get_deveui")[5:]
        
        # Generate AppKey
        hex_characters = "0123456789abcdef" 
        AppKey = "".join([random.choice(hex_characters) for i in range(32)])
        self.sendCommand("mac set_appkey {}".format(AppKey))
        # self.sendCommand("mac get_appkey")

        # Get Keys
        print("DevEUI for OTAA Athentication: {}".format(DevEUI))
        print("AppKey for OTAA Athentication: {}".format(AppKey))
        print("\n---------------------------\n")
        return DevEUI, AppKey

    def send(self):
        cnt = 0
        while True:
            status = self.sendCommand("mac get_join_status")
            self.sendCommand("mac tx ucnf {} {}".format(self.port_num, self.data))
            time.sleep(3)
            if status == "\n\r>> unjoined\n":
                if cnt == 0:
                    self.sendCommand("mac join otaa")
                    time.sleep(2)
                    cnt += 1
                else:
                    print("Sending Payload")
                    
    def doChoice(self):
        list = ["Check Module Infomation", "Auto Config Module", 
                "Show Key", "Send Data", "Quit"]

        # Do Choice List
        for i, x in enumerate(list):
            print("{0}. {1}".format(i + 1, repr(x).replace("'","")))
        
        num = int(input("Please select your choice: "))
        print()
        try:
            # Check if input is integer
            choice = int(num)
        # If not a integer
        except ValueError:
            print("************************************")
            print("You did not enter a valid integer")
            print("************************************\n")
            try:
                self.doChoice()
            except Exception:
                sys.exit(0)
                
        # Select the Choice
        if choice in range(1,len(list)+1):
            print("Roger That!\n")
            if choice == 1:
                self.check()
            elif choice == 2:
                self.config()
            elif choice == 3:
                self.getKey()
            elif choice == 4:
                self.send()
            elif choice == 5:
                print("----------Bye----------")
                sys.exit(0)

        # If input out of range
        else:
            print("************************************")
            print("The value is out of range")
            print("************************************\n")
            try:
                self.doChoice()
            except Exception as err:
                raise SystemExit(err)

if __name__ == "__main__":
    pass

