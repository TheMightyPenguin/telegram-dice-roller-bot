import time
import random
import telepot

def decode_dice(dice):
	dice = dice.split('d')
	return int(dice[0]), int(dice[1])

def roll(quantity, type_of_dice):
	return str([random.randint(1, type_of_dice) for _ in range(quantity)])

def pipe(size):
	return '8' + ('=' * clamp(size, 1, 3000)) + 'D'

def clamp(n, minimum, maximum):
	return max(minimum, min(maximum, n))

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	print '------------'
	print "Got Message: ", command
	print telepot.glance(msg)
	print msg['chat']

	try:
		if command == '/roll':
			message = '%s: %s' % ('1d6', random.randint(1, 6))

		elif '/roll' in command:
			dice = command.split(' ')[1]
			message = '%s: %s' % (dice, roll(*decode_dice(dice)))

		elif '/eval' in command:
			python_expression = ' '.join(command.split(' ')[1:])
			message = eval(str(python_expression))
			print 'message:', message

		elif '/pipe' in command:
			quantity = int(' '.join(command.split(' ')[1:]))
			message = pipe(quantity)

		print 'debug-message:', message
		bot.sendMessage(chat_id, message)
	except:
		bot.sendMessage(chat_id, 'Instruccion no reconocida')

if __name__ == '__main__':
	print 'hola'
	bot = telepot.Bot('165751672:AAHfTHCFjXUc13yE_DrZMdBAyy1drusSfC4')
	bot.notifyOnMessage(handle)
	print 'Listening ...'

	variables = {}
	while True:
		time.sleep(10)
