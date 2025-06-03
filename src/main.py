from get_names import read_names
from get_initials import format_names
from write_names import write_names
import config

def main():
    names = read_names(config.READ_PATH)
    formated_names = format_names(names)
    write_names(formated_names, config.WRITE_PATH)

main()