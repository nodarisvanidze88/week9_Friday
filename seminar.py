# import random
# from statistics import mean
# from collections import Counter

# random_integers = [random.randint(1,1000) for _ in range(1000)]

# unique_integers = list(dict.fromkeys(random_integers))
# sorted_unique_integers  = sorted(unique_integers)
# average = sum(unique_integers) / len(unique_integers)

# top_integers = Counter(unique_integers ).most_common(5)
# print(top_integers)

# import re
# text = "This is a `code snippet`. Use `print('Hello, world!')` to display a message."

# def extract_code(text):
#     pattern = r'`([^`]+)`'
#     return re.findall(pattern, text)

# result = extract_code(text)
# print(result)

# import re
# text = "The event is scheduled for 2024-03-25. Please RSVP by 2024-03-20."

# def extract_date(txt):
#     pattern = r'\b\d{4}-\d{2}-\d{2}\b'
#     return re.findall(pattern, txt)

# result = extract_date(text)
# print(result)

# import re
# html_string = "<p>This is <b>bold</b> and <i>italic</i>.</p>"

# def remove_teges(txt):
#     pattern = r'<.*?>'
#     return re.sub(pattern,"",txt)

# result = remove_teges(html_string)
# print(result)

# import re
# text = "Check out our website at https://www.example.com or visit http://example.org for more information."

# def extract_Links(txt):
#     pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'
#     return re.findall(pattern, txt)

# result = extract_Links(text)
# print(result)
# import re
# text = "The quick brown fox jumps over the lazy dog the the sdkflsdkfl the."
# word = "the"
# def count_word(txt, word):
#     pattern = r'\b' + re.escape(word) + r'\b'
#     return re.findall(pattern, txt)

# result = count_word(text.lower(),word.lower())
# print(len(result))


# import re
# text = "Please contact me at 123-456-7890 or 987.654.3210."
# def extract_phone_numbers(txt):
#     pattern = r'\b\d{3}[-.]?\d{3}[-.]?\d{4}'
#     return re.findall(pattern, txt)

# result = extract_phone_numbers(text)
# print(result)

# def main():
#     user_text = input("Give me the Text: ")
#     shift = int(input("Give shift value: "))
#     encripted = shifter(user_text,shift)
#     decripted = shifter(encripted,-shift)

#     print(encripted)
#     print(decripted)

# def shifter(txt, shift):
#     result_text = ""
#     for char in txt:
#         if char.isalpha():
#             shifted = ord(char)+shift
#             if char.islower():
#                 if shifted > ord('z'):
#                     shifted -= 26
#                 elif shifted < ord('a'):
#                     shifted += 26
#             elif char.isupper():
#                 if shifted > ord('Z'):
#                     shifted -= 26
#                 elif shifted < ord('A'):
#                     shifted += 26
#             result_text += chr(shifted)
#         else:
#             result_text += char
#     return result_text
    
# main()

# def main():
#     file_path = 'sample_text.txt'
#     result = text_analize(file_path)
#     print(result)

# def text_analize(file_path):
#     with open(file_path, 'r') as file:
#         text = file.read()
    
#     words = text.split()
#     num_words = len(words)
#     unique_words = set(words)
#     unique_words_num =len(unique_words) 
#     word_count = {word: words.count(word) for word in unique_words}
#     most_common_word = max(word_count, key=word_count.get)
#     avg_word_length = sum(len(word) for word in words) / num_words

#     return avg_word_length

# main()

# def main():
#     user = int(input("Give me the Limit: "))
#     result = generate_primes(user)
#     print(result)

# def generate_primes(limit):
#     primes = []
#     for num in range(2, limit+1):
#         is_prime = True
#         for i in range(2, int(num**0.5)+1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#         if is_prime:
#             primes.append(num)
#     return primes
# main()
