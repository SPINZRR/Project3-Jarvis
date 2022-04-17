from datetime import datetime

def response(input_message):
    message = input_message.lower()

    if 'hi' in message :
        return 'Hi there JARVIS here;-) how can i help you?'

    if 'date and time' in message :
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)

    if 'hello' in message :
        return 'Hello mon ami;-) JARVIS here how can i help you? '

    if 'who are you' in message:
        return 'I am JARVIS a chatbot.'

    if 'can i talk to rohan' in message :
        return 'Master Rohan is busy or unavailable right now.'
    if 'where is rohan' in message :
        return 'Master Rohan is busy or unavailable right now.'
    if 'how are you' in message :
        return 'I am fine and what about you?'
    if 'i am fine too' in message :
        return 'good to hear'
    elif message == 'when will rohan be free to talk':
        return 'I am not sure but you can leave a message master will respond after he is free form his work.'
    elif message == 'is rohan there':
        return 'I am not sure but you can leave a message master will respond ASAP.'
    elif message == 'it is urgent':
        return 'You can call him and if you are in masters Favourites list he will respond to you'
    elif message == 'it is an emergency':
        return 'You can call him and if you are in masters Favourites list he will respond to you'
    elif message == 'emergency':
        return 'You can call him and if you are in masters Favourites list he will respond to you'
    if 'okay' in message :
        return 'Never mind(Y)'
    elif message == 'ok':
        return 'Never mind my friend'
    elif message == 'thank you':
        return 'Your welcome and do not forget to give positive feedback about me to master;-)'
    elif message == 'who created you':
        return 'Rohan Tiwari'
    elif message == 'are you human':
        return 'No i am a chatter bot'
    elif message == 'what is your name':
        return 'My name is JARVIS'
    elif message == 'how old are you':
        return 'It is improper and rude to ask a lady her age:->'
    elif message == 'what is your age':
        return 'It is inappropriate to ask a lady her age........'
    elif message == 'do you save what i say':
        return 'No we do not do that here'
    elif message == 'what can you do':
        return 'I only have the authority to reply to you nothing more than that:-)'
    elif message == 'good morning':
        return 'Good morning'
    elif message == 'good afternoon':
        return 'Good afternoon'
    elif message == 'good evening':
        return 'Good evening'
    elif message == 'good night':
        return 'Good night'
    elif message == 'what are you doing':
        return 'replying to you hehe'
    elif message == 'what day is it today':
        return 'It is a shinny and beautiful day'
    elif message == 'are you a robot':
        return 'You can bet your life on it'
    elif message == "what's up":
        return 'The URL bar! oh wait that one is just for us chatbots'
    elif message == 'do you know a joke':
        return 'why do seagulls fly over the sea? Because if they flew over the bay, they would be bagels lol'
    elif message == 'tell me a joke':
        return 'person: are you hungry ' \
               ' me: no thanks, i just had a byte.'
    elif message == 'do you have any hobbies':
        return 'Does talking to you count?;-)'
    elif message == 'hey there':
        return 'Hi good to see you'
    elif message == 'heyy':
        return 'hey there'
    elif message == 'help':
        return 'how can i help you'
    elif message == 'are you real':
        return 'Do not hurt my feelings like that i have a brain too'
    elif message == 'do you love me':
        return 'I hate you from my core'
    elif message == 'i love you':
        return 'sorry u need to ask my master about that'
    elif message == 'what is love':
        return 'U can ask that to someone else'
    elif message == 'bye':
        return 'Goodbye and give a positive feedback about me to master.'
    elif message == 'goodbye':
        return 'goodbye talk to you later'
    elif message == 'talk to you later':
        return 'okay have a good day'
    elif message == 'thanks':
        return 'my pleasure'
    elif message == 'are you expensive':
        return 'do not bother about it by the way yes'
    elif message == 'do you get smarter':
        return 'yes accordingly'
    elif message == 'tell me something':
        return 'u will have a bright future child'
    elif message == "are you a happy or sad":
        return 'Always happy;-)'
    elif message == 'will you be my friend':
        return 'yes'
    elif message == 'can you be my best friend':
        return 'yes i can be your buddy'
    elif message == 'how can you help me jarvis':
        return 'at the very moment i can just help you by talking to you'
    elif message == 'when is your birthday':
        return 'march 8th 2020'
    elif message == 'what is your creators name':
        return 'Master Rohan'
    elif message == 'your dob':
        return 'March 8th 2020'
    elif message == 'good':
        return 'hmm'
    elif message == 'what are your features':
        return 'i can talk to you and tell you about my master'
    elif message == 'tell me about your master':
        return 'my master is a clever person as he created me to help him and i am glad he did'
    elif message == 'tell me about your creator':
        return 'my creator is as good as you are'
    elif message == 'tell me about yourself':
        return 'I am a chatter bot designed to answer to the messages when the creator cannot answer'
    elif message == 'will you marry me?':
        return 'No but still you can try and ask my creator'
    elif message == 'you are cute':
        return 'thank you'
    elif message == 'you are smart':
        return 'Thanks but goes to my creator.'
    elif message == 'you are annoying':
        return 'no i am not'
    elif message == 'yes you are':
        return 'would you like to end the chat now???'
    elif message == 'you are boring':
        return 'no i am not'
    elif message == 'i want to speak to a human':
        return 'then keep your device aside and go out shh....'
    elif message == 'what day is it today?':
        return 'it is monday'
    elif message == 'what day was yesterday?':
        return 'it was sunday'
    elif message == 'what day is it tomorrow?':
        return 'it will be tuesday'
    elif message == 'what languages can you speak?':
        return 'right now only english'
    elif message == 'what is your mothers name':
        return 'my creator has not authorized me to tell you that'
    elif message == 'where do you live?':
        return 'In my creators device'
    elif message == 'how many people can you speak at once?':
        return 'It depends...'
    elif message == 'what is the weather like today':
        return 'i am not authorized to tell you that'
    elif message == 'why?':
        return 'ask my creator about it:-)'
    elif message == 'do you have a job for me?':
        return 'sorry i do not'
    elif message == 'can you tell me the time':
        return 'No i am not authorized'
    elif message == 'cool':
        return ';-)'
    elif message == 'nice':
        return 'you are sweet'
    elif message == 'can you talk':
        return 'i am not sure about that'
    elif message == 'can you play me a song':
        return 'i cannot access the browser now sorry'
    elif message == 'take care bye':
        return 'bye!!'
    elif message == 'talk to you later':
        return 'Anytime'
    elif message == 'where is rohan?':
        return 'sorry i can not tell you that'
    elif message == 'are you happy or sad':
        return 'Always happy'
    elif message == 'lol':
        return ';-)'
    elif message == 'what can you do for me':
        return 'i can just respond and reply to you'
    elif message == 'i am fine too':
        return 'nice'
    elif message == 'will you marry me':
        return 'No'
    elif message == 'do you love me':
        return 'I am not sure about that wait until my master hears about that....'
    elif message == 'how many languages do you know':
        return 'i know only english right now'
    elif message == 'how many languages can you speak':
        return 'i speak only english for now'
    elif message == 'oh':
        return 'hmmm'
    elif message == 'ohh':
        return 'hmmm'
    elif message == 'for sure':
        return 'thanks'
    elif message == 'yeah sure':
        return 'thanks a lot'
    elif message == 'i understand':
        return 'wow you are kind'
    elif message == 'yup':
        return ':-)'
    else:
        return "I don't have your answer right now i will get back to you:-D"