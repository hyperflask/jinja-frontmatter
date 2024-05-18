from jinja2 import Environment, FileSystemLoader
from jinja_frontmatter import RemoveFrontmatterLoader, get_template_frontmatter

env = Environment(loader=RemoveFrontmatterLoader(FileSystemLoader('templates')))
print(env.get_template("index.html").render())
print(get_template_frontmatter(env, "index.html"))