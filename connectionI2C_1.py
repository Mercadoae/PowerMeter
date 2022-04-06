from smbus2 import SMBus
import time

try:
    while True:
        with SMBus(1) as bus:
            comando = input("Ingresar comando (on/off): ")
            comando = comando + "\n"
            comando = comando.encode()
            bus.write_i2c_block_data(31, 0, comando) #direccion 31
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nInterrupcion por teclado")
except ValueError as ve:
    print(ve)
    print("Otra interrupcion")