import click
from helpers import (
    exit_program,
    create_hymn, 
    update_hymn,
    delete_hymn,
    list_hymns,
    view_lyrics,
    hymns_by_key,
    hymns_by_author
)

def menu():
    click.echo("Hi welcome to Eric's hymns app.")
    click.echo("We are glad to see you here ")
    click.echo("1: Create a new hymn")
    click.echo("2: Update an existing hymn")
    click.echo("3: Get the list of hymns")
    click.echo("4: Delete a hymn")
    click.echo("5: View hymn lyrics")
    click.echo("6: Hymns by key")
    click.echo("7. Hymns by author")
    click.echo("8: Exit")


def main():
    while True:
        menu()
        choice = click.prompt("Select an option", type=str)
        if choice == "1":
            create_hymn_input()

        elif choice == "2":
            update_hymn_input()
        elif choice == "3":
            list_hymns()

        elif choice == "4":
            delete_hymn_input()

        elif choice == "5":
            view_lyrics_input()

        elif choice == "6":
            hymns_by_key_input()

        elif choice == "7":
            hymns_by_author_input()

        elif choice == "8":
            exit_program()
        
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

def view_lyrics_input():
    hymn_id = click.prompt("Enter the hymn Id")
    view_lyrics(hymn_id)

def hymns_by_key_input():
    key_name = click.prompt("Enter the key")
    hymns_by_key(key_name)

def hymns_by_author_input():
    author_name = click.prompt("Author")
    hymns_by_author(author_name)
    
if __name__ == "__main__":
    main()