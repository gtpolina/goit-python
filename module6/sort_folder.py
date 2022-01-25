import os
import re
import shutil
import sys

''' raplacing file to folder if extention is known except from repeting
    os.replace(d + '\\' + f, root + final_folder + new_f) for example '\\videos\\'
'''


def replace_root(final_folder):
    os.replace(d + '\\' + f, root + final_folder + new_f)


# function for file name prefix normalization

def normalize(file_prefix):
    dictionary = {
        'а': 'a',
        'б': 'b',
        'в': 'v',
        'г': 'g',
        'ґ': 'g',
        'д': 'd',
        'е': 'e',
        'ё': 'yo',
        'ж': 'zh',
        'з': 'z',
        'и': 'i',
        'i': 'i',
        'ї': 'yi',
        'й': 'i',
        'к': 'k',
        'л': 'l',
        'м': 'm',
        'н': 'n',
        'о': 'o',
        'п': 'p',
        'р': 'r',
        'с': 's',
        'т': 't',
        'у': 'u',
        'ф': 'f',
        'х': 'h',
        'ц': 'ts',
        'ч': 'ch',
        'ш': 'sh',
        'щ': 'shch',
        'ъ': '',
        'ы': 'y',
        'ь': '',
        'э': 'e',
        'є': 'ye',
        'ю': 'iu',
        'я': 'ia',
        'А': 'A',
        'Б': 'B',
        'В': 'V',
        'Г': 'G',
        'Ґ': 'g',
        'Д': 'D',
        'Е': 'E',
        'Ё': 'Yo',
        'Ж': 'Zh',
        'З': 'Z',
        'И': 'I',
        'I': 'I',
        'Ї': 'Yi',
        'Й': 'y',
        'К': 'K',
        'Л': 'L',
        'М': 'M',
        'Н': 'N',
        'О': 'O',
        'П': 'P',
        'Р': 'R',
        'С': 'S',
        'Т': 'T',
        'У': 'U',
        'Ф': 'F',
        'Х': 'H',
        'Ц': 'Ts',
        'Ч': 'Ch',
        'Ш': 'Sh',
        'Щ': 'Shch',
        'Ъ': '',
        'Ы': 'y',
        'Ь': '',
        'Э': 'E',
        'Є': 'Ye',
        'Ю': 'Yu',
        'Я': 'Ya',
    }

    tbl = file_prefix.maketrans(dictionary)
    file_prefix = file_prefix.translate(tbl)
    file_prefix = re.sub('[^\d\w]', '_', file_prefix)

    return file_prefix

# absolute path input in cmd, test root = r'C:\Users\Полина\Desktop\trash'


root = sys.argv[1]

category_list = ['images', 'videos', 'documents',
                 'music', 'archives', 'unknown_extentions']
for folder in category_list:
    if not os.path.isdir(os.path.join(root, folder)):
        os.mkdir(os.path.join(root, folder))

# folders recursion with file copy in final directories

for d, dirs, files in os.walk(root):

    for f in files:

        (prefix, suffix) = os.path.splitext(f)
        new_f = f.replace(prefix, normalize(prefix))
        suffix = suffix.strip('.')

        # move and rename files

        if suffix in {'jpeg', 'png', 'jpg', 'svg', 'bmp'}:
            replace_root('\\images\\')

        elif suffix in {'avi', 'mp4', 'mov', 'mkv'}:
            replace_root('\\videos\\')

        elif suffix in {'doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx'}:
            replace_root('\\documents\\')

        elif suffix in {'mp3', 'ogg', 'wav', 'amr'}:
            replace_root('\\music\\')

        # gz not supported by shutil, proclaimed as unkown
        elif suffix in {'zip', 'gztar', 'tar'}:
            replace_root('\\archives\\')

        else:
            # without changes

            os.replace(d + '\\' + f, root + '\\unknown_extentions\\' + f)


# recursive delete of directories
suffix_set = set()


def del_empty_dirs(path):

    for folder in os.listdir(path):
        low_path = os.path.join(path, folder)
        if folder in {'images', 'videos', 'documents', 'music', 'archives', 'unknown_extentions'}:

            if os.listdir(low_path):
                print(f'"{folder}" folder contains {os.listdir(low_path)}')
                suffix_set = set()  # cleaning set of file extentions
                for i in os.listdir(low_path):

                    # adding suffixes to the extentions set
                    suffix_set.add(i.split('.')[1])
                    if folder == 'archives':
                        folder_to_unpack = os.path.join(
                            low_path, i.split('.')[0])
                        shutil.unpack_archive(os.path.join(
                            low_path, i), folder_to_unpack)

                if folder == 'unknown_extentions':
                    print(f'extentions not recognized by code {suffix_set}\n')
                else:
                    print(
                        f'recognized extentions in "{folder}" folder {suffix_set}\n')

            else:
                print(f'"{folder}" folder is empty\n')
                continue

        if os.path.isdir(low_path):
            del_empty_dirs(low_path)
            if not os.listdir(low_path):
                os.rmdir(low_path)


del_empty_dirs(root)
