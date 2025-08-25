import logging
import time
from pathlib import Path

from docling_core.types.doc import ImageRefMode, PictureItem, TableItem

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

_log = logging.getLogger(__name__)

IMAGE_RESOLUTION_SCALE = 2.0

def main():
  logging.basicConfig(level=logging.INFO)

  data_folder = Path(__file__).parent / "pdfs/"
  pdfs = [
    "dist_sys", 
    "attention_is_all_you_need", 
    "Lecture19_ProjectManagementPlanning"
    ]
  output_dir = Path("images")

  pipeline_options = PdfPipelineOptions()
  pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
  pipeline_options.generate_page_images = True
  pipeline_options.generate_picture_images = True

  doc_converter = DocumentConverter(
    format_options={
      InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
  )

  for pdf in pdfs:
    start_time = time.time()

    conv_res = doc_converter.convert(data_folder / f"{pdf}.pdf")

    # Set up output directories
    images_dir = output_dir / pdf
    images_dir.mkdir(parents=True, exist_ok=True)
    doc_filename = conv_res.input.file.stem

    # Save images of figures and tables
    tab_count = 0
    img_count = 0
    for element, _level in conv_res.document.iterate_items():
      if isinstance(element, TableItem): # Table
        element_image_filename = images_dir / f"table-{tab_count}.png"
        with element_image_filename.open("wb") as fp:
          element.get_image(conv_res.document).save(fp, "PNG")
        tab_count += 1

      if isinstance(element, PictureItem): # Images
        element_image_filename = images_dir / f"image-{img_count}.png"
        with element_image_filename.open("wb") as fp:
          element.get_image(conv_res.document).save(fp, "PNG")
        img_count += 1

    # Save text content as JSON with references to the images extracted
    json_filename = output_dir / f"{doc_filename}.json"
    conv_res.document.save_as_json(json_filename, image_mode=ImageRefMode.REFERENCED)

    end_time = time.time() - start_time

    _log.info(f"{pdf} extracted in {end_time:.2f} seconds.")

if __name__ == "__main__":
  main()
