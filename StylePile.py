
# A simple helper script for AUTOMATIC1111/stable-diffusion-webui.
# Enter your keywords and let the selections here help you determine the look.
# https://replicate.com/methexis-inc/img2prompt has been an incredible help for improving the prompts.

import modules.scripts as scripts
import gradio as gr

from modules.processing import process_images, Processed

ResultBefore = {
    "Not set":"", 
    "Photography":"A photograph of  ", 
    "Digital art":"Digital art of  ", 
    "3D Rendering":"3D rendering of ", 
    "Painting":"A painting of ", 
    "Sketch":"A sketch of ", 
    "Classic Comics":"Comic book art of ", 
    "Modern Comics":"Comic book art of ",
    "Manga":"Manga comic art of ",
    "Vector art":"A vector image of "
}

ResultType = {
    "Not set":"", 
    "Photography":", ((analog photo)), (detailed), ZEISS, studio quality, 8k, 4k, uhd", 
    "Digital art":", ((digital painting)), trending on artstation, trending on cgsociety, corel painter, 8k, 4k, uhd", 
    "3D Rendering":", ((render)), (global illumination), RayTracing, hyper realism, high quality, trending on cgsociety, trending on artstation, 8k, 4k, uhd", 
    "Painting":", ((canvas, fine art)), detailed", 
    "Sketch":", ((drawing)), (pencil art), (pen), graphite, ink, high contrast, 2 bit", 
    "Classic Comics":", ((storybook drawing)), ((graphic novel)), (line art, ink), Jack Kirby, Will Eisner, Frank Miller, Steve Ditko, Brian Bolland, John Romita, Neal Adams", 
    "Modern Comics":", ((digital comic)), Jim Lee, Todd McFarlane, Cory Walker, ryan ottley",
    "Manga":", ((danbooru)), ((zerochan art)), Blame!, JoJo's Bizarre Adventure, Pure Trance, Phoenix, Kokou no Hito, Battle Angel Alita, Dorohedoro, Horror,Collector, Homunculus",
    "Vector art":"((low detail)), flat shading, sharp, hd, 2 bit"  #,featured on dribble, behance contest winner"
}

ResultTypeNegatives = {
    "Not set":"", 
    "Photography":", ((painting)), ((drawing)), ((sketch)), ((camera)), ((rendering))", 
    "Digital art":", blurry, ((photography)), ui, windows, cursor", 
    "3D Rendering":", ((painting)), (photography), low detail, ui, windows, cursor", 
    "Painting":", (((frame))), rendering, photography, brush, pencil", 
    "Sketch":", (photography), frame, rendering, painting, pencil, brush", 
    "Classic Comics":", (photography), rendering, blurry", 
    "Modern Comics":", (photography), rendering, blurry", 
    "Manga":", (photography), rendering, blurry",
    "Vector art":"(((text))), ((photography)), ((painting)), titles, ui, windows, cursor"
}

ResultStyle = {
    "Not set":"", 
    "Realism":", (((realistic))), ((realism)), (real)", 
    "Photorealism":", (((photorealistic))), ((detailed)), transfer", 
    "Hyperrealism":", (((hyperrealism))), ((superrealism)), (highly detailed), vivid", 
    "Surrealism":", (((surrealism))), ((dream)), (juxtaposition), irrational", 
    "Modern Art":", (((modern art))), ((rhytm)), (balance), proportion", 
    "Painterly":", (((painterly))),(large brushes),(emphasis)", 
    "Abstract":", ((abstract art)), Art Deco, Art Nouveau, Avant-garde, Baroque, Bauhaus", 
    "Pop Art":", (((pop art))), roy lichtenstein, claes oldenburg, james rosenquist, andy warhol, wayne thiebaud, lines, shapes, space", 
    "Impressionist":", (((impressionist art))), (Gestalt brushstroke), pure colors, composition", 
    "Cubism":", (((cubism))), lines, primary colors", 
    "Fantasy":", (((fantasy art))), ((mythological)), supernatural, magical"
}

ResultColors = {
    "Not set":"", 
    "Chaotic":", ((chaotic colors))",
    "Colorful":", ((colorful))", 
    "Vivid":" ((vivid)), ((vibrant))",
    "Muted colors":", ((muted colors))", 
    "Desaturated":", ((desaturated))", 
    "Grayscale":", ((grayscale, monochrome))", 
    "Black and white":", ((black and white, 2 colors))", 
    "Complementary":", ((complementary colors))", 
    "Non-complementary":", ((non-complementary colors))"
}

ImageView = {
    "Not set":"", 
    "Fisheye lens":", ((photo taken with fisheye lens))", 
    "Ultra-wide":", ((photo taken with ultrawide lens))", 
    "Wide-angle":", ((photo taken with wide angle lens))", 
    "Portrait lens":", ((portrait)), Nikon 50mm f/1.8, Sigma f/1.4, Canon EF 85mm", 
    "Telephoto lens":", ((photo taken with telephoto lens))", 
    "Super telephoto":", ((photo taken with a super telephoto lens))", 
    "Macro lens":", ((macro)),",
    "Close up":"(close up), worms-eye view",
    "Birds-eye view":"(birds-eye view), distant"
}

