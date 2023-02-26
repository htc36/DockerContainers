# CLIPxGPT Captioner

- First download the folder https://drive.google.com/file/d/1jZQ9eb21Ijx22Ts0oTNGrK7-WbQkjT5r/view?usp=share_link. Place it inside the folder 'weights', make sure it has the name model.pt
<img width="494" alt="image" src="https://user-images.githubusercontent.com/54700621/221389964-adbaf9f3-f3b7-4fe0-b978-4b467a1bfbc7.png">

- Make sure all the photos that need to be processed are inside the ./input folder. Every photo in that folder will be processed and renamed to the generated caption and placed into the ./output folder.
- docker compose build (this only needs to be run once and can take up to 15 minutes as a few GB's of models and liabarys need to be downloaded)
- docker compose up (this will start the captioner and will process all the photos in the ./input folder and place them in the ./output folder).
- If you want to process other photos just place it in the ./inputs folder and re run 'docker compose up'



