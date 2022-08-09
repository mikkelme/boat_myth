# Boat myth 

Hobby project to settle an argument with my father-in-law. The article is written in danish but the following abstract sums up the small resulting article.


> In this article we investegate the rule of thumb for recognizing when two boats are on a collision course. The proposed statement to be analyzed, namely The background method, can be formulated briefly as: ”If the static background seen behind the oncoming boat does not visually move relatively to the boat, then you are on a collision course.”. The analysis have shown that this statement is strongly related to the dertermination of the relative bearing. By mathematical derivation we found that if and only if two boats approaching each other with constant velocity have constant relative bearing, they are on collision couse. Therefore the direct determination of the relative bearing is the most precise way of recognizing a collision course. On the other hand we found that the background method can be used as a means to determine whether the relative bearing is constant in special cases. This were mainly derived by an analytical approach but is also supported by numerical simmulations. In general the background method is found to be valid when used in greater distances to the coast, losely estimated to approximately 833 meters or more. The exact value requires the relative velocity of the observer, the tolerance definition for a humanly recognizable angular velocity and is dependent on the value of the relative bearning and the angle between the heading and the coast. The nature of this relationship is showcased generally on figure 7 and 8.



## Animationer
Her findes animationer til støtte af resultaterne i rapporten. Animationerne viser forskellige situationer med og uden kollision, og hvordan sigtelinjen til baggrunden ændres undervejs. Bemærk at det kan tage lidt tid at loade.

### Animation 1 (Kollision)
**Beskrivelse**: Simpel kollision hvor baggrundsmetoden er misvisende. 

|         | Start         | Slut   |
|:-------:|:-------------:| :-----:|
| **HB**  | (0,0)         | (0,40) |
| **KB**  | (40,40)       | (0,40) |

![](article/figures/aniC1.gif)

### Animation 2 (Kollision)
**Beskrivelse**: Lignende eksempel som i animaiton 1, men her gør den mindre pejlingsvinkel at baggrundsmetoden ikke er misvisende i samme grad. For iagtageren synes baggrunden ikke at forflytte sig i samme grad (vinkelmæssig) som i animatiom 1.

|         | Start         | Slut   |
|:-------:|:-------------:| :-----:|
| **HB**  | (0,0)         | (0,40) |
| **KB**  | (40,90)       | (0,40) |

![](article/figures/aniC2.gif)

### Animation 3 (Kollision)
**Beskrivelse**: Tilfælde hvor baggrundsmetoden giver det mest misvisende resultat mulig. 

|         | Start         | Slut   |
|:-------:|:-------------:| :-----:|
| **HB**  | (0,0)         | (0,40) |
| **KB**  | (20,0)        | (0,40) |

![](article/figures/aniC3.gif)

### Animation 4 (Ikke-Kollision)
**Beskrivelse**: Eksempel på ikke kollision, hvor man ved brug af baggrundsbetoden kan tro at bådene er på kollisionskurs i begyndelsen af animationen. 

|         | Start         | Slut   |
|:-------:|:-------------:| :-----:|
| **HB**  | (0,0)         | (0,40) |
| **KB**  | (40,40)       | (10,40) |

![](article/figures/aniNC1.gif)

### Animation 5 (Ikke-Kollision)
**Beskrivelse**: Endnu et eksempel hvor baggrundsmetoden umiddelbart predikere kollision selvom dette langt fra er tilfældet. Dette bliver tydelig efter lidt tid dog.

|         | Start         | Slut   |
|:-------:|:-------------:| :-----:|
| **HB**  | (0,0)         | (0,80) |
| **KB**  | (70,-20)       | (10,50) |

![](article/figures/aniNC2.gif)


