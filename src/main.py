# Enter user input and Search text files for matches.
import re
import sys
import os


def get_search_str():
    """Get the text that the user would like to search for"""
    return input('Enter the string to search for in filenames:\n')


def get_swap_str():
    """Get the text that the user would like to swap"""
    return input('Enter the string to swap for found matches:\n')


def get_path():
    """Get the filepath where we will be searching"""
    return input('\nEnter the path of the folder you would like to search:\n')


def check_exit(str):
    """Check if the user wants to exit the script"""

    exit_reg = re.compile(r'exit(.){3}', re.IGNORECASE)
    try:
        m = exit_reg.search(str)
    except Exception as e:
        print("check_exit: failed...")
        print(f"check_exit: {e}")
        sys.exit()
    else:
        if m:
            print(f"check_exit: exiting!")
            sys.exit()
        else:
            return False


def search_txt_files():
    """Search text files for user input"""

    print("Enter \'exit...\' to quit")

    # create a regex of user input
    search_str = get_search_str()
    if not check_exit(search_str):
        input_reg = re.compile(search_str, re.IGNORECASE)

    swap_str = get_swap_str()
    check_exit(swap_str)

    # get the path and make sure it exists
    path = get_path()
    if not check_exit(path) and os.path.exists(path):

        print(f'search_txt_files: scanning... {os.path.join(path)}')

        # path exists to iterate over files
        for i in os.listdir(path):

            try:
                m = input_reg.search(i)
            except Exception as e:
                print("search_txt_files: failed...")
                print(f"search_txt_files: {e}\n")
            else:
                if m:
                    print(f"search_txt_files: match found!")
                    print(f"search_txt_files: {i}")

                    try:
                        base = os.path.splitext(i)[0]
                        print(
                            f"search_txt_files: Renaming file to: {base}{swap_str}")
                        os.rename(os.path.join(path, i),
                                  os.path.join(path, base + swap_str))
                    except Exception as e:
                        print("search_txt_files: Rename failed...")
                        print(f"search_txt_files: {e}\n")

    else:
        print('search_txt_files: The file path does not exist.')
        print(f'search_txt_files: {path}\n')


if __name__ == '__main__':
    while True:
        search_txt_files()
