def characters(unformatted):
    formatted_text = ""
    formatted_number = ""
    numbers_sum = 0  #هنا وقفت فيها عشان كنت عاوزه يطبع الارقام ثم يجمعها
    for character in unformatted:
        if character.isalpha(): #هنا وقفت في isalpha فا عملت سيرش 
            formatted_text += character.lower()
        elif character.isdigit(): #isdigit same thing in isalpha
            formatted_number += character
            numbers_sum += int(character) #int كنت عملاها (int(character))

    if formatted_text: #spaces
        formatted_text = formatted_text.capitalize()

    return formatted_text, formatted_number, numbers_sum  #رجعتها من جزء function  in the note bec. it doesn't work
unformatted = "L78uj32i1n9A"
formatted_text, formatted_numbers, numbers_sum = characters(unformatted)

print(f"Formatted Text: {formatted_text}")
print(f"Formatted Number String: {formatted_numbers}")
print(f"The sum of the numbers: {numbers_sum}")



