import requests
from typing import Dict, Optional


def fetch_github_repo_details(repo_full_name: str, github_token: Optional[str] = None, timeout: int = 10) -> Dict[str, object]:
    """
    Fetch GitHub repository details using the GitHub REST API.

    Args:
        repo_full_name: Repository full name in the format 'owner/repo'.
        github_token: Optional GitHub personal access token for higher rate limits.
        timeout: Request timeout in seconds.

    Returns:
        A dictionary containing repository metadata.

    Raises:
        ValueError: For invalid input or repository not found.
        RuntimeError: For rate limit errors or bad API responses.
        ConnectionError: If the GitHub API is unreachable.
    """
    if not repo_full_name or not isinstance(repo_full_name, str) or "/" not in repo_full_name:
        raise ValueError("Repository name must be provided in 'owner/repo' format")

    owner, repo = [part.strip() for part in repo_full_name.split("/", 1)]
    if not owner or not repo:
        raise ValueError("Repository name must be provided in 'owner/repo' format")

    url = f"https://api.github.com/repos/{owner}/{repo}"
    headers = {
        "Accept": "application/vnd.github.v3+json",
    }
    if github_token:
        headers["Authorization"] = f"token {github_token.strip()}"

    try:
        response = requests.get(url, headers=headers, timeout=timeout)
    except requests.exceptions.RequestException as exc:
        raise ConnectionError(f"GitHub API is unavailable: {exc}") from exc

    if response.status_code == 404:
        raise ValueError(f"Repository not found: {repo_full_name}")

    if response.status_code == 403:
        message = response.json().get("message", "") if response.headers.get("Content-Type", "").startswith("application/json") else ""
        if "rate limit" in message.lower():
            raise RuntimeError("GitHub API rate limit exceeded")
        raise RuntimeError(f"GitHub API returned 403 Forbidden: {message}")

    if not response.ok:
        raise RuntimeError(f"GitHub API returned unexpected status {response.status_code}")

    try:
        repo_data = response.json()
    except ValueError as exc:
        raise ValueError("GitHub API returned invalid JSON") from exc

    required_fields = ["name", "description", "stargazers_count", "forks_count", "open_issues_count"]
    if not all(field in repo_data for field in required_fields):
        raise ValueError("GitHub API response is missing expected repository fields")

    return {
        "name": repo_data["name"],
        "full_name": repo_data.get("full_name", repo_full_name),
        "description": repo_data["description"] or "No description provided.",
        "stars": repo_data["stargazers_count"],
        "forks": repo_data["forks_count"],
        "open_issues": repo_data["open_issues_count"],
        "html_url": repo_data.get("html_url"),
    }


def display_repo_details(repo_details: Dict[str, object]) -> None:
    """Print GitHub repository details in a structured format."""
    print("\n" + "=" * 60)
    print("GITHUB REPOSITORY DETAILS")
    print("=" * 60)
    print(f"Name: {repo_details['name']}")
    print(f"Full Name: {repo_details['full_name']}")
    print(f"Description: {repo_details['description']}")
    print(f"Stars: {repo_details['stars']}")
    print(f"Forks: {repo_details['forks']}")
    print(f"Open Issues: {repo_details['open_issues']}")
    if repo_details.get("html_url"):
        print(f"URL: {repo_details['html_url']}")
    print("=" * 60 + "\n")


def main() -> None:
    try:
        repo_details = fetch_github_repo_details("torvalds/linux")
        display_repo_details(repo_details)
    except ValueError as exc:
        print(f"Input or repository error: {exc}")
    except RuntimeError as exc:
        print(f"GitHub API error: {exc}")
    except ConnectionError as exc:
        print(f"GitHub connection error: {exc}")


if __name__ == "__main__":
    main()
