
# MarkdownWiki

One of my college assignments is to write the pages for an interactive Wiki website about Planning and Management of Computer Systems. The aim of doing this is to practice writing support documentation for support agents who need to educate themselves on a computer system. The exact details are fuzzy to me as the assignment brief hasn't been made available to us at the time of writing, but it's something along those lines.

## Overengineering for fun

The task requires us to make a resource with interlinked pages without the use of slideshow software such as Powerpoint. Everyone else has taken the easy (and probably smart) decision to sign up to a website builder service, but I decided that was dull. So instead, I endeavoured to spend a few days in the half term break devising a way to completely self host the Wiki and write all article text in Markdown.

After a bit of research I discovered a neat project called Strapdown.js, which is a client-side Markdown text-processor that turns MD into HTML completely inside the user's browser. This means that all I have to do is write an article, put it inside a very minimalistic HTML file referencing Strapdown, and it will handle the job of styling and formatting the text into an actual webpage. I was even able to find an extension that someone else made for adding a menu bar at the top of the page, which facilitates simplistic dropdown menus.

### Automating the tedium

So armed with both of these tools, I set to work with figuring out how to effectively put them to use. I very quickly realised that I would have to be copy/pasting the article text into each HTML file per page, and if I ever decided to add a page then I would have to update the page selection menu for every other page to reference the new one. I decided that this was too much hassle for when I needed to focus on writing.

Why do something repetitive and tedious when you can instead write a script to automate the task? So that is exactly what I did! There's a Python script with the express purpose of copying everything in a source folder into an almost identical folder, except along the way it formats the raw Markdown files into a minimalistic HTML file. It also has to generate the page's unique dropdown menu to include all the other pages in the Wiki.

## Instructions

Simply write Markdown in .md files within the Wiki folder as you wish, and run the Python script from a terminal. The article-template.html file dictates what the generated content gets wrapped inside, so any changes in there will affect the entire Wiki. The output is saved to a folder which is presently hardcoded into the source, but in the future I may add command-line options to override the defaults. 
