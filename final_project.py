Final Project - Word Cloud
For this project, you'll create a "word cloud" from a text by writing a script. This script needs to process the text, remove punctuation, ignore case and words that do not contain all alphabets, count the frequencies, and ignore uninteresting or irrelevant words. A dictionary is the output of the calculate_frequencies function. The wordcloud module will then generate the image from your dictionary.

For the input text of your script, you will need to provide a file that contains text only. For the text itself, you can copy and paste the contents of a website you like. Or you can use a site like Project Gutenberg to find books that are available online. You could see what word clouds you can get from famous books, like a Shakespeare play or a novel by Jane Austen. Save this as a .txt file somewhere on your computer.

Now you will need to upload your input file here so that your script will be able to process it. To do the upload, you will need an uploader widget. Run the following cell to perform all the installs and imports for your word cloud script and uploader widget. It may take a minute for all of this to run and there will be a lot of output messages. But, be patient. Once you get the following final line of output, the code is done executing. Then you can continue on with the rest of the instructions for this notebook.

Enabling notebook extension fileupload/extension...
- Validating: OK

# Here are all the installs and imports you will need for your word cloud script and uploader widget
​
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets
!jupyter nbextension install --py --user fileupload
!jupyter nbextension enable --py fileupload
​
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
Requirement already satisfied: wordcloud in /opt/conda/lib/python3.6/site-packages (1.8.1)
Requirement already satisfied: matplotlib in /opt/conda/lib/python3.6/site-packages (from wordcloud) (3.0.3)
Requirement already satisfied: pillow in /opt/conda/lib/python3.6/site-packages (from wordcloud) (5.4.1)
Requirement already satisfied: numpy>=1.6.1 in /opt/conda/lib/python3.6/site-packages (from wordcloud) (1.15.4)
Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.6/site-packages (from matplotlib->wordcloud) (0.10.0)
Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.6/site-packages (from matplotlib->wordcloud) (1.0.1)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /opt/conda/lib/python3.6/site-packages (from matplotlib->wordcloud) (2.3.1)
Requirement already satisfied: python-dateutil>=2.1 in /opt/conda/lib/python3.6/site-packages (from matplotlib->wordcloud) (2.8.0)
Requirement already satisfied: six in /opt/conda/lib/python3.6/site-packages (from cycler>=0.10->matplotlib->wordcloud) (1.12.0)
Requirement already satisfied: setuptools in /opt/conda/lib/python3.6/site-packages (from kiwisolver>=1.0.1->matplotlib->wordcloud) (40.8.0)
Requirement already satisfied: fileupload in /opt/conda/lib/python3.6/site-packages (0.1.5)
Requirement already satisfied: notebook>=4.2 in /opt/conda/lib/python3.6/site-packages (from fileupload) (5.7.5)
Requirement already satisfied: ipywidgets>=5.1 in /opt/conda/lib/python3.6/site-packages (from fileupload) (7.4.2)
Requirement already satisfied: traitlets>=4.2 in /opt/conda/lib/python3.6/site-packages (from fileupload) (4.3.2)
Requirement already satisfied: ipykernel in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (5.1.0)
Requirement already satisfied: jinja2 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (2.10)
Requirement already satisfied: terminado>=0.8.1 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (0.8.1)
Requirement already satisfied: pyzmq>=17 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (18.0.1)
Requirement already satisfied: nbformat in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (4.4.0)
Requirement already satisfied: jupyter-client>=5.2.0 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (5.2.4)
Requirement already satisfied: ipython-genutils in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (0.2.0)
Requirement already satisfied: tornado<7,>=4.1 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (6.0.2)
Requirement already satisfied: jupyter-core>=4.4.0 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (4.4.0)
Requirement already satisfied: prometheus-client in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (0.6.0)
Requirement already satisfied: Send2Trash in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (1.5.0)
Requirement already satisfied: nbconvert in /opt/conda/lib/python3.6/site-packages (from notebook>=4.2->fileupload) (5.4.1)
Requirement already satisfied: widgetsnbextension~=3.4.0 in /opt/conda/lib/python3.6/site-packages (from ipywidgets>=5.1->fileupload) (3.4.2)
Requirement already satisfied: ipython>=4.0.0; python_version >= "3.3" in /opt/conda/lib/python3.6/site-packages (from ipywidgets>=5.1->fileupload) (7.4.0)
Requirement already satisfied: six in /opt/conda/lib/python3.6/site-packages (from traitlets>=4.2->fileupload) (1.12.0)
Requirement already satisfied: decorator in /opt/conda/lib/python3.6/site-packages (from traitlets>=4.2->fileupload) (4.3.2)
Requirement already satisfied: MarkupSafe>=0.23 in /opt/conda/lib/python3.6/site-packages (from jinja2->notebook>=4.2->fileupload) (1.1.1)
Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /opt/conda/lib/python3.6/site-packages (from nbformat->notebook>=4.2->fileupload) (3.0.1)
Requirement already satisfied: python-dateutil>=2.1 in /opt/conda/lib/python3.6/site-packages (from jupyter-client>=5.2.0->notebook>=4.2->fileupload) (2.8.0)
Requirement already satisfied: mistune>=0.8.1 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (0.8.4)
Requirement already satisfied: pygments in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (2.3.1)
Requirement already satisfied: entrypoints>=0.2.2 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (0.3)
Requirement already satisfied: bleach in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (3.1.0)
Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (1.4.2)
Requirement already satisfied: testpath in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (0.4.2)
Requirement already satisfied: defusedxml in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.2->fileupload) (0.5.0)
Requirement already satisfied: setuptools>=18.5 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (40.8.0)
Requirement already satisfied: jedi>=0.10 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.13.3)
Requirement already satisfied: pickleshare in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.7.5)
Requirement already satisfied: prompt_toolkit<2.1.0,>=2.0.0 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (2.0.9)
Requirement already satisfied: backcall in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.1.0)
Requirement already satisfied: pexpect in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (4.6.0)
Requirement already satisfied: attrs>=17.4.0 in /opt/conda/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=4.2->fileupload) (19.1.0)
Requirement already satisfied: pyrsistent>=0.14.0 in /opt/conda/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat->notebook>=4.2->fileupload) (0.14.11)
Requirement already satisfied: webencodings in /opt/conda/lib/python3.6/site-packages (from bleach->nbconvert->notebook>=4.2->fileupload) (0.5.1)
Requirement already satisfied: parso>=0.3.0 in /opt/conda/lib/python3.6/site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.3.4)
Requirement already satisfied: wcwidth in /opt/conda/lib/python3.6/site-packages (from prompt_toolkit<2.1.0,>=2.0.0->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.1.7)
Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.6/site-packages (from pexpect->ipython>=4.0.0; python_version >= "3.3"->ipywidgets>=5.1->fileupload) (0.6.0)
Requirement already satisfied: ipywidgets in /opt/conda/lib/python3.6/site-packages (7.4.2)
Requirement already satisfied: traitlets>=4.3.1 in /opt/conda/lib/python3.6/site-packages (from ipywidgets) (4.3.2)
Requirement already satisfied: ipython>=4.0.0; python_version >= "3.3" in /opt/conda/lib/python3.6/site-packages (from ipywidgets) (7.4.0)
Requirement already satisfied: widgetsnbextension~=3.4.0 in /opt/conda/lib/python3.6/site-packages (from ipywidgets) (3.4.2)
Requirement already satisfied: nbformat>=4.2.0 in /opt/conda/lib/python3.6/site-packages (from ipywidgets) (4.4.0)
Requirement already satisfied: ipykernel>=4.5.1 in /opt/conda/lib/python3.6/site-packages (from ipywidgets) (5.1.0)
Requirement already satisfied: ipython_genutils in /opt/conda/lib/python3.6/site-packages (from traitlets>=4.3.1->ipywidgets) (0.2.0)
Requirement already satisfied: six in /opt/conda/lib/python3.6/site-packages (from traitlets>=4.3.1->ipywidgets) (1.12.0)
Requirement already satisfied: decorator in /opt/conda/lib/python3.6/site-packages (from traitlets>=4.3.1->ipywidgets) (4.3.2)
Requirement already satisfied: setuptools>=18.5 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (40.8.0)
Requirement already satisfied: jedi>=0.10 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.13.3)
Requirement already satisfied: pickleshare in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.7.5)
Requirement already satisfied: prompt_toolkit<2.1.0,>=2.0.0 in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (2.0.9)
Requirement already satisfied: pygments in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (2.3.1)
Requirement already satisfied: backcall in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.1.0)
Requirement already satisfied: pexpect in /opt/conda/lib/python3.6/site-packages (from ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (4.6.0)
Requirement already satisfied: notebook>=4.4.1 in /opt/conda/lib/python3.6/site-packages (from widgetsnbextension~=3.4.0->ipywidgets) (5.7.5)
Requirement already satisfied: jsonschema!=2.5.0,>=2.4 in /opt/conda/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets) (3.0.1)
Requirement already satisfied: jupyter_core in /opt/conda/lib/python3.6/site-packages (from nbformat>=4.2.0->ipywidgets) (4.4.0)
Requirement already satisfied: jupyter-client in /opt/conda/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets) (5.2.4)
Requirement already satisfied: tornado>=4.2 in /opt/conda/lib/python3.6/site-packages (from ipykernel>=4.5.1->ipywidgets) (6.0.2)
Requirement already satisfied: parso>=0.3.0 in /opt/conda/lib/python3.6/site-packages (from jedi>=0.10->ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.3.4)
Requirement already satisfied: wcwidth in /opt/conda/lib/python3.6/site-packages (from prompt_toolkit<2.1.0,>=2.0.0->ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.1.7)
Requirement already satisfied: ptyprocess>=0.5 in /opt/conda/lib/python3.6/site-packages (from pexpect->ipython>=4.0.0; python_version >= "3.3"->ipywidgets) (0.6.0)
Requirement already satisfied: nbconvert in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (5.4.1)
Requirement already satisfied: terminado>=0.8.1 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.8.1)
Requirement already satisfied: pyzmq>=17 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (18.0.1)
Requirement already satisfied: jinja2 in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (2.10)
Requirement already satisfied: prometheus-client in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.6.0)
Requirement already satisfied: Send2Trash in /opt/conda/lib/python3.6/site-packages (from notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (1.5.0)
Requirement already satisfied: attrs>=17.4.0 in /opt/conda/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets) (19.1.0)
Requirement already satisfied: pyrsistent>=0.14.0 in /opt/conda/lib/python3.6/site-packages (from jsonschema!=2.5.0,>=2.4->nbformat>=4.2.0->ipywidgets) (0.14.11)
Requirement already satisfied: python-dateutil>=2.1 in /opt/conda/lib/python3.6/site-packages (from jupyter-client->ipykernel>=4.5.1->ipywidgets) (2.8.0)
Requirement already satisfied: mistune>=0.8.1 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.8.4)
Requirement already satisfied: entrypoints>=0.2.2 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.3)
Requirement already satisfied: bleach in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (3.1.0)
Requirement already satisfied: pandocfilters>=1.4.1 in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (1.4.2)
Requirement already satisfied: testpath in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.4.2)
Requirement already satisfied: defusedxml in /opt/conda/lib/python3.6/site-packages (from nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.5.0)
Requirement already satisfied: MarkupSafe>=0.23 in /opt/conda/lib/python3.6/site-packages (from jinja2->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (1.1.1)
Requirement already satisfied: webencodings in /opt/conda/lib/python3.6/site-packages (from bleach->nbconvert->notebook>=4.4.1->widgetsnbextension~=3.4.0->ipywidgets) (0.5.1)
Installing /opt/conda/lib/python3.6/site-packages/fileupload/static -> fileupload
Up to date: /home/jovyan/.local/share/jupyter/nbextensions/fileupload/extension.js
Up to date: /home/jovyan/.local/share/jupyter/nbextensions/fileupload/widget.js
Up to date: /home/jovyan/.local/share/jupyter/nbextensions/fileupload/fileupload/widget.js
- Validating: OK

    To initialize this nbextension in the browser every time the notebook (or other app) loads:
    
          jupyter nbextension enable fileupload --user --py
    
Enabling notebook extension fileupload/extension...
      - Validating: OK
Whew! That was a lot. All of the installs and imports for your word cloud script and uploader widget have been completed.

IMPORTANT! If this was your first time running the above cell containing the installs and imports, you will need save this notebook now. Then under the File menu above, select Close and Halt. When the notebook has completely shut down, reopen it. This is the only way the necessary changes will take affect.

To upload your text file, run the following cell that contains all the code for a custom uploader widget. Once you run this cell, a "Browse" button should appear below it. Click this button and navigate the window to locate your saved text file.

# This is the uploader widget
​
def _upload():
​
    _upload_widget = fileupload.FileUploadWidget()
​
    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()
​
    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)
