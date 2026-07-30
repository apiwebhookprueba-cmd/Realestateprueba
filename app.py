from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "realestate_prueba_123"

@app.route("/webhook", methods=["GET"])
def verify_webhook():
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return challenge, 200

    return "Verification failed", 403


@app.route("/webhook", methods=["POST"])
def receive_webhook():
    data = request.json
    print("Mensaje recibido:", data)

    return "EVENT_RECEIVED", 200


if __name__ == "__main__":
    app.run(port=5000, debug=True)