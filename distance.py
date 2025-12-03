import streamlit as st
from dotenv import load_dotenv
import os
import urllib.parse
from urllib.parse import quote
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

st.title("Distance Matrix Calculator")

def get_distance(origins, destinations):
    selected = st.selectbox('Source', origins)
    des = st.text_input('Destination', destinations)
    
    destinations = [des.strip()]
    
    origins_list = origins
    destinations_list = destinations
    
    origins_encoded = urllib.parse.quote("|".join(origins_list))
    destinations_encoded = urllib.parse.quote("|".join(destinations_list))
    
    if st.button('Calculate Distance'):
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origins_encoded}&destinations={destinations_encoded}&units=imperial&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data['status'] == 'OK':
            print(data)
            origin_index = origins_list.index(selected)
            distance = data['rows'][origin_index]['elements'][0]['distance']['text']
            st.write(f"Distance: {distance}")
        else:
            st.write("Error fetching distance data.")
            
if __name__ == "__main__":
        
    origins = ["13573 Tehachapi Blvd", "33503 CA-138, Lebec", "19409 National Trails Hwy, Oro Grande", 
               "9350 Oak Creek Rd, Mojave", "5808 CA-18, Lucerne Valley", 
               "16888 E St, Victorville", "401 Canal St, Wilmington", "1150 Pier F Ave, Long Beach"
               "13846 Firestone Blvd, Santa Fe Springs", "14501 Macaw St, La Mirada"
               "10411 Live Oak Ave, Fontana"]
    #destinations = ["840 S Cucamonga Ave"]
    destinations = ""
    
    get_distance(origins, destinations)