ImageStyle = {
    "No focus":"", 

    "Portraits (tick Restore faces above for best results)":", dribble, precisionism, associated press photo, award-winning",

    "Feminine and extra attractive (tick Restore faces above for best results)":", ((Feminine)), (effeminate), attractive, pretty, handsome, hypnotic, beautiful, elegant, sensual, enchanting, precisionism, angelic photograph, associated press photo, award-winning",

    "Masculine and extra attractive (tick Restore faces above for best results)":", ((Masculine)), (manly),  attractive, pretty, handsome, fit, precisionism, associated press photo, award-winning",

    "Monsters":", monster, ugly, surgery, evisceration, morbid, cut, open, rotten, mutilated, deformed, disfigured, malformed, missing limbs, extra limbs, bloody, slimy, goo, Richard Estes, Audrey Flack, Ralph Goings, Robert Bechtle, Tomasz Alen Kopera, H.R.Giger, Joel Boucquemont, artstation, thematic background",

    "Robots":", robot, cyborg, robotic enhancements, electronics, mechanical elements, screws, mainboard, tim hildebrandt, wayne barlowe, bruce pennington, donato giancola, larry elmore, oil on canvas, masterpiece, artstation, pixiv, thematic background",
    
    "Retrofuturistic":", Clarence Holbrook Carter, Ed Emshwiller, cgsociety, retrofuturism, dystopian art, future tech, Fallout, chiaroscuro",

    "Landscapes":", naturalism, land art, regionalism, shutterstock contest winner, trending on unsplash, featured on flickr"
}

ImageStyleNegatives = {
    "No focus":"", 

    "Portraits (tick Restore faces above for best results)":", mutilated, disfigured, unnatural, bad anatomy, morbid, too many fingers, deformed palm,  deformed arm, deformed limbs, extra limbs, missing limbs, unnatural pose", 

    "Feminine and extra attractive (tick Restore faces above for best results)":", ((ugly)), (mutilated), disfigured, unnatural, bad anatomy, morbid, too many fingers, deformed palm, deformed arm, deformed limbs, extra limbs, missing limbs, unnatural pose",

    "Masculine and extra attractive (tick Restore faces above for best results)":", ((ugly)), (mutilated), disfigured, unnatural, bad anatomy, morbid, too many fingers, deformed palm, deformed arm, deformed limbs, extra limbs, missing limbs, unnatural pose",

    "Monsters":", (attractive), pretty, smooth,cartoon,pixar,human, low quality, worst quality",

    "Robots":", cartoon, low quality, worst quality",
    
    "Retrofuturistic":", extra limbs, malformed limbs, modern, low quality, worst quality",

    "Landscapes":"((hdr)), ((terragen)), ((rendering)), (high contrast)"
}

AlwaysBad = ",(((cropped))), (((watermark))), ((logo)), ((barcode)), ((UI)), ((signature)), ((text)), ((label)), ((error)), ((title)), stickers, markings, speech bubbles, lines, cropped, lowres, low quality, artifacts"

class Script(scripts.Script):

    def title(self):
        return "StylePile"

    def ui(self, is_img2img):

        with gr.Blocks(title="StylePile"):
            with gr.Row(variant='panel'):
                poImageStyle = gr.Dropdown(list(ImageStyle.keys()),label = "Focus on:", value="No focus")
            with gr.Row(variant='panel'):
                poTempText = gr.Textbox(label = "Hints",max_lines=4,placeholder = 
                "Hello, StylePile here.\nUntil some weird bug gets fixed you will see this even if the script itself is not active. Meanwhile, some hints to take your artwork to new heights:\nUse the 'Focus on' dropdown to select complex presets. Toggle selections below (with or without Focus) to affect your results. Mix and match to get some interesting results. \nAnd some general Stable Diffusion tips that will take your designs to next level:\nYou can add parenthesis to make parts of the prompt stronger. So (((cute))) kitten will make it extra cute (try it out). This is alsow important if a style is affecting your original prompt too much. Make that prompt stronger by adding parenthesis around it, like this: ((promt)).\nYou can type promts like [A|B] to sequentially use terms one after another on each step. So, like [cat|dog] will produce a hybrid catdog. And [A:B:0.4] to switch to other terms after the first one has been active for a certain percentage of steps. So [cat:dog:0.4] will build a cat 40% of the time and then start turning it into a dog. This needs more steps to work properly.")
            with gr.Row(variant='panel'):
                poResultType = gr.Radio(list(ResultType.keys()), label="Image type", value="Not set")
                poResultStyle = gr.Radio(list(ResultStyle.keys()), label="Visual style", value="Not set")
                poResultColors = gr.Radio(list(ResultColors.keys()), label="Colors", value="Not set")
                poImageView = gr.Radio(list(ImageView.keys()), label="View", value="Not set")
        return [poResultType, poResultStyle, poResultColors, poImageView, poImageStyle]

    def run(self, p, poResultType, poResultStyle, poResultColors, poImageView, poImageStyle):

        p.prompt = ResultBefore[poResultType] + p.prompt + ResultType[poResultType] + ResultStyle[poResultStyle] + ResultColors[poResultColors] + ImageView[poImageView] + ImageStyle[poImageStyle]
        p.negative_prompt += ResultTypeNegatives[poResultType] + ImageStyleNegatives[poImageStyle] + AlwaysBad

        proc = process_images(p)
        return proc
