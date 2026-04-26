from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("/home/julian_jimenez/code/machinelearning/taller_2/docs/taller2-ml1-premier-league.pdf")

# Guardar en otra carpeta
with open("/home/julian_jimenez/code/machinelearning/taller_2/docs/taller2-ml1-premier-league.md", "w", encoding="utf-8") as f:
    f.write(result.text_content)