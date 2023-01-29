# NbConvert PDF Exporter with LaTeX Titles

A pip-installable nbconvert exporter that creates PDFs with a header defined using tagged cells.

## Tags

`title`, `authors`, `date`

The exporter will remove the first cell with each of these tags from the export and use their plain-text content for the LaTeX title at the top of the document.

## Usage

Navigate to this folder and run `pip install .` The exporter will show up under the "Download as" menu in JupyterLab or can be used on the command line with `jupyter nbconvert --to pdf_header mynotebook.ipynb`. See below to replace the default PDF and LaTeX templates with this one.

## Enabling by default for all LaTeX exports

Add these lines to ~/.jupyter/jupyter_nbconvert_config.py

```python
c.LatexExporter.extra_template_basedirs = ['/path/to/this/folder/header_pdf_exporter/templates']
c.LatexExporter.template_name = 'latex_header'
```