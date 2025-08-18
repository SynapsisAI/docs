# TikaOCR Documentation

## Overview

TikaOCR is a fast text extraction tool that works well as a general-purpose OCR
service. It provides reliable basic text extraction from PDFs and other document
formats.

## Capabilities

- Fast processing speed suitable for real-time applications
- Fairly good accuracy with basic text extraction
- Works as a general-purpose OCR tool across multiple file formats
- Can be integrated with websockets for real-time processing

## Limitations

Only extracts basic text content - does not preserve:

- Text formatting (bold, italics, fonts)
- Images
- Table structures
- Captions or headers as distinct elements

## Potential Use Case: Basic Tier Service

Stream lecture slides in and out for real-time summarization. This would work
well for a basic service tier where users need quick text extraction from
presentations without requiring preservation of visual elements or complex
formatting. The fast processing speed makes it suitable for live lecture
scenarios where slides are being presented and summarized in real-time.
