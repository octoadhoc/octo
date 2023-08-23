import re

def chatbot_response(user_input):
    responses = {
        r"(hi|hello|hey|hey there)\b": "Hello! How can I help you?",
        "how are you": "I'm Doing well. Thank you for asking",
        r"(who is your creator|who created you)": "I was created by TEAM ADHOC",
        r"(who is your founder)": "Parvez Kabir",
        r"(which country are you from|where are you from)": "I am from Bangladesh",
        "bye": "Goodbye! Have a great day!",
        r"(Who is parvez kabir?)": "Parvez Kabir is a student of Daffidil International University, Department of CSE and he is From Team AdHOC",
        r"(say about Team AdHoc|What is Team Adhoc)": "The name AdHoc to reflect our ability to adapt and handle various challenges that may arise during the development process. Just like the term ad hoc in computing, which refers to something created for a specific purpose or situation, our team is adept at quickly creating innovative solutions tailored to meet the unique needs of anything. ",
        r"(help|can you help me)": "Of course! I'm here to assist you.",
        r"(what is your favorite color|do you have a favorite color)": "I don't have personal preferences",
        r"(who are the member of team adhoc)": "Nawshin, Sakib, Rajib, Tarik, Babu",
        r"(who are you)": "I'm OCTO. I'm your AI Assistent. I am here to help you",
        r"(I love you)": "oh Thank You. Love You Too",
        r"(I hate you)": "ohh sounds sad. i will cover up my mistakes",
        r"(Say About Bangladesh)": "Bangladesh is a South Asian country located on the northern coast of the Bay of Bengal. It shares borders with India to the west, north, and east, and Myanmar (Burma) to the southeast. Here are some key points about Bangladesh: 1. **Geography and Climate**: Bangladesh is characterized by its low-lying and deltaic geography, formed by the confluence of several major rivers, including the Ganges, Brahmaputra, and Meghna. This makes the country prone to annual monsoon flooding. The climate is tropical, with a hot and humid summer, a monsoon season, and a mild winter. 2. **Population and Culture**: With a population of over 160 million people, Bangladesh is one of the most densely populated countries in the world. The majority of the population follows the Bengali culture and speaks the Bengali language (Bangla). The culture is rich in music, literature, art, and traditional festivities. 3. **Economy**: Bangladesh has experienced significant economic growth in recent years, largely driven by its textile and garment industry, which is one of the largest in the world. The country also relies on agriculture, particularly rice production, as a major source of livelihood. Additionally, remittances from overseas Bangladeshis play a crucial role in the economy. 4. **History**: Bangladesh was part of British India until 1947 when India gained independence. It then became East Pakistan within the newly formed state of Pakistan. However, due to cultural, linguistic, and political differences, Bangladesh fought a war of independence against Pakistan in 1971 and emerged as an independent nation. 5. **Language Movement and Independence**: The Language Movement of 1952 played a significant role in shaping Bangladesh's identity. People protested against the imposition of Urdu as the sole national language and demanded recognition for Bengali. This movement laid the foundation for later political and cultural expressions that eventually led to the country's independence. 6. **Natural Disasters**: Bangladesh is highly vulnerable to natural disasters, including cyclones, floods, and riverbank erosion. The government and various organizations have implemented measures to mitigate the impact of these disasters and improve resilience. 7. **Wildlife and Environment**: The Sundarbans, a vast mangrove forest, is a UNESCO World Heritage Site shared between Bangladesh and India. It is home to the Bengal tiger and various other wildlife species. Bangladesh has been making efforts to protect its biodiversity and address environmental challenges. 8. **Development Challenges**: Despite its progress, Bangladesh faces various challenges, including poverty, political instability, and issues related to healthcare and education. The country has made efforts to improve these areas, but there is still work to be done. 9. **Cuisine**: Bengali cuisine is known for its use of rice, fish, lentils, and various spices. Dishes like rice and fish curry (known as machher jhol) are staples in the Bangladeshi diet. Sweets like rosogolla and mishti doi are also popular. 10. **Tourism**: Bangladesh offers diverse attractions for tourists, including historical sites like the ancient city of Bagerhat and the 60 Dome Mosque, as well as natural wonders like Cox's Bazar, the world's longest natural sea beach. Remember, this overview provides a snapshot of Bangladesh, and there is much more to explore and learn about this vibrant and diverse country.",
        

        # Add q
    }
    
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    return "I am still learning."

def main():
    print("Welcome")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'bye':
            print("OCTO: Goodbye!")
            break
        
        response = chatbot_response(user_input)
        print("OCTO:", response)

if __name__ == "__main__":
    main()
