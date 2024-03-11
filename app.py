from flask import Flask, render_template, request
from nltk.chat.util import Chat

que1 = r'how are you'  # raw string, f-string, b-string
answers1 = [     'all well',    'I am good',    'awesome' ]

que2 = r'what can you do'
answers2 = [    'I can reply to your queries',    'I am here to answer your questions',    'I can chat with you' ]

que3 = r'(.*)your name'
answers3 = [    'my name is chatty',    'I am chatty' ]

que4 = r'(.*)mausam(.*)ba[a]*rish'  # aaj mausam kaisa hai, kya baarish hogi?
answers4 = [    'it looks it will rain today',    'baarish ka mausam hai',  'baarish ho sakti hai mausam kharab hai']

# Question Answer Pairs
qa_pair = [
    (que1, answers1),
    (que2, answers2),
    (que3, answers3),
    (que4, answers4),
 ]
chatbot = Chat(qa_pair)

# Question answer pairs
qa_pair=[
    (que1,answers1),
    (que2,answers2),
    (que3,answers3),
    (que4,answers4),
]

chatbot= Chat(qa_pair)

app= Flask(__name__)

@app.route('/')
def home():
    global chatbot
    query= request.args.get('query')
    print(query)
    if query != None:
        response = chatbot.respond(query)
        if response == None:
            print(response)
            response= 'Sorry I am not sure'
    else:    
        response = ''

    #return "This is coming from Flask"
    return render_template('index.html', result=response)

@app.route('/chatbot')
def chat():
    return "<h2>Chat Bot</h2>"

app.run(debug= True)