import streamlit as st
import re
import random

class RuleBot:
    negative_response = ("no", "nope", "nah", "dont", "sorry", "never")
    exit_command = ("bye", "goodbye", "quit", "exit", "later")
    random_question = ("Who are you?", "Who created you?", "What is your name?")

    def __init__(self):
        self.support_responses = {
            #'skin_care': r'.*\s* skin care',
            'skin_care': r'.*\s* care',
           # 'on_sale': r'.*\s*  office_supplies',
            'on_sale': r'.*\s* supplies',
            'household_essential': r'.*\s* essential',
            'gaming_consoles': r'.*\s* console',
            'formal_clothes': r'.*\s* clothes',
            'home_appliances': r'.*\s* appliances',
            'contact_us': r'.*contact.*help.*'
        }

    def greet(self, username):
        st.write(f"🤖 **Bubble:** Hello, Welcome {username}! This is Bubble, the product shop assistant!")

    def make_exit(self, reply):
        if any(command in reply for command in self.exit_command):
            st.write("🤖 **Bubble:** Thank you! Have a great day!")
            return True
        return False

    def chat(self, reply):
        st.write(f"👤 **You**: {reply}")
        st.write(f"🤖 **Bubble:** {self.match_reply(reply)}")

    def no_match_intent(self):
        return "I'm sorry, I didn't understand your query. Can you please provide more details?"

    def match_reply(self, reply):
        combined_responses = ""
        for intent, regex_pattern in self.support_responses.items():
            found_match = re.search(regex_pattern, reply)
            if found_match:
                combined_responses += self.get_response(intent)
        return combined_responses if combined_responses else self.no_match_intent()

    def get_response(self, intent):
        if intent == 'skin_care':
            return self.skin_care()
        elif intent == 'office_supplies':
            return self.office_supplies()
        elif intent == 'household_essential':
            return self.household_essential()
        elif intent == 'gaming_consoles':
            return self.gaming_consoles()
        elif intent == 'formal_clothes':
            return self.formal_clothes()
        elif intent == 'home_appliances':
            return self.home_appliances()
        elif intent == 'contact_us':
            return self.contact_us()

    def skin_care(self):
        responses = ("Hey! We have a wide range of games. Listed below:",
                     "La Roche-Posay Anthelios Ultra-Light Mineral Sunscreen SPF 50\n",
                     "CeraVe Hydrating Mineral Sunscreen SPF 30\n",
                     "Biore UV Aqua Rich Watery Essence SPF 50+ PA++++\n",
                     "Banana Boat Ultra Sport Sunscreen Lotion SPF 50\n",
                     "Coppertone Sport Sunscreen Lotion SPF 50\n",
                     f"👤 **You** can find all the details on our website.\n")
        return "\n".join(responses)

    def office_supplies(self):
        responses = ("These are games that are on discount right now!:"
                     "HP OfficeJet Pro All-in-One Printer",
                     "V-LIGHT Traditional Style CFL Banker's Desk Lamp",
                     "Fellowes Powershred 79Ci 100% Jam Proof Cross-Cut Shredder",
                     "Canon PIXMA Wireless All-in-One Printer\n",
                     f"👤 **You** can find all the details on our website.\n")
        return "\n".join(responses)

    def household_essential(self):
        responses = ("Accessories available!:"
                     "Viva Signature Cloth Choose-A-Sheet",
                     "Dial Antibacterial Liquid Hand Soap",
                     "Hefty Ultra Strong Tall Kitchen Trash Bags",
                     "Clorox Clean-Up All Purpose Cleaner with Bleach",
                     "Air Wick Plug-In Scented Oil Air Freshener\n",
                     f"👤 **You** can find all the details on our website.\n")
        return "\n".join(responses)

    def gaming_consoles(self):
        responses = ("Below listed are the gaming consoles available!:"
                     "PlayStation 5 - 10 units",
                     "Xbox Series X - 8 units",
                     "Nintendo Switch - 15 units\n",
                     f"👤 **You** can find all the details on our website.\n")
        return "\n".join(responses)

    def formal_clothes(self):
        responses = ("Ralph Lauren\n"," Van Heusen\n"," Calvin Klein\n",
                     " Tie Clips/Bars: Tiffany & Co., Brooks Brothers, The Tie Bar\n"
                     "Cufflinks: Montblanc, Tiffany & Co., Hugo Boss.\n")
        return "\n".join(responses)

    def home_appliances(self):
        responses = ("Whirlpool refrigerators\n",
                     "Samsung washing machine\n",
                     "Panasonic microwaves\n",
                     "Nespresso Nespresso")
        return "\n".join(responses)

    def contact_us(self):
        responses = ("For more details, you can visit our website. Or you can mail us your query at gameshop@gmail.com")
        return "\n".join(responses)


def main():
    st.title("Bubble - Product Recommendation System")
    bot = RuleBot()
    username = st.text_input(f"🤖 **Bubble:** Can you provide me with your username?", key="username_input")
    if username:
        bot.greet(username)
        query = st.text_input(f"👤 **You**: ", key="query_input")
        if query:
            bot.chat(query)


if __name__ == "__main__":
    main()
