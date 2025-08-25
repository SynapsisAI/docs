*Docling's documentation can be found [here](https://docling-project.github.io/docling/).*
Docling is a PDF parsing library written in Python that can extract text, images, tables, and other page elements into more machine friendly formats. A Python file, [[docling_parser.py]], showcases the general workflow of the parser.

## Accuracy - Images and Tables
---
One of Docling's features is the ability to locate and extract images and tables from a document. But how accurate is this extraction? Preliminary testing on the PDF files found in [test_inputs](obsidian://search?vault=docs&query=path:test_inputs) yields the following results:
- Docling's *true positive* rate is 100%, that is, **all images and tables** in the documents are identified and extracted correctly and in order, including in the non-standard format found in the 'lecture' PDF.
- However, while Docling's *false positive* rate is low, it is not zero, as some page elements are classified as images and tables when they should not be.
This suggests that the library performs well for extraction, but context clues will need to be used (i.e. figure captions) to correctly determine what images are useful.

## Timings
---
*Note that tests were performed on CPU, and so results are not accurate to GPU capable devices*
Extraction timings for each PDF in [test_inputs](obsidian://search?vault=docs&query=path:test_inputs) when extracting text, images, and tables can be found below:

| PDF                                         | Time (seconds) |
| ------------------------------------------- | -------------- |
| [[dist_sys.pdf]]                            | 97.2           |
| [[attention_is_all_you_need.pdf]]           | 91.33          |
| [[Lecture19_ProjectManagementPlanning.pdf]] | 281.90         |

