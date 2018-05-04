message = input()
decoded_message = []
p_char = True
for ch in message:
    if ch != ' ':
        if not p_char: # True
            decoded_message.append(ch)
        p_char = not p_char
    else:
        decoded_message.append(ch)
print(''.join(decoded_message))
