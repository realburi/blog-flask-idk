from googletrans import Translator
translator = Translator()
# a = translator.translate('veritas lux mea', src='la',dest='mn')
# print(dir(Translator))

class Data:
	def __init__(self,data):
		self.data = data

	def to_sentences(self):
		return self.data.split(".")

	def unique_words(self):
		words = set(self.data.split())
		return list(words)

	def count(self):
		data = self.data.split()
		unique = len(set(data))
		non_unique = len(data)
		return unique, non_unique


with open('data.txt', 'r', encoding='utf-8') as data:
	data = Data(data.read())


print(data.count())