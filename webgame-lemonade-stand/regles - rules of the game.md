**1 - Gestion generale du stand**
***Chaque jour, avant que la journée commmence, vous devez faire le suivant:***
- Dans le menu "Prix du Menu" vous devez choisir le prix de chaque item, sachant que le plus haut que le prix est, le plus bas que le multiplieur d'argent general sera. (*Il y en a une chance qu'un ingredient aura un bonus de 35% pur ce jour*) (**voir infos mathematiques**)
- Si vous avez suffisament d'argent; achetez des ameliorations (permanentes) dans la section "Améliorations" et/ou une publicite (pour 5 jour) qui donne un bonus appliquer au multiplieur general.
- Finalement, dans le menu "stock" vous achetez les differents ingredients sachant que le plus que vous en achetez, le plus que le prix d'un stock devient cher, et si vous en achetez pas, il baissera. **(voir mathematiques pour + d'infos)**
- Apres avoir tout achetez et gérer, vous appuyez sur "confirmer les parametres" et puis vous commencer votre journée, une meteo entre [neige,tempete,pluie,nuage,soleil] generée aléatoirement affectera le multiplieur generale causant en consequence une baisse ou hausse du prix de vente de produits.
- Si vous n'avez aucun stock vous perderait 2% de votre argent en cause de dissatisfaction de client. Le jeu termine si vous n'avez pas de stock et pas suffisamment d'argent pour en acheter.
- D'apres ces informations, vous pouvez construire votre strategie pour efficacement gérer votre stand et votre finances. Boonne chance!

**2 - Les mathematiques du programme (multiplieurs, achats, bonus, etc)**
- A coté de votre argent, il y en a un multiplieur qui sera appliquer sur le prix de vente des produits, il consiste du multiplieur de meteo mulitplié par le multiplier de publicités (bonus). **(Voir infos sur ces deux par suite)**
- Le multiplieur de meteo sera initialiser aléatoirement par le meteo : neige:0.65;tempete:0.75;pluie:0.85;nuage:1;soleil:1.15
- Ce multiplieur peu baisser d'avantage en corrélation avec la valeur du prix que vous choisissez des ingrédients, le plus haut que leur prix est, le plus bas que sera le multiplieur. Voici l'image de la variation: <br/>
<img width="409" alt="image" src="https://github.com/michaelalhouwayek/lemonadestand/assets/156347349/8978b8b2-523e-4458-8188-d33ae21f2cf7"> <br/>
- Le multiplieur de publicité sera appliqué pour 5 jours sur le multiplieur globale (meteo*publicité), il peut etre de 1.10,1.25,1.50 (voir jeu)
- De plus, un autre multiplieur existant est celui de l'ingredient du jour; chaque jour il y en a une chance de 50% qu'un ingredient est choisi comme "ingredient du jour", son prix a la vente sera donc augmenté de 35% (x1.35 le prix que vous choisissez). Ce multiplieur n'est pas lié au multiplieur global.
- La formule utilisée a la vente d'un produit est prix_choisi x multiplieur_ingredient x multiplieur_globale
- Le nombre de clients qui apparaitront est proportionel a la meteo, le pire qu'elle est, le moins que les clients apparaitra (formule qui fait un calcul aleatoire du probabilité), et aussi le multiplieur globale baissera, donc il y a un aspect de chance. C'est par la que l'amelioration de prevision de meteo sera utile, vous pourrez décider préalablement comment vous voulez variez vos prix et stock.
- Finalement, le prix des stocks varie de la facon suivante: Si vous en achetez aucun, elle baisse ; si vous en achetez 1 ou 2, elle reste la meme; et si vous en achetez plus que 2, pour chaque 3 ingredients additionels, le prix augmentera. > Elle hausse de 60% du prix initital visible au debut du jeu et elle baisse de 10% de sa valeure actuelle.
