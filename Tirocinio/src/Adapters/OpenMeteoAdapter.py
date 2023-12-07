import requests

class OpenMeteoAdapter():
    def __init__(self, lat, lon):
        #controllo latitudine e longitudine
        if lat < -90 or lat > 90:
            raise Exception("Latitudine non valida")
        elif lon < -180 or lon > 180:
            raise Exception("Longitudine non valida")
        self.lat = lat
        self.lon = lon

    def get_data_temperatura(self):
        
        url = "https://api.open-meteo.com/v1/forecast?"\
            "latitude=" + str(self.lat) + "&longitude=" + str(self.lon) + \
            "&hourly=temperature_2m"
        data = requests.get(url).json()
        return data
    
    def get_data_umidita(self):
        
        url = "https://api.open-meteo.com/v1/forecast?"\
            "latitude=" + str(self.lat) + "&longitude=" + str(self.lon) + \
            "&hourly=relative_humidity_2m"
        data = requests.get(url).json()
        return data
    
    def get_data_pressione(self):
        
        url = "https://ensemble-api.open-meteo.com/v1/ensemble?"\
            "latitude="+ str(self.lat) + "&longitude=" + str(self.lon) + \
            "&hourly=surface_pressure&models=icon_seamless"
        data = requests.get(url).json()
        return data

    def get_data_vento(self):
        
        url = "https://api.open-meteo.com/v1/forecast?"\
            "latitude=" + str(self.lat) + "&longitude=" + str(self.lon) + \
            "&hourly=wind_speed_10m,wind_speed_80m,wind_speed_120m"
        data = requests.get(url).json()
        return data
