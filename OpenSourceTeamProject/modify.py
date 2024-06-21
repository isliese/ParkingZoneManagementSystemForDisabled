import sys

def modify_text(user_input):
    return user_input + ' 우하하핳'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
        modified_text = modify_text(user_input)
        print(modified_text)
    else:
        print('No text provided')
        sys.exit(1)
