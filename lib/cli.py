import click
from helpers import (
    exit_program,
    create_hymn, 
    update_hymn,
    delete_hymn,
    list_hymns
)

def menu():
    click.echo("Hi welcome to Eric's hymns management.")
    click.echo("Select an option: ")
    click.echo("0: Exit")
    click.echo("1: Create a new hymn")
    click.echo("2: Update an existing hymn")
    click.echo("3: Get the list of hymns")
    click.echo("4: Delete a hymn")

def main():
    while True:
        menu()
        choice = click.prompt(">", type=str)
        if choice == "0":
            exit_program()
        
        elif choice == "1":
            create_hymn_input()

        elif choice == "2":
            update_hymn_input()
        elif choice == "3":
            list_hymns()

        elif choice == "4":
            delete_hymn_input()
        
        else:
            click.echo("Oops! Invalid choice.")

def create_hymn_input():
    number = click.prompt("Hymn Number", type=int)
    title = click.prompt("Title", type=str)
    lyrics = click.prompt("Lyrics", type=str)
    author_name = click.prompt("Author", type = str)
    key_name = click.prompt("Key", type=str)
    create_hymn(number, title, lyrics, author_name, key_name)

def update_hymn_input():
    hymn_id = click.prompt("Hymn Id ", type = int)
    title = click.prompt("The new title for the hymn ")
    lyrics = click.prompt("New lyrics for the hymn: ")
    author_name = click.prompt("New author ")
    key_name = click.prompt("New key ")
    update_hymn(hymn_id, title, lyrics, author_name, key_name)

def delete_hymn_input():
    hymn_id = click.prompt("Hymn id", type=int)
    delete_hymn(hymn_id)

if __name__ == "__main__":
    main()