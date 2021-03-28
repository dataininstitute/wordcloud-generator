from PIL import Image
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import stylecloud
import twcloud
import twint
import re

st.set_option('deprecation.showPyplotGlobalUse', False)


st.sidebar.image("image.gif",use_column_width=True)
#st.image("image.gif",use_column_width=True)

def clean_tweet(tweet):
    """
    Cleans the tweet text of URLs, user tags, hashtags, pictures,
    and smart punctuation.

    Whitespace does not need to be normalized since it is ignored
    anyways when generating the stylecloud.
    """

    pattern = r'http\S+|pic.\S+|@[a-zA-Z0-9_]+|#[a-zA-Z0-9_]+|[‘’“”’–—…]|\xa0'
    return re.sub(pattern, '', tweet)

# fonction pour definir le wordcloud
def cloud( text, max_word, max_font, random,colormap,background_color,gradient_direction,icon,size2,invert_mask,gradient,font,origin,search,limit,color_collection):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',"c'est",
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came',"a","à","â","abord",
    "afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après",
"assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","auquel","aura",
"auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient",
"avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre",
"boum","bravo","brrr","c","ça","car","ce","ceci","cela",
"celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui",
"celui-ci","celui-là","cent","cependant","certain","certaine","certaines",
"certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun",
"chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine"
,"cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","compris","concernant"
,"contre","couic","crac","d","da","dans","de","debout","dedans","dehors","delà","depuis","derrière","des",
"dès","désormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers"
,"devra","différent","différente","différentes","différents","dire","divers","diverse","diverses","dix",
"dix-huit","dixième","dix-neuf","dix-sept","doit","doivent","donc","dont","douze","douzième","dring",
"du","duquel","durant","e","effet","eh","elle","elle-même","elles","elles-mêmes","en","encore",
"entre","envers","environ","es","ès","est","et","etant","étaient","étais","était","étant","etc",
"été","etre","être","eu","euh","eux","eux-mêmes","excepté","f","façon","fais","faisaient","faisant",
"fait","feront","fi","flac","floc","font","g","gens","h","ha","hé","hein","hélas","hem","hep","hi",
"ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","i","il",
"ils","importe","j","je","jusqu","jusque","k","l","la","là","laquelle","las","le","lequel","les","lès",
"lesquelles","lesquels","leur","leurs","longtemps","lorsque","lui","lui-même","m","ma","maint","mais",
"malgré","me","même","mêmes","merci","mes","mien","mienne","miennes","miens","mille","mince","moi","moi-même",
"moins","mon","moyennant","n","na","ne","néanmoins","neuf","neuvième","ni","nombreuses","nombreux","non","nos",
"notre","nôtre","nôtres","nous","nous-mêmes","nul","o","o|","ô","oh","ohé","olé","ollé","on","ont","onze","onzième",
"ore","ou","où","ouf","ouias","oust","ouste","outre","p","paf","pan","par","parmi","partant","particulier",
"particulière","particulièrement","pas","passé","pendant","personne","peu","peut","peuvent","peux","pff",
"pfft","pfut","pif","plein","plouf","plus","plusieurs","plutôt","pouah","pour","pourquoi","premier","première",
"premièrement","près","proche","psitt","puisque","q","qu","quand","quant","quanta","quant-à-soi","quarante",
"quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles",
"quelque","quelques","quelqu'un","quels","qui","quiconque","quinze","quoi","quoique","r","revoici","revoilà",
"rien","s","sa","sacrebleu","sans","sapristi","sauf","se","seize","selon","sept","septième","sera","seront",
"ses","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son",
"sont","sous","stop","suis","suivant","sur","surtout","t","ta","tac","tant","te","té","tel","telle","tellement",
"telles","tels","tenant","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant",
"toujours","tous","tout","toute","toutes","treize","trente","très","trois","troisième","troisièmement","trop",
"tsoin","tsouin","tu","u","un","une","unes","uns","v","va","vais","vas","vé","vers","via","vif","vifs","vingt",
"vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vôtre","vôtres","vous","vous-mêmes","vu",
"w","x","y","z","zut","alors","aucuns","bon","devrait","dos","droite","début","essai","faites","fois","force",
"haut","ici","juste","maintenant","mine","mot","nommés","nouveaux","parce","parole","personnes","pièce",
"plupart","seulement","soyez","sujet","tandis","valeur","voie","voient","état","étions"])



    inv_mask = False
    #gradient = None
    font = font+".ttf"
    
    palette = 'cartocolors.{}.{}'.format(color_collection,colormap)
    
    
    
    if invert_mask == "Yes":
        inv_mask = True
        
    if origin=="text":   
        
        if gradient_direction is not None:
            gradient = gradient_direction
    
            
            stylecloud.gen_stylecloud(text=text,
                              custom_stopwords=stopwords,
            background_color=background_color,
            random_state=random,
            max_words=max_word,
            max_font_size = max_font,
            palette = palette,
            gradient= gradient,
            invert_mask = inv_mask,
            font_path = font,
           # size= size,
            icon_name = 'fas fa-{}'.format(icon))
            
        elif  gradient_direction is None:
            if size2 == 'square':
                size = (512,512)
            if size2 == 'rectangle':
                size = (1024,512)
        
        # generate the style cloud
            stylecloud.gen_stylecloud(text=text,
                              custom_stopwords=stopwords,
            background_color=background_color,
            random_state=random,
            max_words=max_word,
            max_font_size = max_font,
            palette = palette,
            size= size,
            font_path = font,
            invert_mask = inv_mask,
            icon_name = 'fas fa-{}'.format(icon))
        
    
        #showing image
        st.image('stylecloud.png')
        
    #for tweets    
    
    if origin=="tweet":
        if search == "user":
 
            # cleaning the tweet list
            twint.output.tweets_list=[]
         
            if gradient_direction is not None:
                gradient = gradient_direction
        
                
                twcloud.gen_twcloud(username=text,
                                  custom_stopwords=stopwords,
                background_color=background_color,
                random_state=random,
                max_words=max_word,
                max_font_size = max_font,
                palette = palette,
                gradient= gradient,
                invert_mask = inv_mask,
                font_path = font,
                limit = limit,
                icon_name = 'fas fa-{}'.format(icon))
                
            elif  gradient_direction is None:
                if size2 == 'square':
                    size = (512,512)
                if size2 == 'rectangle':
                    size = (1024,512)
            
            # generate the style cloud
                twcloud.gen_twcloud(username=text,
                                  custom_stopwords=stopwords,
                                    background_color=background_color,
                                    random_state=random,
                                    max_words=max_word,
                                    max_font_size = max_font,
                                    palette = palette,
                                    size= size,
                                    font_path = font,
                                    limit = limit,
                                    invert_mask = inv_mask,
                                    icon_name = 'fas fa-{}'.format(icon))
            #st.write(twint.output.tweets_list.values)
           # st.dataframe(twint.output.tweets_list)
            st.image('twcloud.png')
   
        if search == "search":
 
            # cleaning the tweet list
            twint.output.tweets_list=[]
         
            if gradient_direction is not None:
                gradient = gradient_direction
        
                
                twcloud.gen_twcloud(search=text,
                                  custom_stopwords=stopwords,
                background_color=background_color,
                random_state=random,
                max_words=max_word,
                max_font_size = max_font,
                palette = palette,
                gradient= gradient,
                invert_mask = inv_mask,
                font_path = font,
                limit = limit,
               # size= size,
                icon_name = 'fas fa-{}'.format(icon))
                
            elif  gradient_direction is None:
                if size2 == 'square':
                    size = (512,512)
                if size2 == 'rectangle':
                    size = (1024,512)
            
            # generate the style cloud
                twcloud.gen_twcloud(search=text,
                                  custom_stopwords=stopwords,
                                    background_color=background_color,
                                    random_state=random,
                                    max_words=max_word,
                                    max_font_size = max_font,
                                    palette = palette,
                                    limit = limit,
                                    size= size,
                                    font_path = font,
                                    invert_mask = inv_mask,
                                    icon_name = 'fas fa-{}'.format(icon))
            
            #tweets = [clean_tweet(tweet.tweet) for tweet in twint.output.tweets_list]
            #st.dataframe(tweets)
            st.image('twcloud.png')
            
            
            

