def is_quit(command):
    cleaned = command.strip().lower()
    return cleaned == "q" or cleaned == "quit"


for command in ["  Q ", "Quit", "save", ""]:
    print(f"[{command}] -> {is_quit(command)}")
