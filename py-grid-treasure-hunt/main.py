from random import randint
tour_dattaque = 1
jeu_terminer = False
assistance = False

class personnage():
    def __init__(self,NOM = "heros",PDV = 100, Position = [0,0],PA = (3,4),PD = 1): # heros a 3 attaque 1 defense, mais peut obtenir plus
        self.nom = NOM
        self.pdv = PDV
        self.position = Position
        self.armure = 0 # NOT MERGED WITH PA PD SO THEY CAN BE INDIVIDUALLY TRACKED AND MODIFIED
        self.arme = 0
        self.pa = PA
        self.pd = PD
        
        if not isinstance(self,Monstre):
            if (input("Voulez vous choisir les statistiques de base de votre joueur? (O/N)")).upper() == "O":
                    
                while True:
                    self.pdv = input("[PDV] Choisissez les points de vie de votre joueur (nombre entier > 0; DEFAUT = 100)")
                    try:
                        self.pdv = int(self.pdv)
                        if self.pdv <= 0:
                            print("La valeur choisit doit etre plus grande que 0")
                            while self.pdv <= 0:
                                try:
                                    self.pdv = int(input("Choisissez les points de vie de votre joueur. (nombre entier > 0"))
                                    if self.pdv > 0:
                                        break
                                except:
                                    print("Votre valeur n'est pas un nombre entier ou n'est pas plus grande que 0")
                        break
                    except:
                        print("La valeur que vous avez donner n'est pas un nombre entier, ressayer")
                
                inp = input("[PA] Voulez vous que la valeur de votre PA soit une liste (range) ou un nombre entier? (L/N)")
                while inp not in ["n","N","L","l"]:
                    inp = input("Vous n'avez pas choisis une lettre, ressayer!")
                if inp in ["L","l"]:
                    while True:
                        try:
                            inp = input("[PA] Choisissez les valeurs de votre PA - format: 'X,Y' ; X et Y entiers positifs avec X < Y")
                            self.pa = str.split(inp,",")

                            self.pa[0] = int(self.pa[0])
                            self.pa[1] = int(self.pa[1])
                            
                            if (self.pa[0] < 0 or self.pa[1] < 0) or (self.pa[0] > self.pa[1]):
                                print("Il y a une erreur dans votre format, ressayer.")
                            else:
                                break
                        except:
                            print("Il y a une erreur dans votre format, ressayer.")
                        
                elif inp in ["N","n"]:
                    while True:
                        self.pa = input("[PA] Choisissez les points d'attaque de votre joueur (nombre entier)")
                        try:
                            self.pa = int(self.pa)
                            if self.pa < 0:
                                print("Votre PA est plus petit que 0, ressayer")
                                while self.pa < 0:
                                    try:
                                        self.pa = int(input("Choisissez une valeur pour votre PA qui est au moins 0 et un entier."))
                                        if self.pa > 0:
                                            break
                                    except:
                                        print("La valeur est plus petite que 0, ressayer.")
                            break
                        except:
                            print("La valeure donnee n'est pas un entier")
                      
                while True:
                    self.pd = input("[PD] Choisissez les points de defense de votre joueur (nombre entier ; DEFAUT = 1)")
                    try:
                        self.pd = int(self.pd)
                        if self.pd < 0:
                            print("Votre PD est plus petit que 0, ressayer")
                            while self.pd < 0:
                                try:
                                    self.pd = int(input("Choisissez une valeur pour votre PD qui est au moins 0 et un entier."))
                                    if self.pd > 0:
                                        break
                                except:
                                    print("La valeur est plus petit que 0, ressayer.")
                        break
                    except:
                        print("La valeur n'est pas un nombre entier")
                      
            self.printStats("Votre joueur commence avec les statistiques")
            print("###########################")
    
    def printStats(self,msg="Vos statistiques jusqu'a là sont"):
        if isinstance(self.pa,int):
            print(f"[STATS] {msg}:","PDV:",self.pdv,"| PA + Arme:",(self.pa+self.arme),f"(+{self.arme})","| PD + Armure:",(self.pd+self.armure),f"(+{self.armure})")
        else:
            print(f"[STATS] {msg}:","PDV:",self.pdv,"| PA + Arme:",f"{self.pa[0]+self.arme}-{self.pa[1]+self.arme}",f"(+{self.arme})","| PD + Armure:",(self.pd+self.armure),f"(+{self.armure})")
            
    
    def deplacement(self, carte):
        inp = input("Choisissez une lettre : G/A = Gauche, D = Droite, B/S = Bas, H/W = Haut, Q = Afficher statistiques du joueur: ").upper()
        coords_joueur = self.position
        if inp in ["G", "A"] and coords_joueur[0] > 0:
            coords_joueur[0] -= 1
        elif inp in ["D"] and coords_joueur[0] < len(carte.grille[0])-1:
            coords_joueur[0] += 1
        elif inp in ["H", "W"] and coords_joueur[1] > 0:
            coords_joueur[1] -= 1
        elif inp in ["B", "S"] and coords_joueur[1] < len(carte.grille)-1:
            coords_joueur[1] += 1
        elif inp in ["Q"]:
            self.printStats()
            
    def attaque(self,autre):
        global tour_dattaque
        
        if tour_dattaque == 1: # heros attaque
            tour_dattaque = 2
            if isinstance(self.pa,int):
                dmg = (self.pa + self.arme - autre.pd)
            else:
                dmg = (randint(self.pa[0]+self.arme,self.pa[1]+self.arme) - autre.pd)
            autre.pdv -= dmg
            print("Heros attaque monstre avec",dmg,"points. ",f"(+{self.arme} appliqué)")
            if autre.pdv > 0:
                print("Il reste",autre.pdv,"PDV au monstre")
            else:
                tour_dattaque = 1 # monstre est mort
                
        elif tour_dattaque == 2: # monstre attaque
            tour_dattaque = 1
            dmg = (randint(autre.pa[0],autre.pa[1]) - self.pd - self.armure)
            if dmg <= 0:
                print("[INFO] Vos points de défense et/ou votre armure ont annulé les dégâts de l'ennemi! Votres PDV reste a",self.pdv)
            else:
                self.pdv -= dmg
                print("Monstre attaque heros avec", dmg,"points. ",f"(-{self.armure} appliqué)")
                if self.pdv > 0:
                    print("Il reste",self.pdv,"PDV au heros")
        
        self.combat(autre)
    
    def combat(self,autre):
        global jeu_terminer
        if self.pdv <= 0: #and autre.pdv > 0:
            print("[DEFAITE] L'heros est mort. Il reste",autre.pdv,"PDV au monstre.")
            jeu_terminer = False
            
        elif self.pdv > 0 and autre.pdv <= 0:
            if isinstance(autre,Monstre):
                print("[VICTOIRE] Le monstre",autre.nom,"est mort! Il vous reste",self.pdv,"PDV.")           
                Monstre.monstres_tuer += 1
                monstres.remove(autre)
        
        elif self.pdv > 0 and autre.pdv > 0:
            self.attaque(autre)

