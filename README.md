# Best Image App

This app will return the **best image\*** out of a bunch of images \
\* best image - The image with the biggest most popular face in the images

# To Run Locally

Run in the command line

> docker build -t best_image_app . \
> docker run -d -p 80:80 best_image_app

# Use

Example: with a GET request:

[http://127.0.0.1/best_image/best_face_image?imgs=https://usatftw.files.wordpress.com/2020/04/jordan-3.jpg,https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg,https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg,https://image-cdn.essentiallysports.com/wp-content/uploads/20200420111658/SP-MJ.jpeg](http://127.0.0.1/best_image/best_face_image?imgs=https://usatftw.files.wordpress.com/2020/04/jordan-3.jpg,https://upload.wikimedia.org/wikipedia/commons/a/ae/Michael_Jordan_in_2014.jpg,https://gmsrp.cachefly.net/images/20/04/19/5e385e6a1784ccc718da9d3605fdad79/320.jpg,https://image-cdn.essentiallysports.com/wp-content/uploads/20200420111658/SP-MJ.jpeg)
