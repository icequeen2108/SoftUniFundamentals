spell = input()

while True:
    command = input().split(" ")
    action = command[0]

    if action == "Abracadabra":
        break

    elif action == "Abjuration":
        spell = spell.upper()
        print(spell)

    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)

    elif action == "Illusion":
        index, letter = int(command[1]), command[2]
        if 0 <= index < len(spell):
            spell = spell[:index] + letter + spell[index +1:]
            print("Done!")
        else:
            print("The spell was too weak.")

    elif action == "Divination":
        first_substring, second_substring = command[1], command[2]
        if first_substring in spell:
            spell = spell.replace(first_substring, second_substring)
            print(spell)

    elif action == "Alteration":
        substring = command[1]
        if substring in spell:
            spell = spell.replace(substring,"")
            print(spell)
    else:
        print("The spell did not work!")