class Monstre(personnage):
    monstres_tuer = 0
    def __init__(self,x,y,N="monstre",pdv=20,pa=(5,5),pd=0):
        personnage.__init__(self,N,pdv,[x,y],pa,pd)
        
    def deplacementM(self, carte):
        
        def pas_de_monstre(X,Y):
            global assistance
            m_sur_case = False
            for monstre in monstres:
                if monstre.position == [X,Y]:
                    m_sur_case = True
            if m_sur_case == False:
                print("> Un monstre",self.nom,"s'est deplacer de",self.position,"vers",[X,Y]) if assistance else print("> Monstre deplacer")
                return True
            return False
            
        direction = ["G","D","H","B"][randint(0,3)]
        coords_monstre = self.position
        
        if direction == "G" and coords_monstre[0] > 0:
            if pas_de_monstre((coords_monstre[0]-1),coords_monstre[1]):
                coords_monstre[0] -= 1
        elif direction == "D" and coords_monstre[0] < len(carte.grille[0])-1:
            if pas_de_monstre((coords_monstre[0]+1),coords_monstre[1]):
                coords_monstre[0] += 1
        elif direction == "H" and coords_monstre[1] > 0:
            if pas_de_monstre(coords_monstre[0],(coords_monstre[1]-1)):
                coords_monstre[1] -= 1
        elif direction == "B" and coords_monstre[1] < len(carte.grille)-1:
            if pas_de_monstre(coords_monstre[0],(coords_monstre[1]+1)):
                coords_monstre[1] += 1
        else:
            pass
            #print("monstre ne pouvez pas bouger")
        

