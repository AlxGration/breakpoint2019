import pymorphy2
import re

def normalize_rus(file_data):
    stop_words = [line.strip() for line in open('stop_words_ru.txt', encoding='utf-8')] # список русских стоп-слов
    file_data = [re.compile("[.;:!\'?,\"()\[\]]").sub(" ", line.lower()) for line in file_data]  # очищение от знаков прерывания
    file_data = [re.compile("(<br\s*/><br\s*/>)|(\-)|(\/)").sub("  ", line) for line in file_data] # очищения от двойных пробелов
    norm_data = [] 
    morph = pymorphy2.MorphAnalyzer()
    for file_text in file_data: # нормализуем каждое слово из каждого текста
        norm_data.append(' '.join([morph.normal_forms(word)[0] for word in file_text.split() 
                        if morph.normal_forms(word)[0] not in stop_words]))
    return norm_data
