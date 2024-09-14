from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot function (a placeholder; replace with your actual chatbot logic)
def get_chatbot_response(user_input):
    # Simple example of chatbot response logic
    responses = {
        "hello": "Hi there! How can I help you?",
        "how are you": "I'm just a bot, but I'm doing great!",
        "default": "I'm not sure how to respond to that. Can you please rephrase?"
    }
    return responses.get(user_input.lower(), responses["default"])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def Aboutus():
    return render_template('Aboutus.html')

@app.route('/costprojection')
def costprojection():
    return render_template('costprojection.html')

@app.route('/livingroom')
def livingroom():
    return render_template('livingroom.html')

@app.route('/wardrobe')
def wardrobe():
    return render_template('wardrobe.html')


@app.route('/bedroom')
def bedroom():
    return render_template('bedroom.html')

@app.route('/bathroom')
def bathroom():
    return render_template('bathrooom.html')

@app.route('/kitchen')
def kitchen():
    return render_template('kitchen.html')


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_chatbot_response(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
