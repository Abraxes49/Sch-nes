import Taschenrechner
# import Fibonacci
# import Mini-Game

def main_menu():
    while True:
        print("\n---  MEGA-TOOL MENU ---")
        print("1. Taschenrechner öffnen 🧮")
        print("2. Fibonacci berechnen 🔢")
        print("3. Mini-Game starten 🎮")
        print("4. Beenden ❌")

        choice = input("Wähle eine Option: ")

        if choice == "1":
            Taschenrechner.Taschenrechner()
        elif choice == "2":
            print("🔥 Fibonacci kommt als nächstes...")
        elif choice == "3":
            print("🎮 Mini-Game wird bald programmiert...")
        elif choice == "4":
            print("👋 Programm beendet. Bis bald!")
            break
        else:
            print("❌ Ungültige Eingabe. Bitte erneut versuchen.")

if __name__ == "__main__":
    main_menu()
if __name__ == "__Taschenrechner":
    Taschenrechner()