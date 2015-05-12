 stage_0_titles:
        <div class="stage">
        <h1>
            Stage 0: Getting Started with HTML
            </h1>
def generate_information_for_stage0(subtext_title, paragraph): 
   subtext_title = '''
<div class="subtext_title">
    <h3>
    '''+subtext_title
   paragraph='''
    </h3>
 <p>
        ''' + paragraph
</p>
</h3>

full_html_text=subtext_title+paragraph
    return full_html_subtext


def make_HTML(concept):
    subtext = concept[0]
    paragraph = concept[1]
    return generate_information_for_stage0(subtext_title,paragraph)

EXAMPLE_LIST_OF_Subtext = [ ['The Path to the Internet', 'We interact with the internet through our computer and browser. The browser is a program that displays files on the web, intepreting them to show us what we see. The internet is essentially the world's largest computer, pulling files from servers though HTTP from the servers. Servers are essentially large computers that hold the files that make up the internet and sends them though the internet to our computers.'],
                             ['A Basic Understanding of HTML place in the Internet', 'The Web is made up of mainly HTML documents. 
            HTML stands for hypertext markup language and works essentially as the glue for everything else on the internet.
            There are five types of files on the web: <em> plain text, HTML, images, videos, and music </em>. HTML allows for hyperlinks, making the web "web-like"'],
                             ['What makes up HTML?', 'HTML is made up of four elements. What you see is referred to as the text content. How the text content is displayed to you is the mark up. Links to other pages or reference to other documents like images and videos are how it helps the internet. 

            This is well-explained <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48724340"> here </a>.
            </p>
            <p>
              A HTML markup is made up of the name of the tag, the content of the tag, and the end of the tag. This is explained in this <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48723444"> video. </a>']
                              ['Inline Tags','There are two types of tags: <em> inline</em> and <em> block</em>.
                  </p>
              <p>

              Inline tags are just tags that affect the text while block tags group together text that can be altered together, essentially putting them into boxes with height and width. <br>
              Common inline tags change the text so you can put them into italics and bold. How to use the bold tag is in this <a href= "https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48011976/m-48703273"> video.</a>. How to use the italics tag is in this <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48296546/m-48693677"> video </a>
             . 
              <br> 
              Another commonly used inline tag is attributes. This is how I linked all of the videos in this site. You can learn how to make them in this  <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48508417/m-48723411"> video </a>
            .
            <br>
            Having images is just as simple with a little change. Image tags, like the break tag (used to add breaks in the text n the white space on the page) are void tags, meaning they don't need a closing tag.
            Adding images is shown <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-48744041"> here</a>
            . The concept of white space would be hard to explain on this limited text so just watch <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/e-48666064/m-48678767"> this </a>. ']
                               ['Block Tags','Block tags have already been mentioned as different from inline tags. One commonly used block tag is the paragraph tag. This is used to group together text into a block. All of the text under a section heading, before another section heading here has been placed into a paragraph tag.  If you are still confused by the difference, watch <a href="https://www.udacity.com/course/viewer#!/c-ud721/l-3508959201/m-4872343"> this</a>']
                               ['Computers are stupid.','One that should not be forgotten is that the computer is stupid. Only the correct syntax will be understood properly by the computer. And do not feel stupid if you do not remember how to do something in HTML. That's what google is for.']]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(Example_LIST_Subtext)

