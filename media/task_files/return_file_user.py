import os
from JarvisGeneral.Jarvis_CandF.connection_programs.data_file_user import *
from JarvisGeneral.search_us_file import programs_my_pc 



"""
ФУНКЦІЯ ЩО ПОВЕРТАЄ ДИРЕКТОРІЮ ФАЙЛУ
"""
def get_program(key) -> None:
    if key != None: # якщо ключ пустий програма нічого не шукатиме
        get_dir = programs[key] 
        #print(get_dir)
        return get_dir
    else:
        pass



