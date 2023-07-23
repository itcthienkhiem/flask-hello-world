from Bard import Chatbot


Secure_1PSID = "YgjdenmnVllP0049BbUVYL7_U8yPtf34t76GZNAqfrisYEUEkA4so6W30BHZpBPyFdGmhQ."
Secure_1PSIDTS = "sidts-CjEBPu3jIZCErivtDia39Tng0bJ2JoH1EP0-mUpQu3f-ekC7Svo1zpT83WTPrfs65qimEAA"

chatbot = Chatbot(Secure_1PSID, Secure_1PSIDTS)

answer = chatbot.ask("10 places to visit in the world?")
print(answer)
