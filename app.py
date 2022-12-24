import streamlit as st
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import requests


apikey="d28508c99b13258f304fcaa2db3b34e3eaed9cb7b3e0f0669b3221cb4701cbdb"


urlpaises="https://apiv3.apifootball.com/?action=get_countries&APIkey="+apikey


response=requests.get(urlpaises)
st.write(response.json())
