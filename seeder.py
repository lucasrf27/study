from pprint import pprint




with open('test123.txt', 'r') as file:
    all_music = []
    try:
        for row in file:
            spl = row.split('-')
            all_music.append(spl)
        for music in all_music:
            if len(music) > 1:
                print(music)
    except UnicodeDecodeError:
        raise
            
                



''''

        pprint(all_music)
        for word in all_music:
            print(word[0])
            print(word[1])
        pprint(len(all_music))
'''
'''
    for lista in all_music:
        if len(lista) < 2:
            all_music.remove(lista)
    pprint(all_music)
'''
'''
            if lista[1] is False:
                spl.remove(lista)
            print(spl)
        '''

'''
with open("test123.txt", "r") as input:
    with open("test123.txt", "w") as output: 
        for line in input:
            if line.strip("\n") == '':
                output.write(line)
'''