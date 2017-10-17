import os
import osa
import requests


FILES_DIR = 'currencies'

if __name__ == '__main__':
    with open(os.path.join(FILES_DIR, 'temps.txt')) as f_temp:
        print(f_temp.read())

    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')

    print(client.service.ConvertTemp(20, 'degreeCelsius', 'degreeFahrenheit'))
