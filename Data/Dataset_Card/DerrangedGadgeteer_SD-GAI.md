A dataset of AI-generated images, selected by the community, for fine tuning Stable Diffusion 1.5 and/or Stable Diffusion 2.0 on particular desired artstyles, 
WITHOUT using any images owned by major media companies, nor images by artists who are uncomfortable with their works being used to train AI.

What to submit: Your own AI-generated Images paired with a text description of their subject matter.  Filename can be whatever, but both should have the same filename.
     If you're a conventional digital artist and want to contribute, include solid documentation of your permission for use in the text file.  (see rules below)

Format: Images as .jpeg or .png: 512x512 or preferably 768x768
        Text files as .txt: with a short list of one-word descriptions about what's in the image. (Not the prompts, describe it in your own words)
        
Where to submit: Select the directory most descriptive of the "style" you're going for.  look at a few already-submitted images to make sure it fits. 
     If youre piece is a different style, something new, prepare at least 4 similarly styled images, and a creative style name, and push a new directory too.

What is going to be done with the images: Once the technical issues get ironed out I will use Hugging Face Diffuser's Dreambooth example script to train the 
     Stable Diffusion 2.0 model on the 768px images once we have accumulated at least 50 images in a particular style.  I will document the setup, process, and make the 
     resultant model available here for download.  Once (if) we accumulate on the order of 1000 images, I will begin work on a natively fine-tuned model, incorporating the
     provided text-image pairs.  
     Until that point, all images and text descriptions will be available here.  If you wish to use the datasets for your own training projects at any point, the data is 
     available, and for the purposes of AI training it is free to use.  (Subject to license and Hugging Face T.O.S.)
     I will not be taking submissions of trained models or other code or utilities.

Basic Rules:
The first rule of GAI: No images from human artists without the artist's explicit permission. 
     -In order to document the artist's permission, include a text file with a link to a public statement (like a post on social media for instance) 
          granting permission for use of that image, or a set of images including the image in question.  
     -The link should: 1) Be independently verifiable as actually being from the artist in question.
                      2) Include an unambiguous reference to the image in question, or an image set that clearly includes the image in question.
                      3) Include permission to use the images in question for training AI
     -It is appreciated if members of the community can help reverse-image-search images submitted to the dataset, and help police content.  I am but one goofball, and I 
          will keep on top of submitted images as best I can, but I don't claim to be magical, omnicient, or even competent at content moderation.   

The second rule of GAI: Use creative, and descriptive names to artstyles instead of artist's names, pen names, trade names, or trademarks from media companies.
     -This is part of the point of this dataset, to teach the wider art community that AI doesn't just copy existing work.  And also to provide a hedge against possibly
          litigous activist actions, and future changes to the law.
     -Users who use AI ethically aren't attempting to counterfeit, displace, or impersonate existing artists.  We want images that have a certain "look" to them, or simply
          more visually appealing.  So instead of prompting with artist names or existing properties, specify the actual image you want to see, and let the AI do the rest.

The third rule of GAI: NSFW content is permitted, but it is to be kept seperate.  Illegal content like CSAM and "Lightning Rod" content like hate speech will not be 
      permitted.  Neither will anything else that violates Hugging Face's T.O.s.
      -What is NSFW? Using Unites States ESRB "Teen" rating, MPAA "PG-13", and typical mass-market social media moderation guidelines are the primary benchmark for what is
           and isn't NSFW.  If an image straddles the line, discuss.  The primary purpose for separating this content is for appearances.  If something is a bad look for
           the main dataset, it will get moved.
      -What is Illegal content? Primarily CSAM, CP, adult material including minors, anything that could get the feds to show up.  AI's are not people, pictures are not 
           people, but argue about it somewhere else.  This also includes confidential information, medical imaging, or, per rule #1, unauthorized copyrighted material.
      -What is Lightning Rod content? Hate speech, discriminatory content aimed at groups of people based on heritage, nationality, sex, gender identity, race, ethnicity, 
           religion, etc.  As well as things like deliberate shock images with no artistic merit.  If an image straddles the line, discuss.

The zero'th rule of GAI: The objective is to build models for Stable Diffusion that work AS WELL or BETTER than models trained on copyrighted material. While using only 
     AI generated, or volunteered input.  Anything that doesn't serve that goal is subject to moderation and removal.  Don't try to "sneak" copyrighted material in. 
          Don't try to sneak in illegal, shock, or hateful material.  Don't be a problem.  I can appreciate a good trolling, but we're going to stay on topic here.

          Have fun, and thanks to anyone who wants to contribute! 
          -DerrangedGadgeteer