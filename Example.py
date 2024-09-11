from CSolver.solver import Solver
import time

csolver = Solver("CSolver-API-Key")

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
proxy = 'user:pass@ip:port'

balance = csolver.balance()
print(balance)

st = time.time()
hcapSolution = csolver.hcaptcha(
    'hCaptchaEnterprise',
    '4c672d35-0701-42b2-88c3-78380b0db560',
    'discord.com',
    proxy
)
print(f"Solved --> {hcapSolution[:45]}... --> {round(time.time()-st,2)}")

st = time.time()
recapSolution = csolver.recaptcha3(
    True,
    ua,
    'https://www.google.com/recaptcha/api2/anchor?ar=1&k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge&co=aHR0cHM6Ly8yY2FwdGNoYS5jb206NDQz&hl=en-US&v=EGbODne6buzpTnWrrBprcfAY&size=invisible&cb=berzf6upszbg',
    'https://www.google.com/recaptcha/api2/reload?k=6Lcyqq8oAAAAAJE7eVJ3aZp_hnJcI6LgGdYD8lge'
)
print(f"Solved --> {recapSolution[:45]}... --> {round(time.time()-st,2)}")
