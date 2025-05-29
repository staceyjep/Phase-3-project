from lib.helpers import (
    add_entry,
    list_all_entries,
    delete_entry,
    clear_database
)
from lib.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Setup database
engine = create_engine('sqlite:///films.db')
Session = sessionmaker(bind=engine)
session = Session()

def show_menu():
    while True:
        print("\n🎬 Welcome to the Film Database CLI 🎬")
        print("1. Add New Entry")
        print("2. View All Entries")
        print("3. Delete an Entry")
        print("4. Clear the Entire Database")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_entry(session)
        elif choice == "2":
            list_all_entries(session)
        elif choice == "3":
            delete_entry(session)
        elif choice == "4":
            clear_database(session)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("⚠️ Invalid option. Please try again.")

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    show_menu()
