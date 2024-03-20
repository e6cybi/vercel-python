from flask import Flask
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def hello_world():
   

   url="https://nyahentai.re/magazine/re1596502/"
   if url.startswith("https://nyahentai.re/"):
                          
                         response = requests.get(url)
                         soup = BeautifulSoup(response.text, 'html.parser')
                         namet=soup.find("h1")
                         mame=namet.text
                         img_tags = soup.find_all('img') 
   image_urls =(i["src"] for i in  img_tags)                      
   return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Viewer</title>
    <style>
        body [
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #f0f0f0;
        ]
        img [
            max-width: 100%;
            max-height: 100%;
        ]
    </style>
</head>
<body>
    <img id="image" src="" alt="Image Viewer">
    <script>
        const imageUrls = {image_urls};


        let currentIndex = 0;

        const imageElement = document.getElementById("image");

        function showNextImage() [
            currentIndex = (currentIndex + 1) % imageUrls.length;
            imageElement.src = imageUrls[currentIndex];
        ]

        imageElement.addEventListener("click", showNextImage);

        // Show the first image initially
        showNextImage();
    </script>
</body>"""


