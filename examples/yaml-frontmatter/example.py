from jinja2 import Environment, FileSystemLoader
from jinja_frontmatter import YAMLFrontmatterExtension

env = Environment(loader=FileSystemLoader('templates'))
env.add_extension(YAMLFrontmatterExtension)

print(env.get_template("index.html").render())