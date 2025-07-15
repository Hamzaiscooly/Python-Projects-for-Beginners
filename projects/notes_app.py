# Simple Notes App

notes = {}

while True:
    print("\nOptions: [add] note, [view] notes, [quit]")
    cmd = input("What do you want to do? ").strip().lower()

    if cmd == "add":
        title = input("Note title: ")
        content = input("Note content: ")
        notes[title] = content
        print("Note added.")
    elif cmd == "view":
        for title, content in notes.items():
            print(f"\n{title}\n{'-'*len(title)}\n{content}")
    elif cmd == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")