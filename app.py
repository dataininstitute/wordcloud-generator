from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(
     page_title="Wordcloud generator",
     page_icon="🚀",
     layout="wide",
     initial_sidebar_state="expanded" )

st.sidebar.image("image.png")

# fonction pour definir le wordcloud
def cloud(image, text, max_word, max_font, random,colormap,background_color):
    stopwords = set(STOPWORDS)
    stopwords.update(['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
    'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
    'put', 'seem', 'asked', 'made', 'half', 'much',
    'certainly', 'might', 'came',"a","à","â","abord",
    "afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après",
"assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","auquel","aura",
"auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient",
"avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre",
"boum","bravo","brrr","c","ça","car","ce","ceci","cela",
"celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent",
"cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci",
"ceux-là","chacun","chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine"
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


    wc = WordCloud(background_color=background_color, colormap= colormap, max_words=max_word, mask=image,
                stopwords=stopwords, max_font_size=max_font, random_state=random)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
   # image_colors = ImageColorGenerator(image)

    # show
    plt.figure(figsize=(100,100))
    fig, axes = plt.subplots(1,2, gridspec_kw={'width_ratios': [3, 2]})
    #fig, axes = plt.subplots(1,1)
    axes[0].imshow(wc, interpolation="bilinear")
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
   # axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    #axes[1].imshow(image, cmap=plt.cm.gray, interpolation="bilinear")
    for ax in axes:
        ax.set_axis_off()
    
    st.pyplot()
    
   


def main():
    st.write("# Synthèse de texte avec un WordCloud")
    st.write("[By Régis Amon](https://www.linkedin.com/in/r%C3%A9gis-amon-87669665/)")
    max_word = st.sidebar.slider("Max words", 200, 3000, 200)
    max_font = st.sidebar.slider("Max Font Size", 50, 350, 60)
    random = st.sidebar.slider("Random State", 30, 100, 42 )
    image = st.file_uploader("1. Choisir une image (de préférence une silouhette)")
    text = st.text_area("2. Copiez-collez votre texte ci-dessous...")
    # ajout de couleur
    colormap = st.sidebar.selectbox("Choisir le jeu de couleur",["viridis", "plasma", "inferno", "magma",
                                                          "cividis",'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper'])
    background_color=st.sidebar.selectbox("Quelle couleur de fond ?",["white","black"])
    if image and text is not None:
        if st.button("Générer Wordcloud"):
            #st.write("### Original image")
            image = np.array(Image.open(image))
            #st.image(image, width=100, use_column_width=True)
       
            st.write("### Word cloud")
            st.write(cloud(image, text, max_word, max_font, random,colormap,background_color), use_column_width=True)

    
if __name__=="__main__":
    main()
