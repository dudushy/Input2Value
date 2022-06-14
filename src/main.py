# pip freeze > requirements.txt
#* -- Imports
import os

#* -- Variables
path = os.path.dirname(__file__) #? Directory path

#* -- Functions
def clearConsole() -> None: #? Clear console
    os.system("cls" if os.name == "nt" else "clear")

def main() -> None:  # sourcery skip: move-assign-in-block, use-join
    clearConsole()
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    raw_input = input("raw_input: ")
    aux = ""
    value = 0

    for i in range(len(raw_input)):
        if (raw_input[i] in numbers):
            aux += raw_input[i]
    value = int(aux)

    print(value)

#! Main
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
