def main():
    file = 'books/frankenstein.txt'
    with open(file) as f:
        text = f.read()
        words = text.split()
        occurences = count_letters(text)
        sorted_occurences = sorted(occurences, reverse=True, key=sort_dict)
        print(f'--- Begin report of {file} ---')
        print(f'{len(words)} words found in the document')
        for item in sorted_occurences:
            print(f'The "{item["letter"]}" character was found {item["count"]} times')
        print('--- End report ---')


def sort_dict(dict):
    return dict['count']

def count_letters(text):
    occurences = {}
    data = []
    for letter in text.lower():
        if(letter in occurences):
            occurences[letter] += 1
        else:
            occurences[letter] = 1
    for item in occurences:
        if(item.isalpha()):
            data.append({'letter': item, 'count': occurences[item]})
    return data

main()