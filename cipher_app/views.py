from django.shortcuts import render
from django.http import JsonResponse

def vigenere_cipher(request):
    return render(request, 'cipher_app/index.html')

def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    key = key.lower()

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)]
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

def process_cipher(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        key = request.POST.get('key', '')
        action = request.POST.get('action', 'encrypt')

        if not key.isalpha():
            return JsonResponse({'error': 'The key must be a non-empty string of alphabetic characters.'})

        if action == 'encrypt':
            result = encrypt(message, key)
        else:
            result = decrypt(message, key)

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method.'})
