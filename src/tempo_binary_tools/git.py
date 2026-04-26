import requests


def get_commit_short_hash_from_tag(repo_name, is_online: bool, tag_name="latest"):
    """
    Gets the short commit hash (7 characters) for a given tag (default 'latest').

    Args:
        repo_name (str): GitHub repo in 'owner/repo' format.
        tag_name (str): The tag name to fetch the commit hash from.

    Returns:
        str: 7-character short commit hash or an error message.
    """
    if not is_online:
        raise RuntimeError('You are not able to get call get get_commit_short_hash_from_tag when not connected to the web.')
    try:
        # Get the tag reference
        tag_ref_url = (
            f"https://api.github.com/repos/{repo_name}/git/ref/tags/{tag_name}"
        )
        ref_response = requests.get(tag_ref_url)
        ref_response.raise_for_status()
        tag_ref = ref_response.json()

        # Lightweight tag points directly to a commit
        if tag_ref["object"]["type"] == "commit":
            return tag_ref["object"]["sha"][:7]

        # Annotated tag — follow the tag object
        tag_object_url = tag_ref["object"]["url"]
        tag_object_response = requests.get(tag_object_url)
        tag_object_response.raise_for_status()
        tag_object = tag_object_response.json()

        return tag_object["object"]["sha"][:7]

    except requests.exceptions.RequestException as e:
        return f"Request error: {e}"
    except KeyError:
        return "Tag or commit data not found."
