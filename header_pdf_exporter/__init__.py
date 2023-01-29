import os
from traitlets import default
from nbconvert.exporters import PDFExporter
from nbconvert.preprocessors import Preprocessor
from nbconvert.filters.pandoc import convert_pandoc

class HeaderPDFExporter(PDFExporter):
    export_from_notebook = 'PDF with LaTeX title'

    @default('template_name')
    def _template_name_default(self):
        return 'latex_header'
        
    extra_template_basedirs = [os.path.join(os.path.dirname(__file__), "templates")]


class FormatHeaderPreprocessor(Preprocessor):
    """
    Find and remove title, author, date tagged cells and dump them into notebook metadata if not already set
    """
    def preprocess(self, nb, resources):
        nb.cells = [cell for cell in nb.cells if self.keep_cell_or_save_metadata(nb, cell)]
        return nb, resources

    def keep_cell_or_save_metadata(self, nb, cell):
        tags = cell.get('metadata', {}).get('tags', [])
        plaintext = convert_pandoc(cell.source, 'markdown', 'plain') if cell.cell_type == 'markdown' else cell.source
        if 'title' in tags and nb.metadata.get('title', None) is None:
            nb.metadata.title = plaintext
        elif 'authors' in tags and nb.metadata.get('authors', None) is None:
            nb.metadata.authors = [{'name': name.strip()} for name in plaintext.split(',')]
        elif 'date' in tags and nb.metadata.get('date', None) is None:
            nb.metadata.date = plaintext
        else:
            return True
        return False