monstres = []
tresors = []
potions = []
armes = []
armures = []

class monde():
    def __init__(self,X,Y):
        self.largeur = X
        self.hauteur = Y
        self.grille = []

        self.initialiser(heros)
        self.visualiser(heros)
        self.tour(heros)

    def creer_monstre(self,X,ligne):
        global assistance
        type_monstre = randint(1,3)
        if type_monstre == 1:
            monstres.append(Monstre(X,ligne,"'Équilibré' [20HP (4,6)PA]",20,(4,6)))
            
            if [X,ligne] in tresors:
                print("> Monstre équilibré [20HP (4,6)PA] creer sur trésor a",[X,ligne],"<") if assistance else print("> Monstre creer sur trésor <")
            else:
                print("> Monstre équilibré [20HP (4,6)PA] creer a",[X,ligne],"<") if assistance else print("> Monstre creer <")
                
        elif type_monstre == 2:
            monstres.append(Monstre(X,ligne,"'Santé élevée, dégâts faibles' [30HP (1,3)PA]",30,(1,3)))
            
            if [X,ligne] in tresors:
                print("> Monstre 'Santé élevée, dégâts faibles' [30HP (1,3)PA] creer sur trésor a",[X,ligne],"<") if assistance else print("> Monstre creer sur trésor <")
            else:
                print("> Monstre 'Santé élevée, dégâts faibles' [30HP (1,3)PA] creer a",[X,ligne],"<") if assistance else print("> Monstre creer <")
            
        elif type_monstre == 3:
            monstres.append(Monstre(X,ligne,"'Santé faible, dégâts élevés' [10HP (9,11)PA]",10,(9,11)))
            
            if [X,ligne] in tresors:
                print("> Monstre 'Santé faible, dégâts élevés' [10HP (9,11)PA] creer sur trésor a",[X,ligne],"<") if assistance else print("> Monstre creer sur trésor <")
            else:
                print("> Monstre 'Santé faible, dégâts élevés' [10HP (9,11)PA] creer a",[X,ligne],"<") if assistance else print("> Monstre creer <")

    def initialiser(self,joueur):
        print("[INITIALISATION DU JEU]")
        global assistance
        for Y in range(self.hauteur):
            self.grille.append([])
        for ligne in range(len(self.grille)):
            for X in range(self.largeur):
                self.grille[ligne].append(X)
                
                if randint(1,10) == 3 and joueur.position != [X,ligne]:
                    self.creer_monstre(X,ligne)
        
        nbr_cases = len(self.grille[0])*len(self.grille) # creation de tresors
        if nbr_cases < 20:
            locx = randint(0,len(self.grille[0])-1)
            locy = randint(0,len(self.grille)-1)
            while [locx,locy] == [0,0]:
                locx = randint(0,len(self.grille[0])-1)
                locy = randint(0,len(self.grille)-1)
            tresors.append([locx,locy])
            
            print(f"> Trésor creer a {[locx,locy]} <") if assistance else print("> Trésor creer <")

            monstre_sur_case = False
            for monstre in monstres:
                if monstre.position == [locx,locy]:
                    monstre_sur_case = True

            if monstre_sur_case == False:
                self.creer_monstre(locx,locy)
                    
            else:
                pass
                #print("Monstre existe deja sur ce tresor.")

        elif nbr_cases < 50:
            while len(tresors) < 3:
                locx = randint(0,len(self.grille[0])-1)
                locy = randint(0,len(self.grille)-1)

                if not [locx,locy] in tresors and [locx,locy] != [0,0]:
                    tresors.append([locx,locy])
                    
                    print(f"> Trésor creer a {[locx,locy]} <") if assistance else print("> Trésor creer <")

                    monstre_sur_case = False
                    for monstre in monstres:
                        if monstre.position == [locx,locy]:
                            monstre_sur_case = True

                    if monstre_sur_case == False:
                        self.creer_monstre(locx,locy)
                             
                    else:
                        pass
                        #print("monstre existe deja sur ce tresor")

        elif nbr_cases > 50:
            while len(tresors) < 5:
                locx = randint(0,len(self.grille[0])-1)
                locy = randint(0,len(self.grille)-1)

                if not [locx,locy] in tresors and [locx,locy] != [0,0]:
                    tresors.append([locx,locy])
                    
                    print(f"> Trésor creer a {[locx,locy]} <") if assistance else print("> Trésor creer <")

                    monstre_sur_case = False
                    for monstre in monstres:
                        if monstre.position == [locx,locy]:
                            monstre_sur_case = True

                    if monstre_sur_case == False:
                        self.creer_monstre(locx,locy)
                        
                    else:
                        pass
                        #print("monstre existe deja sur ce tresor")
        
    
        _ = 0 # compteur pour creation de armes et armures
        if len(monstres) >= 2:
            while _ < 2: 
                for m in monstres:
                    if randint(1,3) == 2 and m.position not in armes and m.position not in armures and _ < 2:
                        _ += 1
                        if randint(1,2) == 1:
                            armes.append(m.position)
                            
                            print(f"> Arme creer a {m.position} <") if assistance else print("> Arme creer <")
                        else:
                            armures.append(m.position)
                            
                            print(f"> Armure cree a {m.position} <") if assistance else print("> Armure creer <")
        else:
            print("[INFO] Pas suffisamment de monstres pour creer des armes / armures.")
    
        if (nbr_cases - 1 - len(monstres)) >= 3: # creation de potions de +-5 PDV // note: pas besoin de verifier armes armures ou tresors car tous on des mosntres sur et -1 car doit pas compter cas joueur dans calcul meme impossible d'etre sur
            while len(potions) < 3:
                locx = randint(0,len(self.grille[0])-1)
                locy = randint(0,len(self.grille)-1)
                
                if not [locx,locy] in potions and [locx,locy] != [0,0]:
                    monstre_dans_case = False
                    for monstre in monstres:
                        if monstre.position == [locx,locy]:
                            monstre_dans_case = True
                       
                    if monstre_dans_case == False:
                        potions.append([locx,locy])
                        print(f"> Potion creer a {[locx,locy]} <") if assistance else print("> Potion creer <")
        else:
            print("[INFO] Il n y a pas suffisamment de place pour mettre des potions.")

        print("[FIN INITIALISATION] BIENVENU A LA QUÊTE AU TRÉSOR")
        print("[INFO] Il existe", len(tresors),"tresor.s,",len(potions),"potion.s,",len(armes),"arme.s,",len(armures),"armure.s, et",len(monstres),"monstre.s")
        joueur.printStats("Vos statistiques sont")
            
    def visualiser(self,joueur):
        coords_joueur = joueur.position
        j_placer = False
        print()
        for _ in range(len(self.grille[0])):
            print(" _",end="")
        print()
        for i in range(len(self.grille)):
            for e in self.grille[i]:
                if i == coords_joueur[1] and j_placer == False and e == coords_joueur[0]:
                        if e == 0:
                            print("|X|",end="")
                            j_placer = True
                        else:
                            print("X|",end="")
                            j_placer = True
                elif e == 0:
                    print("|_|",end="")
                else:
                    print("_|",end="")
            print()
        print()
    
    def tour(self,joueur):
        global jeu_terminer
        if joueur.pdv > 0 and jeu_terminer == False:
            coords_av_dep = joueur.position.copy()
            joueur.deplacement(self)
            coords_ap_dep = joueur.position
            
            if coords_av_dep == coords_ap_dep:
                print("> Vous n'avez pas bouger.")
                self.tour(joueur)
            print("###########################")
            if len(monstres) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                for monstre in monstres:
                    if monstre.position == coords_ap_dep and joueur.pdv > 0:
                        print("[COMBAT] Un monstre",monstre.nom,"est dans cette case! le combat commence!")
                        joueur.printStats("Vos statistiques avant le combat sont")
                        joueur.combat(monstre)
                        if joueur.pdv > 0:
                            joueur.printStats("Vos statistique apres le combat sont")
                            if len(monstres) > 0:
                                print("[-MONSTRE] Vous avez jusqu'a la tuer ",Monstre.monstres_tuer," monstre(s), il reste",len(monstres))
                            else:
                                print("[-MONSTRE] Vous avez tuer tous les monstres")
                        else:
                            print("[FIN] Vous êtes morts!")
                            jeu_terminer = True
                        print("###########################")
                        
            if len(tresors) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                for tresor in tresors:
                    if tresor == joueur.position:
                        if len(tresors) > 1:
                            print("[+TRESOR] Vous avez capturer un tresor! loc:",tresor,end=".")
                            tresors.remove(tresor)
                            print("[INFO] Il reste",len(tresors),"tresor(s)")
                        elif len(tresors) == 1:
                            print("[+TRESOR] Vous avez capturer tous les tresors! le dernier etait a",tresor)
                            tresors.remove(tresor)
                            jeu_terminer = True
                
                            
            if len(potions) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                for potion in potions:
                    if potion == joueur.position and joueur.pdv > 0:
                        if len(potions) > 1:
                            if randint(1,2) == 1:
                                joueur.pdv += 5
                                print("[+POTION DE GUÉRISON] Vous avez ramassez une potion de guérison, cela vous donne 5 PDV, vous avez maintenant",joueur.pdv,"PDV")
                                
                            else:
                                joueur.pdv -= 5
                                print("[+POTION DE POISON] Vous avez ramassez une potion poisonnée, cela vous fait perdre 5 PDV, vous avez maintenant",joueur.pdv,"PDV")
                            
                            potions.remove(potion)
                            print("[INFO] Il reste",len(potions),"potion(s) sur la carte")
                                
                        elif len(potions) == 1:
                            if randint(1,2) == 1:
                                joueur.pdv += 5
                                print("[+POTION DE GUÉRISON] vous avez ramassez une potion de guérison, cela vous donne 5 PDV, vous avez maintenant",joueur.pdv,"PDV")
                            else:
                                joueur.pdv -= 5
                                print("[+POTION DE POISON] vous avez ramassez une potion poisonnée, cela vous fait perdre 5 PDV, vous avez maintenant",joueur.pdv,"PDV")
                            
                            print("[INFO] Vous avez ramassez toutes le potions qui existaient, vous avez maintenant",joueur.pdv,"PDV")
                            potions.remove(potion)
                            
                if joueur.pdv <= 0:
                    print("[FIN] Vous etes morts!")
                    jeu_terminer = True
                            
                
                        
            if len(armures) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                for armure in armures:
                    if armure == joueur.position:
                        if len(armures) > 1:
                            joueur.armure += 2
                            print(f"[+ARMURE] Vous avez ramassez une armure, cela vous donne +2 points de défense, votre PD + armure équivaut maintenant {joueur.pd + joueur.armure} points. (+{joueur.armure} appliqué).")
                            armures.remove(armure)
                            print("[INFO] Il reste",len(armures),"armure(s) sur la carte.")
                        elif len(armures) == 1:
                            joueur.armure += 2
                            print(f"[+ARMURE] Vous avez ramassez toutes les armures qui existaient, votre PD + armure équivaut maintenant {joueur.pd+joueur.armure} points. (+{joueur.armure} appliqué)")
                            armures.remove(armure)
                
                        
            if len(armes) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                for arme in armes:
                    if arme == joueur.position:
                        if len(armes) > 1:
                            joueur.arme += 2
                            if isinstance(joueur.pa,int):
                                print(f"[+ARME] Vous avez ramassez un arme, cela vous donne +2 attaque, votre PA + arme équivaut maintenant {joueur.pa+joueur.arme} points. (+{joueur.arme} appliqué)")
                            else:
                                print(f"[+ARME] Vous avez ramassez un arme, cela vous donne +2 attaque, votre PA + arme équivaut maintenant ({joueur.pa[0]+joueur.arme},{joueur.pa[1]+joueur.arme}) points. (+{joueur.arme} appliqué)")
                            armes.remove(arme)
                            print("[INFO] Il reste",len(armes),"arme(s) sur la carte.")
                        elif len(armes) == 1:
                            joueur.arme += 2
                            if isinstance(joueur.pa,int):
                                print(f"[+ARME] Vous avez ramassez toutes les armes qui existaient, votre PA + arme équivaut maintenant {joueur.pa+joueur.arme} points. (+{joueur.arme} appliqué)")
                            else:
                                print(f"[+ARME] Vous avez ramassez toutes les armes qui existaient, votre PA + arme équivaut maintenant ({joueur.pa[0]+joueur.arme},{joueur.pa[1]+joueur.arme}) points. (+{joueur.arme} appliqué)")
                            armes.remove(arme)
                
                        
            if len(monstres) > 0 and joueur.pdv > 0 and jeu_terminer == False:
                compteur = 0
                while compteur < len(monstres) and joueur.pdv > 0:
                    monstre = monstres[compteur]
                    monstre.deplacementM(self)
                    compteur += 1
                    if monstre.position == joueur.position:
                        print("###########################")
                        compteur -=1
                        print("[COMBAT] Un monstre",monstre.nom,"s'est deplacer vers cette case! Le combat commence!")
                        joueur.printStats("Vos statistique avant le combat sont")
                        joueur.combat(monstre)
                        if joueur.pdv > 0:
                            joueur.printStats("Vos statistiques apres le combat sont")
                            if len(monstres) > 0:
                                print("[-MONSTRE] Vous avez jusqu'a la tuer",Monstre.monstres_tuer,"monstre(s), il reste",len(monstres))
                            else:
                                print("[-MONSTRE] Vous avez tuer tous les monstres.")
                        else:
                            jeu_terminer = True
                            break
                        print("###########################")
            
            if jeu_terminer == False:
                print("[INFO] Il reste", len(tresors),"tresor.s,",len(potions),"potion.s,",len(armes),"arme.s,",len(armures),"armure.s, et",len(monstres),"monstre.s")
                joueur.printStats("Vos statistiques sont")
                self.visualiser(joueur)
                self.tour(joueur)

            elif jeu_terminer == True:
                if joueur.pdv > 0 and len(tresors) == 0:
                    print("[FIN - GAGNER] jeu terminer, vous avez capturer tous les tresors!")
                    print("[INFO] Il rester",len(potions),"potion.s,",len(armes),"arme.s,",len(armures),"armure.s, et",len(monstres),"monstre.s")
                    joueur.printStats("Vos statistiques étaient")
                
                elif joueur.pdv <= 0:
                    print("[FIN - MORT] Jeu terminer, vous êtes morts!")
                    print("[INFO] Il rester", len(tresors),"tresors,",len(potions),"potions,",len(armes),"armes,",len(armures),"armures, et",len(monstres),"monstres")
                    joueur.printStats("Vos statistiques étaient")
                
                else:
                    print("qlq chose ne va pas")

        elif joueur.pdv <= 0:
            jeu_terminer = True
            print("[FIN - MORT] Jeu terminer, vous êtes morts")
            print("[INFO] Il rester", len(tresors),"tresors,",len(potions),"potions,",len(armes),"armes,",len(armures),"armures, et",len(monstres),"monstres")
        
        elif joueur.pdv > 0 and jeu_terminer == True:
            print("[FIN - GAGNER] jeu terminer, vous avez capturer tous les tresors!")
            print("[INFO] Il rester",len(potions),"potion.s,",len(armes),"arme.s,",len(armures),"armure.s, et",len(monstres),"monstre.s")
            joueur.printStats("Vos statistiques étaient")
            

