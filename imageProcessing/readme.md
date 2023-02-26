# CLIPxGPT Captioner

- Make sure all the photos that need to be process are inside the ./input folder. Every photo in there will be processed and renamed to the generated caption and placed into the ./output folder.
- docker compose build (this only needs to be run once and can take up to 15 minutes as a few GB's of models and liabarys need to be downloaded)
- docker compose up (this will start the captioner and will process all the photos in the ./input folder and place them in the ./output folder).
- If you want to process other photos just place it in the ./inputs folder and re run docker compose up
