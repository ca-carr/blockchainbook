import os
import re

def replace_translation_tags(directory, replacements):
    """
    Recursively walks through the specified directory, finds all files
    with .html, .md, or .liquid extensions, and replaces {% t ... %} tags
    with the corresponding static text from the replacements dictionary.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith((".html", ".md", ".liquid")):
                filepath = os.path.join(root, file)
                with open(filepath, "r") as f:
                    content = f.read()

                # Replace each {% t key %} with its static text
                updated_content = content
                for key, value in replacements.items():
                    # Match {% t key %} and replace with the static text
                    updated_content = re.sub(rf"{{% t {key} %}}", value, updated_content)

                # Write updated content back to the file
                with open(filepath, "w") as f:
                    f.write(updated_content)

# Define the static replacements for translation keys here
replacements = {
    "home.heading": "Welcome to Blockchain Book",
    "home.about": "About Blockchain",
    "error.title": "Error 404, Page Not Found",
    "error.button": "Return to Homepage",
    "home.morevideos": "More Videos",
    "home.joincommunity": "Join the Community",
    "home.get_started": "Get Started",
    "home.choosewallet": "Choose a Wallet",
    "home.choosewallet_para": "Find the best wallet to securely store your blockchain assets.",
    "home.downloads": "Downloads",
    "home.getcoins": "Get Coins",
    "home.getcoins_para": "Learn how to acquire blockchain assets securely.",
    "home.exchanges": "Exchanges",
    "home.useit": "Use It",
    "home.useit_para": "Explore merchants and platforms that accept blockchain payments.",
    "home.merchants": "Merchants",
    "home.answers": "Get Answers",
    "home.faq_para": "Find answers to common questions about blockchain technology.",
    "home.faq": "FAQ",
    "home.guides": "User Guides",
    "home.guides_para": "Explore guides for users, developers, and resources.",
    "titles.userguides": "User Guides",
    "titles.developerguides": "Developer Guides",
    "titles.library": "Library",
    "moneropedia.back": "Back to Moneropedia",
    "home.contributecommunity": "Contribute to the Community",
    "home.contributecommunity_para": "Find out how to contribute to the blockchain ecosystem.",
    "home.contributing": "Contributing",
    "home.moneropedia_para": "A comprehensive guide to all things Blockchain.",
    "home.moneropedia_button": "Learn More",
    "titles.researchlab": "Research Lab",
    "home.researchlab_para": "Learn about cutting-edge blockchain research.",
    "home.visitmrl": "Visit the Research Lab",
    "home.meetcommunity": "Meet the Community",
    "home.meetus": "Connect with like-minded individuals in the blockchain space.",
    "home.hangouts": "Community Hangouts",
    "accessibility.arrowup": "Go to top",
    "accessibility.gotop": "Go to top",
}

# Specify the root path of your Jekyll project
project_directory = "."

# Run the replacement function
replace_translation_tags(project_directory, replacements)

print("Translation tags have been replaced with static text.")
