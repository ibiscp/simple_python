from semantic_release.history.logs import generate_changelog

def generate_custom_changelog(version):
    """
    Generate a changelog with emojis based on commit types.
    """
    changelog = generate_changelog(version)

    # Define mappings from commit types to emojis
    emoji_map = {
        'feat': '✨',  # Feature
        'fix': '🐛',   # Bug Fix
        'perf': '⚡',  # Performance Improvement
        'docs': '📚',  # Documentation
        'style': '💎',  # Style
        'refactor': '🔨',  # Refactor
        'test': '🚨',  # Tests
        'build': '🏗️',  # Build System
        'ci': '🤖',  # CI
        # Add more mappings as needed
    }

    # Add emojis to the changelog
    for commit_type, emoji in emoji_map.items():
        changelog = changelog.replace(commit_type + ':', emoji + ' ' + commit_type + ':')

    return changelog

# Example usage
if __name__ == "__main__":
    # You should replace 'your_version_here' with the actual version you are generating the changelog for
    version = 'your_version_here'
    custom_changelog = generate_custom_changelog(version)
    print(custom_changelog)
