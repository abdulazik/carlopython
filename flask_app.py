
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def processing():
	class returnToken:
		def checking (data, token, secretKey, confirmationCode):
			if 'type' not in data.keys():
	        	return 'not vk'
	 	   	if data['type'] == 'confirmation':
	        	return cofiramtionCode
	   		elif data['type'] == 'message_new':
		        session = vk.Session()
		        api = vk.API(session, v=5.69)
		        user_id = data['object']['user_id']
		        api.messages.send(access_token=token, user_id=str(user_id), message='Привет, я новый бот!')
	        # Сообщение о том, что обработка прошла успешно
	        return 'ok'

	token = ("b034fc3dab4426054d1eef2945ed182953705b2cff6a6a7b19aca50940c78d2ee9a0edf62cff1c23ceb02")
	secretKey = ("aeg348921hdf8h9a2u7fvhu")
	cofiramtionCode = ("7044d46d")
	data = json.loads(request.data)
	if data !== null:
		returnToken = returnToken()
		processing = returnToken.checking(data, token, secretKey, confirmationCoden)

    