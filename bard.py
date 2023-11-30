from bardapi import BardCookies
import datetime
import speak as sp


    
cookie_dict={
    "__Secure-1PSID" :  "dAhdEnu1x3Oti3O7tLm2y2FpJlVxiDyFLnEyEhT9GDZPompL_6WUjpJ53DOAZPoT1gzGbQ.",
    "__Secure-1PSIDTS" :  "sidts-CjIBNiGH7vb6XBKCb80pGx6X_5BGDHIAnJmY455PeGm-D98kL1WGD3HaykelP7EBzmjVEhAA",
    "__Secure-1PSIDCC" :  "ACA-OxP7_L_gA7M_6GPD5ZT7CZuu5CbRzhQQzmmn-Kmah8rJrCf_d4BVlpQ2gsYsgRjlmbVI3Ec"

}
bard=BardCookies(cookie_dict=cookie_dict)
def reply(Query):    

    reply=bard.get_answer(Query)['content']
    print(reply)
    sp.speak(reply)
    