if jeu_terminer == False:
    Xinput = input("Choisissez la largeur de la carte.")
    Yinput = input("Choisissez la hauteur de la carte.")

    Xinput = int(Xinput)
    Yinput = int(Yinput)
    if Xinput < 2 or Yinput < 2:
        print("[ERR] Les valeurs doivent etre au moins 2 chacune!")
    else:   
        assistanceReq = (input("[ASSISTANCE] Voulez vois savoir vers où les monstres se deplacent et les coordonnées de tous les objets? (O/N)")).upper()
        if assistanceReq == "O":
            assistance = True
                
        heros = personnage()
        carte = monde(Xinput,Yinput)
    #"""

    """
    try:
        Xinput = input("Choisissez la largeur de la carte.")
        Yinput = input("Choisissez la hauteur de la carte.")

        Xinput = int(Xinput)
        Yinput = int(Yinput)
        if Xinput < 2 or Yinput < 2:
            print("[ERR] Les valeurs doivent etre au moins 2 chacune!")
        else:   
            assistanceReq = (input("[ASSISTANCE] Voulez vois savoir vers où les monstres se deplacent et les coordonnées de tous les objets? (O/N)")).upper()
            if assistanceReq == "O":
                assistance = True
                    
            heros = personnage()
            carte = monde(Xinput,Yinput)
            
    except:
        print("[ERR] Votres valeurs doivent etre des nombres entiers!")"""
