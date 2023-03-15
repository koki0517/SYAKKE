#!/usr/bin/env pybricks-micropython
from pybricks.iodevices import UARTDevice
from pybricks.parameters import Port
from pybricks.tools import wait

esp = UARTDevice(Port.S1, 115200,100)
esp.clear()
wait(1000)
print("start")

while 1:
    esp.write((10).to_bytes(1,'big')) # ESP32に値のリクエスト(10)を送る
    error_count = 0
    while esp.waiting() < 4: # 受信バッファに4Byteたまるまで待つ
        wait(10) # 待てる最大の時間は10ms
        print("error")
        esp.write((10).to_bytes(1,'big')) # リクエストの再送
    # 4Byte読み取る
    # whatread[n]の形で使うときは型がunsigned(正の数)になる
    whatread = esp.read(4)
    print(str(whatread[0])+", "+str(whatread[1])+", "+str(whatread[2])+", "+str(whatread[3]))
    wait(500)