def main():
    
    st.write("# Generate Awesome Wordcloud !")
    
    max_word = st.sidebar.slider("Max words", 200, 3000, 200)
    max_font = st.sidebar.slider("Max Font Size", 50, 350, 60)
    random = st.sidebar.slider("Random State", 30, 100, 42 )
    
# initialisation de size
    size2 =None
    
    gradient_direction = None
    gradient = st.sidebar.selectbox("Gradient ?",['No','Yes'])
    if gradient == 'Yes':
        gradient_direction = st.sidebar.selectbox("Gradient orientation",["horizontal","vertical"])
    else:
        gradient_direction = None
        size2 = st.sidebar.selectbox("Which size",['square','rectangle'])
    
    
    origin = st.radio("Origin",["text","tweet"])
    if origin == "text":
        text = st.text_area("Copy-Paste some text here...")
    elif origin == "tweet":
        limit = st.slider("Limit of tweets", 60, 3000, 500,step=20)
        search = st.radio('User or search',["user","search"])
        if search == "user":

              text = st.text_input("Enter tweet account")
        elif search == "search":
              text = st.text_input("Enter a search or hashtag")
        
    
    
    
    font = st.sidebar.selectbox("Font",["Staatliches","ArchitectsDaughter","Roboto","PermanentMarker","Pacifico"])
    # ajout de couleur creez fonction 
    color_collection = st.sidebar.selectbox("Color collection ?",["qualitative","diverging","sequential"])
    if color_collection == "qualitative":
        colormap = st.sidebar.selectbox("Palette ?",["Bold_5","Pastel_6","Safe_7","Vivid_8","Prism_6","Antique_5"])
    if color_collection == "diverging":
        colormap = st.sidebar.selectbox("Palette ?",["ArmyRose_5","Earth_5","Fall_5","Geyser_5","TealRose_5","Tropic_5","Temps_5"])
    if color_collection == "sequential":
        colormap = st.sidebar.selectbox("Palette ?",["BluGrn_5","BluYl_5","BrwnYl_5","Burg_5","BurgYl_5","DarkMint_5","Emrld_5","Magenta_5","OrYel_5","PurpOr_5","Sunset_5","SunsetDark_5","TealGrn_5","agGrnYl_5"])
    #background_color=st.sidebar.selectbox("Background Color ?",["white","black"])
    background_color = st.sidebar.color_picker("Background color")
    icon = st.sidebar.selectbox("Icon ?",["flag","at","cloud","smile","thumbs-up","user","bolt","angle-right","angle-double-right","mask","calendar-check"
                                               ,"balance-scale","battery-full","bell","birthday-cake","search","tag","dog","barcode",
                                               "book-reader","chart-line","coffee","comment","comments","tshirt","bullseye"
                                               ,"cube","cubes","expand-arrows-alt","mug-hot","bullhorn","egg","envelope",
                                               "glass-martini","globe-africa","grin","grin-hearts","graduation-cap","laugh"
                                               ,"microphone","paper-plane","lock-open","percent"])
    invert_mask = st.sidebar.selectbox("Invert mask ?",["No","Yes"])
    st.sidebar.write("[By Régis Amon](https://www.linkedin.com/in/r%C3%A9gis-amon-87669665/)")
    st.sidebar.write("[Using the Stylecloud library created by Minimaxir](https://github.com/minimaxir/stylecloud)")
    st.sidebar.write("[Color collection available here](https://jiffyclub.github.io/palettable/cartocolors/)")


    if text is not None:
        if st.button("Generate Wordcloud"):
          
       
            st.write("### Word cloud")
            st.write(cloud(text, max_word, max_font, random,colormap,background_color,gradient_direction,icon,size2,invert_mask,gradient,font,origin,search,limit,color_collection), use_column_width=True)
            st.write("Right click on the image then choose ***Save as*** to download the Wordcloud")
            #st.balloons()
    
if __name__=="__main__":
    main()
