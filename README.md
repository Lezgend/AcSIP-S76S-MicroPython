# AcSIP-S76S-MicroPython
A very simple library and useful for AcSIP S76S LoRa Module on ESP32 or ESP8266 using MicroPython

# Specifications
* Model name: S76S
* Product Desc.: LoRa Wireless Communication Module
* Host Interface: UART
* Temp. Storage -50 to 105 degree Celsius
* Temp. Operating: -40 to 85 degree Celsius
* Humid. Storage: 10 to 95 % (non-condensing)
* Humid. Operating: 5 to 95 % (non-condensing)
* Dimension: 13 mm x 11 mm x 1.14 mm
* Package: LGA
* Supply voltage: 3.3 V (typical)
* Supply current: 5 uA (sleep), 9.6 mA (standby), 17.5 mA (receive), 127 mA (transmit)

Ref: [AcSIP Product brief 📑](https://www.acsip.com.tw/index.php?action=products-detail&fid1=19&fid2=&fid3=&id=79)

# Command Set
[S76S/S78S Commands Set Reference v1.6.5](https://edit.wpgdadawant.com/uploads/news_file/program/2019/35461/tech_files/S7678S_Commands_Set_Reference_1.6.5.pdf)

# Usage

## ESP32
|    | UART0 | UART1 | UART2 |
|----|-------|-------|-------|
| TX |   1   |   10  |   17  |
| RX |   3   |   9   |   16  |

The ESP32 has three hardware UARTs: UART0, UART1 and UART2. They each have default GPIO assigned to them.

Ref: [ESP32 UART 📗](https://docs.micropython.org/en/latest/esp32/quickref.html#uart-serial-bus)

## ESP8266
|    | UART0 | UART1 |
|----|-------|-------|
| TX |   1   |   2   |
| RX |   3   |   8   |

UART0 is bidirectional. \
UART1 is on Pins 2 (TX) and 8 (RX) however Pin 8 is used to connect the flash chip, so UART1 is TX only.

Ref: [ESP8266 UART 📘](https://docs.micropython.org/en/latest/esp8266/quickref.html?highlight=dht#uart-serial-bus)

# Example

## Result when run up the python script.
```
Which UART ID do you using ?: 2
Which class do you prefer ? (A, C): C
Which port number do you want to use ? (1-223): 10
Data to send (String): HELLO_WORLD

1. Check Module Infomation
2. Auto Config Module
3. Show Key
4. Send Data
5. Quit
Please select your choice:
```

## Result of choice number 1
```
Please select your choice: 1

Roger That!

Command: sip get_hw_model_ver

>> module=S76S ver=v1.6.5

Command: mac get_band

>> 923

Use CTRL-C to stop sending
```

## Result of choice number 2
```
Please select your choice: 2

Roger That!

Starting Reset Factory
Command: sip reset
                             
     ___        _____ _ ____ 
    /   | _____/ ___/(_) __ \
   / /| |/ ___/\__ \/ / /_/ / Tech Co., LTD
  / ___ / /__ ___/ / / ____/   LoRaWAN v1.0.2 Ready
 /_/  |_\___//____/_/_/         (Class A & C)

>> S76S - v1.6.5 - AS923 - Jun 25 2018 - 14:33:19 


Setting up frequency
Command: mac set_ch_freq 0 923200000

>> Ok

Command: mac set_ch_freq 1 923400000

>> Ok

Command: mac set_ch_freq 2 922000000

>> Ok

Command: mac set_ch_freq 3 922200000

>> Ok

Command: mac set_ch_freq 4 922400000

>> Ok

Command: mac set_ch_freq 5 922600000

>> Ok

Command: mac set_ch_freq 6 922800000

>> Ok

Command: mac set_ch_freq 7 923000000

>> Ok

Command: mac set_rx2 2 923200000

>> Ok

Setting up device keys
Command: mac set_appkey a8e69894dcde18e57829bdc05bcc2834

>> Ok

Setting up device class
Command: mac set_class C

>> Ok

Command: mac save
None
Config Module Successfully!

Use CTRL-C to stop sending
```

## Result of choice number 3
```
Please select your choice: 3

Roger That!

----------For OTAA----------
Command: mac get_deveui

>> Ok

>> 9c65XXXXXXXXXXXX

Command: mac get_appkey

>> a8e698********************cc2834

----------For ABP----------
Command: mac get_appskey

>> a8e698********************cc2834

Command: mac get_nwkskey

>> a8e698********************cc2834

Use CTRL-C to stop sending
```

## Result of choice number 4
```
Please select your choice: 4

Roger That!

Command: mac get_join_status

>> unjoined

Command: mac tx ucnf 10 48454c4c4f5f574f524c44

>> not_joined

Command: mac get_join_status

>> accepted

>> joined

Command: mac tx ucnf 10 48454c4c4f5f574f524c44

>> Ok

Command: mac get_join_status

>> mac command (downlink) 0302030001

>> tx_ok

>> joined

Command: mac tx ucnf 10 48454c4c4f5f574f524c44

>> mac command (uplink) 0307

>> Ok

Interrupted!

```

## Result of choice number 5
```
Please select your choice: 5

Roger That!

----------Bye----------
```
