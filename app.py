from datetime import datetime, timedelta
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
        "flower": random.choice(json.load(Path("data/flowers.json").open())["flowers"]),
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
        visitors.append(
            generate_random_modifiers(visitor.user.login, visitor.starred_at.date())
        )

    return visitors


def main(repo_name=str, mock_users=0):
    repo = g.get_repo(repo_name)

    visitors: list[dict[str, str]] = []

    for i in range(0, mock_users):
        # Group mock user in groups of 2
        date = datetime.today() + timedelta(days=i if i % 2 == 0 else i - 1)
        visitors.append(generate_random_modifiers(str(random.randint(0, 1000)), date.date()))

    visitors = visitors + create_visitors(repo)

    you = generate_random_modifiers(repo.owner.login, repo.created_at.date())

    stars = len(visitors) + 1 # Total number of stars is the number of visitors plus "you"

    loader = FileSystemLoader(".")
    env = Environment(
        loader=loader, extensions=["jinja2_humanize_extension.HumanizeExtension"]
    )
    def numword(number: int):
        return num2words(number)

    env.filters["numword"] = numword

    template = env.get_template("index.jinja")
    Path("index.html").write_text(
        template.render(
            {
                "visitors": visitors,
                "repo": repo,
                "you": you,
                "stars": stars,
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
    parser.add_argument(
        "--mock-users",
        default=0,
        type=int,
        help="Generate a test run with N numbers of mock users",
    )
    args = parser.parse_args()
    main(repo_name=args.repo, mock_users=args.mock_users)
