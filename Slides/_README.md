# README for slides
PDFs of slides for each chapter are included in this folder. The slides are minimal in the sense that they include major equations, figures, and results, but do not add a lot of explanatory text or examples. The intention is that these provide minimal working examples that you can edit and customize without having to re-type equations. 

The TEX files are provided for that purpose, and feel free to copy and edit those however works for your class. A few notes on the TEX files
1. Each chapter file requires the *_SlideInclude.tex* file, which is located in this folder. This has all the Latex header information. The slides use beamer for formatting, and you can change options for beamer in that header file. 
2. The figures included in the slides are all located in a separate "Figures" folder that you should find in the same Github repository as these slides. You'll need both folders to be downloaded to re-compile the slides. The "Figures" folder should be at the same level as the "Slides" folder. 

If you want to play with the actual code and/or data behind the figures