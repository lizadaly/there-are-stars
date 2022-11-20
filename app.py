from datetime import datetime
import os
from pathlib import Path
import json
import random

from num2words import num2words
from github import Github
from github.Repository import Repository
from jinja2 import FileSystemLoader, Environment

g = Github(os.environ["GITHUB_TOKEN"])


def generate_random_modifiers(username: str, visited: datetime) -> dict[str, str]:
    random.seed(username)
    return {
        "weather": random.choice(
            json.load(Path("data/weather_conditions.json").open())["conditions"]
        ),
        "material": random.choice(
            json.load(Path("data/natural-materials.json").open())["natural materials"]
        ),
        "flower": random.choice(
            json.load(Path("data/flowers.json").open())["flowers"]
        ),
        "stone": random.choice(
            json.load(Path("data/decorative-stones.json").open())["decorative stones"]
        ),
        "metal": random.choice(
            json.load(Path("data/layperson-metals.json").open())["layperson metals"]
        ),
        "home": random.choice(
            json.load(Path("data/natural-places.json").open())["natural places"]
        ),
        "occupation": random.choice(
            json.load(Path("data/occupations.json").open())["occupations"]
        ),
        "trail_type": random.choice(["flower", "metal"]),
        "visited": visited,

    }


def create_visitors(repo: Repository) -> list[dict[str, str]]:
    visitors: list[dict[str, str]] = []

    for visitor in repo.get_stargazers_with_dates():
        visitors.append(generate_random_modifiers(visitor.user.login, visitor.starred_at))

    return visitors

def main(repo_name=str):
    repo = g.get_repo(repo_name)

    visitors = create_visitors(repo)
    you = generate_random_modifiers(repo.owner.login, repo.created_at)

    loader = FileSystemLoader(".")
    env = Environment(
        loader=loader, extensions=["jinja2_humanize_extension.HumanizeExtension"]
    )
    template = env.get_template("index.jinja")
    Path("index.html").write_text(
        template.render(
            {
                "visitors": visitors,
                "repo": repo,
                "you": you,
                "count": num2words(len(visitors))
            }
        )
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo",
        default="lizadaly/there-are-stars",
    )
    args = parser.parse_args()
    main(repo_name=args.repo)
