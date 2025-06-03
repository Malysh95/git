from get_names import read_names
from get_initials import format_names
import config

def main():
    names = read_names(config.READ_PATH)
    formated_names = format_names(names)
    print(formated_names)

main()