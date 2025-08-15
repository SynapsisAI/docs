# PDF Parsers to try

Here are the parsers I have found in the last semester:
1. LLamaParse
2. Copali https://huggingface.co/blog/manu/colpali
3. AllenAi Science-Parse: https://github.com/allenai/science-parse (seems ok, but alr from 6-7 years ago)
4. Docling: https://github.com/docling-project/docling
5. Grobid: https://github.com/kermitt2/grobid
6. Unstructured.io
7. TIKA Parser
8. Nougat (hasn’t been updated in a while)
9. tabula-py, or tabula-java: https://aegis4048.github.io/
10. PDFBox https://pdfbox.apache.org/ 
11. Texify/marker
12. poppler and surya ocr 
13. layoutlmv3
14. blip
15. Qwen 2.5 VL Instruct?
16. itext Pdfs: https://itextpdf.com/
Other in-built python libraries
1. PyMuPDF4
2. 
Other approaches
1. RAG approach by this video by Thu Vu
2. **LLM Chat Model**: Use other LLM: Gemini flash 2.0. llama 3.3; but need to have the correct approach
- Can try to put the Markdown output as input of ChatGPT and ask chatgpt to produce output, but so far the output is bad, and using double LLM just increases work load.
* think about what domain something is in. This will help the model understand the nuances that docling is struggling with.
think about what it needs to get absolutely right (e.g inline equations, tables, etc).
* Then, process 5 random documents to check painfully if the job is alright. If not, tune prompts, go again.
* I'd generally do it at either a page level or if the doc is small enough, just at the doc level.
* Quite similar to this, conceptually: https://generative-ai-newsroom.com/structured-outputs-making-llms-reliable-for-document-processing-c3b6b2baed36 Give it a read, and use the concepts around document processing here. 

| Parser / Tool | Advantages | Limitations / Notes | Internet Insights / Recent Findings | Best Use Case |
|---------------|------------|---------------------|--------------------------------------|---------------|
| **LLamaParse** | High accuracy layout parsing; integrates with LlamaIndex; supports OCR and table extraction. | Commercial API; cost for large-scale use; less open-source flexibility. | Strong for RAG pipelines where preserving document structure is crucial. | RAG pipelines for mixed-layout PDFs (lecture notes, handouts). |
| **RAG approach by Thu Vu** | Flexible retrieval-augmented generation pipeline; adaptable parsing for downstream tasks. | Requires careful embedding + retrieval design; depends on quality of parser used in pipeline. | Works well if tuned for domain-specific content like educational materials. | When combining parsing + semantic search in a custom pipeline. |
| **Colpali** ([HF blog](https://huggingface.co/blog/manu/colpali)) | Multi-modal model for PDF QA; integrates text and visual features. | Heavy model; requires GPUs; parsing quality depends on training domain. | Strong for extracting answers from document visuals. | Visual+text QA over diagrams and textbook figures. |
| **science-parse** ([GitHub](https://github.com/allenai/science-parse)) | Good at extracting metadata, sections from research papers. | Abandoned (~6-7 years old); scholarly formats only. | Not ideal for modern or non-research PDFs. | Parsing older academic papers for metadata. |
| **docling** ([GitHub](https://github.com/docling-project/docling)) | Modern parser with AI-assisted layout analysis. | Still evolving; may struggle with niche formats. | Designed for diverse document layouts including scanned notes. | General-purpose parsing of varied educational materials. |
| **GROBID** ([GitHub](https://github.com/kermitt2/grobid)) | Excellent for structured research papers; extracts references, metadata accurately. | Domain-specific to scholarly articles. | Best-in-class for academic PDFs. | Parsing journal articles for structured metadata. |
| **Unstructured.io** | Modular pipeline for splitting/parsing docs for AI/LLM ingestion. | Needs tuning for complex layouts. | Good for ingestion pipelines for varied docs. | Pre-processing PDFs for LLM workflows. |
| **Tika Parser** ([Apache Tika](https://tika.apache.org/)) | Extracts text, metadata; supports many formats. | Java-based; loses layout fidelity. | Industry standard for bulk extraction. | High-throughput, basic text extraction. |
| **Nougat** | Transformer-based PDF parsing (LaTeX/math aware). | Not updated recently; research prototype quality. | Former SOTA for scientific PDFs. | Math-heavy PDFs where layout is less important. |
| **PyMuPDF / PyMuPDF4** | High performance; preserves layout; supports image extraction & OCR. | OCR weaker than dedicated tools; license nuances. | Often outperforms PDFMiner in layout-heavy docs. | Mixed-text/image educational PDFs. |
| **Tabula / tabula-py** ([Guide](https://aegis4048.github.io/)) | Excellent for table extraction; multi-page support. | Only for tables; needs clean input. | Widely used in data workflows. | Extracting data tables from textbooks. |
| **PDFBox** ([Apache PDFBox](https://pdfbox.apache.org/)) | Robust Java library; text/image extraction & manipulation. | Java-based; needs wrappers for Python. | Enterprise-proven. | Enterprise-scale PDF processing. |
| **Texify / marker** | Converts PDFs to Markdown; math to LaTeX. | LaTeX sometimes inaccurate; needs extra OCR for fixes. | Good for creating LLM-friendly docs. | Converting lecture notes to Markdown with math support. |
| **Poppler** | Fast C++ backend; bindings in many languages. | No layout intelligence. | Often used internally by other tools. | Quick raw text extraction from digital PDFs. |
| **Surya OCR** | Modern, multilingual OCR. | Needs GPU for speed; OCR only. | High accuracy on scanned notes. | OCR for handwritten/printed lecture scans. |
| **layoutlmv3** | Layout-aware document model. | Requires fine-tuning. | Combines text + layout features. | Structured extraction from visually rich pages. |
| **BLIP** | Vision-language model for document images. | Needs image preprocessing. | Great for diagrams. | Extracting info from textbook diagrams. |
| **Qwen 2.5 VL Instruct** | Handles equations & diagrams via page-to-image. | Requires GPU; needs math cleanup. | Good for academic PDFs with math. | Parsing STEM lecture notes with math. |
| **iTextPDF** ([Site](https://itextpdf.com/)) | Commercial-grade PDF gen/parsing. | Licensing restrictions; Java-first. | Common in enterprise. | Reliable parsing + generation in Java apps. |
| **PyPDF2 / pypdf** | Simple API; basic manipulation. | Poor with complex layouts. | Maintained as `pypdf`. | Simple PDF splitting/merging tasks. |
| **PDFMiner.six** | Detailed layout control. | Slower; complex API. | Preserves positions. | Layout-sensitive extraction from textbooks. |
| **pdfplumber** | Built on PDFMiner; table & image extraction. | Slower than PyMuPDF. | High tabular accuracy. | Table extraction with positions preserved. |
| **OCRmyPDF** | Adds searchable text to scans. | No structural parsing. | Ideal for searchable archives. | Preprocessing scanned lecture PDFs. |
| **Camelot** | Visual table extraction. | Needs clean input. | Works well for academic tables. | Table-heavy academic documents. |
| **pdf-parser (Didier Stevens)** | Forensic PDF analysis. | Not for bulk parsing. | Great for PDF security work. | Security/metadata inspection. |
| **LLMWhisperer** | Layout-preserving for LLM ingestion. | API-based; cost. | Good for RAG ingestion. | Feeding structured PDFs into LLMs. |
| **olmOCR** | OCR for scans with diagrams/equations. | GPU-intensive. | Strong for complex educational scans. | Full OCR of STEM textbooks with diagrams. |
