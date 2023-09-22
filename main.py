import smtplib # simple mail transport protocol
import requests  

# https://api.kanye.rest/ 

# API
response = requests.get(url="https://api.kanye.rest/") # request = žádost, response = odpověď
data = response.json()
quote = data["quote"]


# Odesílací email - Google
# kickerz.hc@gmail.com

# Přijímací email - Seznam
# mara.janik@post.cz

my_email = "kickerz.hc@gmail.com"
password = "tasrdqvikkclcagu"
message = "Subject: Důležitá zpráva\n\nAhoj, toto je testovací email" # \n\n - pozná to předmět
received_email = "mara.dymkar@email.cz" # pro více mailů se použije list (pole) [mail1@seznam.cz, mail2@seznam.cz,...]

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls() # tls = transport layer security
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs=received_email,
                        msg=quote.encode("utf-8")
                        ) # musíme dodat kódování (univerzální znaková sada)
    
