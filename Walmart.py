import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

walmart = yf.Ticker("WMT")
data = walmart.history(period="max")

data.reset_index(inplace=True)

#Tendencia precio cierre de Walmart
data.plot(x="Date", y="Close", title="Tendencia del precio de cierre de Walmart", figsize=(10,5))
plt.ylabel("Precio de cierre (USD)")
plt.show()

#Variación porcentual diaria
data["Daily Change %"] = data["Close"].pct_change() * 100
data["Daily Change %"].plot(title="Variación porcentual diaria del precio de Walmart", figsize=(10,5))
plt.ylabel("Cambio diario (%)")
plt.show()

#Promedios móviles 
data["MA30"] = data["Close"].rolling(30).mean()
data["MA90"] = data["Close"].rolling(90).mean()

data.plot(x="Date", y=["Close", "MA30", "MA90"], title="Precio de cierre con medias móviles (30 y 90 días)", figsize=(10,5), color="Blue")
plt.ylabel("Precio (USD)")
plt.show()

#Volumen de transacciones 
data.plot(x="Date", y="Volume", title="Volumen de transacciones de Walmart", figsize=(10,5), color="orange")
plt.ylabel("Volumen")
plt.show()




