from termcolor import colored, cprint

file_name = 'out1.txt'
file = open(file_name, mode='w', encoding='utf8')
file_content = '''# -*- coding: utf-8 -*-
My soul is dark - Oh! quickly string
The harp I yet can brook to hear;
And let thy gentle fingers fling
Its melting murmurs o'er mine ear.
If in this heart a hope be dear,
That sound shall charm it forth again:
If in these eyes there lurk a tear,
'Twill flow, and cease to burn my brain.

But bid the strain be wild and deep,
Nor let thy notes of joy be first:
I tell thee, minstrel, I must weep,
Or else this heavy heart will burst;
For it hath been by sorrow nursed,
And ached in sleepless silence, long;
And now 'tis doomed to know the worst,
And break at once - or yield to song.'''
file.write(file_content)
a = file_name


# print(file_content)
# file.close()
class Poetry:
    def __init__(self, file_name):
        self.file_name = file_name
        self.content = file_content

    def __enter__(self):
        self.file = open(self.file_name, 'r')
        cprint("-=вход=-", color='yellow')

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        cprint('-=выход=-', color='yellow')

    def some_method(self):
            cprint(file_content, color='cyan')


with Poetry(a) as byron:
    byron = Poetry(a)
    byron.some_method()

# Q: Чем отличается использование оператора with open(file_name...) от простого использования file.close()?
# A: Использование оператора with open () гарантированно закрывает файл при выходе из кода