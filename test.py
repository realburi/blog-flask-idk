from googletrans import Translator
import pandas as pd 
import csv

translator = Translator()
a = translator.translate("assainissement", src='fr',dest='mn')
print(dir(a))
print("*"*120)

# print("*"*120)
# print(a.text)
# print("*"*120)
# print(a.src)
# print("*"*120)
# print(a.origin)

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


print(a.extra_data)
print("*"*150)
print(a.pronunciation)
print("*"*150)
for data in a.extra_data['translation']:
	print(data)
print("*"*150)
for data in a.extra_data['possible-translations']:
	print(data)