name=''
def get_intent(data):
    global name
    m=data['message'].lower()
    if data['key']=="name":
        name=m
        return "next"
    if any(x in m for x in ["clock","time"]):
        return "clock"
    elif any(x in m for x in ["news","today news","get news"]):
            return "news"
    elif any(x in m for x in ["quote","quote of the day"]):
        return "quote"
    elif any(x in m for x in ["end","end the bot"]):
        return "end"
    elif "fetch" in m:
        return "fetch"
    else:
        return "echo"
def handle(data):
    global name
    from flask import render_template
    intent = get_intent(data)
    if intent=='clock':
        return render_template('messages/clock1.html',name=name,
        question={'text':'what is your next task ?'})
    elif intent=='next':
        return render_template('messages/greet.html',name=name,
            question={'key':'task','text': 'what can i do for you ?'})
    elif intent=='news':
        return render_template('messages/news1.html',name=name,
           question={'text':'what is your next task ?'})
    elif intent=='quote':
        return render_template('messages/quote1.html',data=data,
         question={'key':'task','text':' what is your next task ?'})
    elif intent=='end':
        return render_template('messages/end.html',data=data)
    else:
        return render_template('messages/echo.html',data=data)