#!/usr/bin/python3
from pathlib import Path
import shutil

input_dir = Path("Wiki")
output_dir = Path("html")

# Remove the output directory if it already exists
if output_dir.exists() and output_dir.is_dir():
    print("Removing old build folder")
    shutil.rmtree(output_dir)

def directory_scan(folder: Path):
    """Recursively scans a Path and returns a list of lists/Paths"""
    contents = []
    for item in folder.iterdir():
        if item.is_dir():
            contents.extend(directory_scan(item))
        else:
            contents.append(item)
    return contents

# Load all pages and directory structure into memory
manifest = directory_scan(input_dir)

def process_article(file: Path, manifest: list):
    """Turns an article file into its HTML counterpart"""
    if file.is_dir():
        raise Exception("Cannot process non-file as article")
    # Generate list of all articles that should appear in the Pages menu
    pages = {}
    for item in manifest:
        if item == file:
            continue  # Do not include the present page in the list
        if ".md" not in str(item):
            continue  # Skip non-markdown files
        # Change file extension of articles in toc hyperlinks
        item = str(item).replace(".md", ".html")
        # Remove input directory name from page names
        name = item[len(str(input_dir)) + 1:]
        # Convert slashes in file path into greater-than signs as an arrow
        name = name.title().replace("/", " > ")
        # Remove file extension from article name and assign to dict, where key:value is url:name
        pages[item] = name[:name.rfind(".")]
    # Assemble HTML to be placed in the Pages menu
    links = "\n"
    for url, name in sorted(pages.items()):
        links += "<item><a href=\"/{}\">{}</a></item>\n".format(url, name)
    # Read in the article contents
    contents = file.read_text(encoding="UTF-8")
    with open("article-template.html", "r") as template:
        # Insert page links and article text into the template article
        output = template.read().format(links, contents)
    return output  # Return the generated HTML document

def process_manifest(manifest: list):
    """Iterates over every file, converting if needed or plain copies to destination otherwise"""
    def recurse(items: list, manifest: list):
        for item in items:
            print((" * " if str(item).endswith(".md") else "") + str(item))

            if type(item) is list:
                process_manifest(item, manifest)  # Recursively process folders

            # Determine where the file in question will be placed
            destination = output_dir / str(item).replace(".md", ".html")  # Make output files appear in the configured folder
            destination.parents[0].mkdir(parents=True, exist_ok=True)  # Make parent folder of path if it doesn't exist

            if str(item).endswith(".md"):  # Markdown document, process it
                # Convert markdown file into an HTML document and determine its location
                article = process_article(item, manifest)

                # Write contents
                with open(destination, "w") as file:
                    file.write(article)

            else:  # Other asset file, copy without processing
                destination.write_bytes(item.read_bytes())
    recurse(manifest, manifest)

# Turns all .md files into .html files and saves them, while copying anything else.
process_manifest(manifest)
