from pathlib import Path

def file_input():
    vector = list()
    for file in list(Path('.').rglob('*.vtt')):
        print('{}: {}'.format(len(vector) + 1, file.name))
        vector.append(file.name)
    choice = int(input('Insira o número do arquivo: '))
    select = vector[choice - 1]
    with open(select, 'r', encoding='UTF-8') as f:
        ata_out = f.read()
    line_block = ata_out.split('\n\n')
    ata_tuples = [(tuple(block.strip().split('\n'))) for block in line_block]
    return ata_tuples

def transcription_cleaner(tup):
    out = list()
    for i in tup:
        if 5 > len(i) > 2:
            out.append((i[2], i[3]) if len(i) == 4 else (i[2],))
    with open('saida1.txt', 'w', encoding='UTF-8') as output:
        for transcription in out:
            for line in range(len(transcription)):
                output.write('{}\n'.format(transcription[line]))
            output.write('\n')

if __name__ == '__main__':
    file = file_input()
    clean = transcription_cleaner(file)
    print('Limpeza concluída.')
