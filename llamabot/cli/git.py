"""Git subcommand for LlamaBot CLI."""

import pyperclip
from typer import Typer

from llamabot.code_manipulation import get_git_diff
from llamabot.prompt_library.git import commitbot, write_commit_message

from .utils import get_valid_input

gitapp = Typer()


@gitapp.command()
def hello():
    """Say hello."""
    print("Hello!")


@gitapp.command()
def commit_message():
    """Generate a commit message."""
    bot = commitbot()

    while True:
        diff = get_git_diff()
        if not diff:
            print(
                "I don't see any staged changes to commit! Please stage some files before running me again."
            )
            return
        message = bot(write_commit_message(diff))
        user_response = get_valid_input("Do you accept this commit message? (y/n) ")
        if user_response == "y":
            break
    pyperclip.copy(message.content)