​
_upload()
Uploaded `input_file.txt` (1.70 kB)
The uploader widget saved the contents of your uploaded file into a string object named file_contents that your word cloud script can process. This was a lot of preliminary work, but you are now ready to begin your script.

Write a function in the cell below that iterates through the words in file_contents, removes punctuation, and counts the frequency of each word. Oh, and be sure to make it ignore word case, words that do not contain all alphabets and boring words like "and" or "the". Then use it in the generate_from_frequencies function to generate your very own word cloud!

Hint: Try storing the results of your iteration in a dictionary before passing them into wordcloud via the generate_from_frequencies function.

,
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a","in", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    result = {}
    clean_text=""
    for word in file_contents:
        if word not in punctuations:
            clean_text+=word
    words=clean_text.split()
    clean_words=[]
    for word in words:
        if word.isalpha():
            if word not in uninteresting_words:
                clean_words.append(word)
    for clean_word in clean_words:
        if clean_word not in result:
            result[clean_word]=1
        else:
            result[clean_word]+=1
    print(result)
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(result)
    return cloud.to_array()
If you have done everything correctly, your word cloud image should appear after running the cell below. Fingers crossed!

# Display your wordcloud image
​
myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
{'completed': 1, 'basic': 1, 'Python': 7, 'programming': 2, 'tutorial': 1, 'finished': 1, 'Al': 2, 'best': 3, 'selling': 1, 'Automate': 1, 'Boring': 1, 'Stuff': 3, 'next': 1, 'step': 1, 'toward': 1, 'becoming': 1, 'capable': 1, 'confident': 1, 'software': 2, 'developerWelcome': 1, 'Beyond': 2, 'Basic': 2, 'More': 1, 'than': 1, 'mere': 1, 'collection': 1, 'advanced': 2, 'syntax': 1, 'masterful': 1, 'tips': 1, 'for': 2, 'writing': 1, 'clean': 1, 'code': 4, 'learn': 3, 'advance': 1, 'skills': 3, 'using': 1, 'command': 1, 'line': 1, 'other': 1, 'professional': 2, 'tools': 1, 'like': 1, 'formatters': 1, 'type': 1, 'checkers': 1, 'linters': 1, 'version': 1, 'control': 1, 'Sweigart': 1, 'takes': 1, 'through': 1, 'practices': 2, 'setting': 1, 'up': 1, 'development': 1, 'environment': 1, 'naming': 1, 'variables': 1, 'improving': 1, 'readability': 1, 'then': 1, 'tackles': 1, 'documentation': 1, 'organization': 1, 'performance': 1, 'measurement': 1, 'well': 1, 'objectoriented': 1, 'design': 1, 'BigO': 1, 'algorithm': 1, 'analysis': 1, 'commonly': 1, 'used': 1, 'coding': 1, 'interviews': 1, 'The': 1, 'boost': 1, 'ability': 1, 'language': 1, 'Toward': 1, 'end': 1, 'book': 2, 'read': 1, 'detailed': 1, 'sourcecode': 1, 'breakdown': 2, 'two': 1, 'classic': 1, 'commandline': 1, 'games': 1, 'Tower': 1, 'Hanoi': 1, 'logic': 1, 'puzzle': 1, 'FourinaRow': 1, 'twoplayer': 1, 'tiledropping': 1, 'game': 1, 'follows': 1, 'test': 1, 'implementing': 1, 'program': 1, 'yourself': 1, 'Of': 1, 'course': 1, 'single': 1, 'make': 2, 'developer': 1, 'But': 1, 'get': 1, 'further': 1, 'down': 1, 'path': 1, 'better': 1, 'programmer': 1, 'process': 1, 'write': 1, 'readable': 1, 'easy': 1, 'debug': 1, 'perfectly': 1, 'Pythonic': 1, 'My': 1, 'early': 1, 'programs': 1, 'work': 1, 'could': 1, 'improved': 1, 'massively': 1, 'writes': 1, 'about': 1, 'small': 1, 'goldmine': 1, 'knowledge': 1, 'beginners': 1, 'intermediates': 1, 'probably': 1, 'even': 1, 'programmers': 1, 'benefit': 1}

If your word cloud image did not appear, go back and rework your calculate_frequencies function until you get the desired output. Definitely check that you passed your frequecy count dictionary into the generate_from_frequencies function of wordcloud. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!

