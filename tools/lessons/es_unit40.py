"""Unit 40: review of Unit 8 (textbook Chapter 40): ser/estar/haber in the past, trade and economy, perfect tenses, the present perfect subjunctive, si-clauses, intellectual property, political and art vocabulary, como si / ojalá / quisiera, the conditional perfect and the pluperfect subjunctive."""
from dsl_es import *

# ---------------------------------------------------------------------------- 864
L864 = lesson(
    "Review: ser, estar and haber in a story of the past (a railroad)",
    "El trabajo era duro. Los trabajadores estaban lejos de su familia. Hubo accidentes.",
    requires=["ferrocarril", "trabajador", "inmigrante", "construcción", "accidente", "montaña", "ceremonia", "histórico", "familia", "estado", "duro", "lejos"],
    cards=[
        card("Choosing between era, fue, estaba, estuvo, había and hubo",
             "In a story about the past, the imperfect describes the background (what things were like) and the preterite reports events (what happened). "
             "Era and estaba set the scene. Fue and estuvo present a completed fact. Había describes what existed, and hubo reports that something took place. Hubo never changes for plural nouns.",
             tables=[table(["Forma", "Uso", "Ejemplo"],
                           [["era / eran", "description, identity, background", "Muchos eran inmigrantes."],
                            ["estaba / estaban", "state or place in the background", "Estaban lejos de su familia."],
                            ["había", "there was / there were (background)", "Había miles de trabajadores."],
                            ["hubo", "there was (an event)", "Hubo accidentes graves."],
                            ["fue", "was (a completed event or fact)", "Fue un momento histórico."],
                            ["estuvo / estuvieron", "was (for a limited time)", "Estuvieron meses en las montañas."]],
                           say=[2])]),
        card("A short history (original summary)",
             "In the nineteenth century, builders laid a railroad across the United States. Thousands of workers took part, and many of them were immigrants from China. "
             "The work was hard and dangerous. The last two sections of track met in Utah in 1869. Historians note that for a long time many workers received little recognition.",
             examples=[
                 ex("Había miles de trabajadores, y muchos eran inmigrantes de China.", "There were thousands of workers, and many were immigrants from China.", "Había"),
                 ex("El trabajo era duro y los trabajadores estaban lejos de su familia.", "The work was hard and the workers were far from their families.", "estaban"),
                 ex("En mil ochocientos sesenta y nueve se unieron las dos líneas, y hubo una ceremonia.", "In eighteen sixty-nine the two lines were joined, and there was a ceremony.", "hubo"),
             ]),
    ],
    exercises=[
        M("Which verb gives background (“there were thousands of workers”)?", "había", ["hubo", "fue", "estuvo"], "Background existence."),
        M("Which verb reports that an accident took place?", "hubo", ["había", "era", "estaba"], "An event."),
        M("Is “hubieron” correct for “there were”?", "No, the form is hubo", ["Yes, always", "Only in writing", "Only with people"], "Hubo does not change."),
        F("En aquella época ___ miles de trabajadores en el campamento.", "había", ["habían", "han", "hayan"], "Haber is singular in this meaning.", tr="At that time there were thousands of workers in the camp.", lemma="haber:él:impf"),
        F("Muchos trabajadores ___ inmigrantes de China.", "eran", ["era", "fuiste", "soy"], "Plural subject, background.", tr="Many workers were immigrants from China.", lemma="ser:ellos:impf"),
        F("Los trabajadores ___ muy lejos de sus familias.", "estaban", ["estaba", "estamos", "estarán"], "Plural subject, place.", tr="The workers were very far from their families.", lemma="estar:ellos:impf"),
        F("De repente ___ un accidente grave en la montaña.", "hubo", ["había", "hubieron", "habían"], "A sudden event.", tr="Suddenly there was a serious accident in the mountains.", lemma="haber:él:pret"),
        F("La ceremonia ___ un momento histórico.", "fue", ["fueron", "fui", "fuimos"], "Singular subject, event.", tr="The ceremony was a historic moment.", lemma="ser:él:pret"),
        F("Durante meses, los ingenieros ___ en las montañas.", "estuvieron", ["estuvo", "estuve", "estuvimos"], "Plural subject.", tr="For months the engineers were in the mountains.", lemma="estar:ellos:pret"),
    ],
    verify=vpp("estar", "estuve", "estuviste", "estuvo", "estuvimos", "estuvisteis", "estuvieron") + vpi("ser", "era", "eras", "era", "éramos", "erais", "eran") + vpi("estar", "estaba", "estabas", "estaba", "estábamos", "estabais", "estaban"),
)

# ---------------------------------------------------------------------------- 865
L865 = lesson(
    "Review: era or fue, estaba or estuvo, había or hubo?",
    "Cuando llegué, había mucha gente. De repente hubo un ruido.",
    requires=["ser", "estar", "haber", "gente", "plaza", "ruido", "director", "hospital", "niña", "tarde", "nieve", "ciudad"],
    cards=[
        card("Cue words help you choose",
             "Certain words point toward the imperfect (background) or the preterite (event). Use them as clues, but always ask: am I describing the scene, or reporting something that happened?",
             tables=[table(["Pista", "Se usa", "Ejemplo"],
                           [["siempre, de niño, mientras, todos los días", "imperfecto", "Siempre había mucha gente en esa calle."],
                            ["de repente, de pronto, por primera vez", "pretérito", "De repente hubo un ruido muy fuerte."],
                            ["cuando + acción puntual", "la otra cláusula suele ir en imperfecto si describe el fondo", "Cuando lo llamé, el director estaba en el hospital."],
                            ["una duración o una fecha exacta", "pretérito", "La semana pasada estuvo dos días en el hospital."]],
                           say=[2])]),
        card("Same sentence, different picture",
             "Notice how the choice changes the picture. Era describes what she was like as a child. Fue would report a single event or a completed fact.",
             examples=[
                 ex("De niña, ella era muy tímida.", "As a child, she was very shy.", "era"),
                 ex("Por primera vez en años, hubo nieve en la ciudad.", "For the first time in years, there was snow in the city.", "hubo"),
             ]),
    ],
    exercises=[
        M("Which word signals a sudden event?", "de repente", ["siempre", "mientras", "de niño"], "Event cue."),
        M("Which tense do “siempre” and “mientras” usually point to?", "The imperfect", ["The preterite", "The future", "The conditional"], "Ongoing background."),
        M("In “Cuando lo llamé, el director estaba en el hospital”, what is “estaba”?", "Background to a specific action", ["A completed event", "A command", "A future plan"], "The scene."),
        F("Cuando llegamos, ya ___ mucha gente en la plaza.", "había", ["hubo", "hubieron", "habían"], "Background: many people were already there.", tr="When we arrived, there were already many people in the square.", lemma="haber:él:impf"),
        F("De niño, siempre ___ mucha gente en esa calle.", "había", ["hubo", "hubieron", "habían"], "Habit in the past.", tr="When I was a child, there were always many people on that street.", lemma="haber:él:impf"),
        F("Por primera vez en años, ___ nieve en la ciudad.", "hubo", ["había", "habían", "hubieron"], "A first-time event.", tr="For the first time in years, there was snow in the city.", lemma="haber:él:pret"),
        F("De niña, ella ___ muy tímida.", "era", ["eras", "fuimos", "eran"], "Description of a past habit or trait.", tr="As a child, she was very shy.", lemma="ser:ella:impf"),
        F("Cuando lo llamé, el director ___ en el hospital.", "estaba", ["estuvo", "estuvieron", "estuvimos"], "Background.", tr="When I called him, the director was in the hospital.", lemma="estar:él:impf"),
        F("La semana pasada, ellos ___ dos días en el hospital.", "estuvieron", ["estaba", "estuvimos", "estuve"], "Plural subject, duration.", tr="Last week they were in the hospital for two days.", lemma="estar:ellos:pret"),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 866
L866 = lesson(
    "Reading: trade between China and Latin America (summary in our own words)",
    "El comercio ha crecido mucho. Algunos economistas advierten que la relación es desigual.",
    requires=["comercio", "crecimiento", "energía", "alimento", "tecnología", "tratado", "producto", "región", "economista", "estrategia", "gobierno", "fuente"],
    cards=[
        card("Texto resumido, primera parte",
             "This text is a summary of common arguments in our own words. It is not a report with exact numbers. Figures change every year, so check current sources.",
             examples=[
                 ex("Durante las últimas décadas, el comercio entre China y América Latina ha crecido mucho.", "In recent decades, trade between China and Latin America has grown a lot.", "ha crecido"),
                 ex("Varios análisis explican este aumento por el crecimiento de la economía china, que necesita materias primas, energía y alimentos.", "Several analyses explain this increase by the growth of China's economy, which needs raw materials, energy and food.", "necesita"),
                 ex("Muchos países latinoamericanos han exportado esos productos y han importado bienes de consumo y tecnología.", "Many Latin American countries have exported those products and have imported consumer goods and technology.", "han exportado"),
                 ex("Algunos países firmaron tratados de libre comercio con China.", "Some countries signed free trade agreements with China.", "firmaron"),
             ]),
        card("Texto resumido, segunda parte",
             "Different experts weigh the results differently.",
             examples=[
                 ex("Sin embargo, algunos economistas advierten que la relación es desigual.", "However, some economists warn that the relationship is unequal.", "advierten"),
                 ex("Según estos economistas, la región vende sobre todo materias primas, y las manufacturas importadas pueden competir con la producción local.", "According to these economists, the region sells mostly raw materials, and imported manufactured goods can compete with local production.", "pueden competir"),
                 ex("Otros expertos responden que el comercio con China ofrece una alternativa y que depende de la estrategia de cada gobierno.", "Other experts answer that trade with China offers an alternative and that it depends on each government's strategy.", "depende"),
                 ex("Los datos cambian cada año; por eso conviene consultar fuentes actuales.", "The data change every year, so it is wise to consult current sources.", "conviene"),
             ]),
    ],
    exercises=[
        M("Why do some analyses say trade has grown?", "China's economy needs raw materials, energy and food", ["China stopped trading", "Latin America closed its ports", "Taxes disappeared"], "The economic growth of China."),
        M("What do some economists warn about?", "An unequal relationship", ["Too little technology in China", "A total end of trade", "A new language"], "Desigual."),
        M("What do other experts say?", "Results depend on each government's strategy", ["Nothing can change", "Only China decides", "Trade is illegal"], "La estrategia de cada gobierno."),
        M("Why does the text say to consult current sources?", "The data change every year", ["The books are old", "The text is a poem", "The figures are secret"], "Los datos cambian."),
        F("El comercio con China ___ crecido mucho.", "ha", ["han", "he", "hemos"], "Singular subject.", tr="Trade with China has grown a lot.", lemma="haber:él"),
        F("Los países ___ exportado materias primas.", "han", ["ha", "hemos", "has"], "Plural subject.", tr="The countries have exported raw materials.", lemma="haber:ellos"),
        F("Algunos expertos ___ que la relación es desigual.", "advierten", ["advierte", "advertimos", "adviertes"], "Plural subject.", tr="Some experts warn that the relationship is unequal.", lemma="advertir:ellos"),
        F("___ embargo, algunas industrias locales pueden sufrir.", "Sin", ["Con", "Por", "Sobre"], "Sin embargo = however.", tr="However, some local industries may suffer."),
        F("Los datos ___ cada año.", "cambian", ["cambia", "cambiamos", "cambias"], "Plural subject.", tr="The data change every year.", lemma="cambiar:ellos"),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 867
L867 = lesson(
    "Review: trade and economy words",
    "Un país importa más de lo que exporta: tiene un déficit.",
    requires=["comercio", "importar", "déficit", "inversión", "socio", "tratado", "empresa", "empleo", "salario", "precio", "mercado", "plazo"],
    cards=[
        card("Key words",
             "These words appear in news and in textbooks about the economy. Note the accent in déficit and the English-looking word superávit, which has the accent on the a.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["el comercio", "trade", "El comercio crece."],
                            ["importar", "to import", "Importamos tecnología."],
                            ["exportar", "to export", "Exportan alimentos."],
                            ["el déficit", "deficit", "Hay déficit cuando se importa más de lo que se exporta."],
                            ["el superávit", "surplus", "Hay superávit cuando se exporta más."],
                            ["la materia prima", "raw material", "El cobre es una materia prima."],
                            ["las manufacturas", "manufactured goods", "Compran manufacturas baratas."],
                            ["el tratado de libre comercio", "free trade agreement", "Firmaron un tratado de libre comercio."],
                            ["la inversión", "investment", "La inversión crea empleo."],
                            ["el socio comercial", "trading partner", "Es nuestro principal socio comercial."],
                            ["a largo plazo", "in the long term", "Planean a largo plazo."]],
                           say=[0, 2])]),
        card("Remember",
             "Importar and exportar are regular -ar verbs. The noun for the person is el importador / el exportador.",
             examples=[
                 ex("Un país con superávit exporta más de lo que importa.", "A country with a surplus exports more than it imports.", "superávit"),
                 ex("Una inversión puede crear empleo a largo plazo.", "An investment can create jobs in the long term.", "a largo plazo"),
             ]),
    ],
    exercises=[
        M("What is a “déficit comercial”?", "Importing more than exporting", ["Exporting more than importing", "A kind of tax", "A market day"], "Importa más."),
        M("What does “a largo plazo” mean?", "In the long term", ["Right away", "At a long table", "By plane"], "Plazo = time limit."),
        M("Which word is a raw material?", "el cobre", ["la película", "el poema", "el museo"], "Cobre is a metal."),
        F("Un país que importa más de lo que exporta tiene un ___.", "déficit", ["superávit", "tratado", "socio"], "Deficit.", tr="A country that imports more than it exports has a deficit."),
        F("Un país que exporta más de lo que importa tiene un ___.", "superávit", ["déficit", "salario", "precio"], "Surplus.", tr="A country that exports more than it imports has a surplus."),
        F("El cobre y el petróleo son ___ primas.", "materias", ["manufacturas", "inversiones", "empresas"], "Materias primas.", tr="Copper and oil are raw materials."),
        F("Los dos países firmaron un ___ de libre comercio.", "tratado", ["déficit", "salario", "precio"], "A trade agreement.", tr="The two countries signed a free trade agreement."),
        F("China es el principal ___ comercial de varios países.", "socio", ["salario", "precio", "tratado"], "Trading partner.", tr="China is the main trading partner of several countries."),
        F("La ___ en nuevas fábricas puede crear empleo.", "inversión", ["manufactura", "región", "persona"], "Investment.", tr="Investment in new factories can create jobs."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 868
L868 = lesson(
    "Review: has been doing, had been doing, has been done",
    "La empresa había estado perdiendo dinero. El plan ha sido aprobado.",
    requires=["empresa", "perder", "dinero", "buscar", "trabajar", "plan", "aprobar", "apoyar", "preocupar", "crisis", "gobierno", "mes"],
    cards=[
        card("Three useful patterns",
             "The perfect continuous (ha estado + gerund / había estado + gerund) says that something has been going on or had been going on for a while. "
             "The passive perfect (ha sido / había sido + participle) says that something has been done to a thing. The participle agrees with the thing.",
             tables=[table(["Patrón", "Ejemplo"],
                           [["ha estado + gerundio", "La empresa ha estado buscando una solución."],
                            ["había estado + gerundio", "La empresa había estado perdiendo dinero."],
                            ["ha sido + participio", "El plan ha sido aprobado."],
                            ["habían sido + participio", "Las medidas habían sido respaldadas por el gobierno."],
                            ["ha habido", "Ha habido una crisis grave."]],
                           say=[1])]),
        card("Notes",
             "Ha habido is impersonal: it stays singular even with plural nouns (ha habido muchos problemas). The gerund of perder is perdiendo, and the gerund of buscar is buscando.",
             examples=[
                 ex("Los vecinos han estado trabajando todo el mes.", "The neighbors have been working all month.", "han estado trabajando"),
                 ex("Ha habido muchos problemas este año.", "There have been many problems this year.", "Ha habido"),
             ]),
    ],
    exercises=[
        M("Which pattern means “had been losing money”?", "había estado perdiendo dinero", ["ha estado perdiendo dinero", "perdió dinero", "habrá perdido dinero"], "Había estado + gerund."),
        M("What does the participle agree with in “Las medidas habían sido respaldadas”?", "Las medidas", ["habían", "sido", "el gobierno"], "The thing."),
        M("Does “ha habido” change with plural nouns?", "No, it stays ha habido", ["Yes, han habido", "Yes, hemos habido", "Only in writing"], "Impersonal haber."),
        F("La empresa había estado ___ dinero durante meses.", "perdiendo", ["perder", "perdido", "perdió"], "Gerund of perder.", tr="The company had been losing money for months.", lemma="perder:ger"),
        F("Los vecinos han estado ___ todo el mes.", "trabajando", ["trabajar", "trabajado", "trabajó"], "Gerund of trabajar.", tr="The neighbors have been working all month.", lemma="trabajar:ger"),
        F("El plan ha sido ___ por el gobierno.", "aprobado", ["aprobar", "aprobando", "aprobó"], "Masculine singular: plan.", tr="The plan has been approved by the government.", lemma="aprobar:part"),
        F("Las medidas habían sido ___ por muchas personas.", "respaldadas", ["respaldado", "respaldada", "respaldar"], "Feminine plural: medidas.", tr="The measures had been backed by many people."),
        F("___ habido muchos problemas este año.", "Ha", ["Han", "Hemos", "He"], "Impersonal haber.", tr="There have been many problems this year.", lemma="haber:él"),
        F("La empresa ha estado ___ una solución.", "buscando", ["buscar", "buscado", "buscó"], "Gerund of buscar.", tr="The company has been looking for a solution.", lemma="buscar:ger"),
    ],
    verify=vpa("aprobar", "aprobado"),
)

# ---------------------------------------------------------------------------- 869
L869 = lesson(
    "Review: the present perfect subjunctive (haya + participle)",
    "Me alegra que hayan reconstruido el puente. Cuando hayan firmado, empezará la obra.",
    requires=["alegrar", "construir", "puente", "alcalde", "terminar", "firmar", "informe", "publicar", "obra", "vecino", "llegar", "dudar"],
    cards=[
        card("Forming it",
             "The present perfect subjunctive uses haber in the present subjunctive (haya, hayas, haya, hayamos, hayáis, hayan) + a past participle. "
             "It describes a completed action when the main clause expresses emotion, doubt, hope or a future condition.",
             tables=[table(["Persona", "Haber", "Ejemplo"],
                           [["yo", "haya", "Dudo que yo haya terminado."], ["tú", "hayas", "Espero que hayas llegado bien."],
                            ["él / ella / usted", "haya", "No creo que el alcalde haya firmado."], ["nosotros", "hayamos", "Ojalá hayamos terminado."],
                            ["vosotros", "hayáis", "Me alegra que hayáis llegado."], ["ellos / ustedes", "hayan", "Me alegra que hayan reconstruido el puente."]],
                           say=[1, 2])]),
        card("Where you will meet it",
             "Use it after emotion (me alegra que), doubt (dudo que, no creo que), hope (espero que, ojalá) and in future time clauses (cuando, en cuanto, hasta que). In a time clause, the main verb is often in the future or present.",
             examples=[
                 ex("Cuando los vecinos hayan firmado, empezará la obra.", "When the neighbors have signed, the work will start.", "hayan firmado"),
                 ex("En cuanto el gobierno haya publicado el informe, hablaremos.", "As soon as the government has published the report, we will talk.", "haya publicado"),
             ]),
    ],
    exercises=[
        M("What is the form of haber in the present perfect subjunctive?", "haya, hayas, haya…", ["he, has, ha…", "había, habías…", "habría, habrías…"], "Present subjunctive of haber."),
        M("Which triggers the present perfect subjunctive?", "No creo que…", ["Sé que…", "Es verdad que…", "Veo que…"], "Doubt."),
        M("Which sentence is about the future condition?", "Cuando hayan firmado, empezará la obra.", ["Cuando firmaron, empezó la obra.", "Cuando firman, empieza la obra.", "Firmaron la obra."], "Cuando + haya + participle."),
        F("Me alegra que ellos ___ reconstruido el puente.", "hayan", ["han", "hayas", "hubieran"], "Plural subject, subjunctive.", tr="I am glad that they have rebuilt the bridge.", lemma="haber:ellos:subj"),
        F("Espero que tú ___ llegado bien.", "hayas", ["has", "haya", "hubieras"], "Tú form.", tr="I hope you have arrived safely.", lemma="haber:tú:subj"),
        F("No creo que el alcalde ___ firmado todavía.", "haya", ["ha", "hayan", "hubiera"], "Singular subject.", tr="I do not think the mayor has signed yet.", lemma="haber:él:subj"),
        F("Cuando los vecinos hayan ___, empezará la obra.", "firmado", ["firmar", "firmando", "firmaron"], "Participle of firmar.", tr="When the neighbors have signed, the work will start.", lemma="firmar:part"),
        F("En cuanto el gobierno haya ___ el informe, hablaremos.", "publicado", ["publicar", "publicando", "publicó"], "Participle of publicar.", tr="As soon as the government has published the report, we will talk.", lemma="publicar:part"),
        F("Ojalá nosotros ___ terminado ya.", "hayamos", ["hemos", "hayan", "hubiéramos"], "Nosotros form.", tr="I hope we have finished on time.", lemma="haber:nosotros:subj"),
    ],
    verify=vpj("haber", "haya", "hayas", "haya", "hayamos", "hayáis", "hayan"),
)

# ---------------------------------------------------------------------------- 870
L870 = lesson(
    "Review: if-sentences about books and rights",
    "Si no existieran los derechos de autor, muchos escritores no podrían vivir de su trabajo.",
    requires=["derecho", "autor", "escritor", "libro", "existir", "poder", "vivir", "trabajo", "ley", "proteger", "dinero", "publicar"],
    cards=[
        card("Three kinds of if-sentences",
             "Real or likely: si + present, then present or future. Unreal now: si + imperfect subjunctive, then conditional. Unreal past: si + pluperfect subjunctive, then conditional perfect. "
             "The examples below discuss a debate. Opinions about how copyright affects creativity differ, so we present it as hypothetical reasoning.",
             tables=[table(["Tipo", "Ejemplo"],
                           [["real", "Si el autor firma, recibe un pago."],
                            ["irreal ahora", "Si no existieran los derechos de autor, muchos escritores no podrían vivir de su trabajo."],
                            ["irreal pasado", "Si la ley no hubiera protegido a los autores, habría habido menos libros."]],
                           say=[1])]),
        card("Reminder",
             "Never use the conditional or the future directly after si in these patterns. Remember that the order of the two clauses can change.",
             examples=[
                 ex("Habría menos libros si los autores no hubieran recibido protección.", "There would be fewer books if authors had not received protection.", "hubieran recibido"),
             ]),
    ],
    exercises=[
        M("Which pattern is “unreal now”?", "si + imperfect subjunctive, then conditional", ["si + present, then present", "si + pluperfect, then conditional perfect", "si + future"], "Imagined present."),
        M("Which pattern is “unreal past”?", "si + pluperfect subjunctive, then conditional perfect", ["si + present, then future", "si + imperfect, then conditional", "si + infinitive"], "Imagined past."),
        M("Why does the text call this “hypothetical reasoning”?", "Opinions about the effects differ", ["Because all experts agree", "Because it is a poem", "Because the law is secret"], "A debate."),
        F("Si no ___ los derechos de autor, muchos escritores tendrían menos ingresos.", "existieran", ["existen", "existirán", "existirían"], "Imagined present.", tr="If copyright did not exist, many writers would have less income.", lemma="existir:ellos:isubj"),
        F("Si la ley no hubiera protegido a los autores, habría ___ menos libros.", "habido", ["haber", "habiendo", "hubo"], "Participle of haber.", tr="If the law had not protected authors, there would have been fewer books.", lemma="haber:part"),
        F("Si el autor firma el contrato, ___ un pago.", "recibe", ["recibiera", "recibiría", "habría recibido"], "Real condition.", tr="If the author signs the contract, he receives a payment.", lemma="recibir:él"),
        F("Si yo ___ más dinero ahora, publicaría mi propio libro.", "tuviera", ["tengo", "tendré", "hubiera tenido"], "Imagined present.", tr="If I had more money now, I would publish my own book.", lemma="tener:yo:isubj"),
        F("Si ellos ___ publicado el libro antes, habrían ganado más lectores.", "hubieran", ["habían", "habrían", "han"], "Imagined past.", tr="If they had published the book earlier, they would have won more readers.", lemma="haber:ellos:isubj"),
        F("Los autores no podrían vivir de su trabajo si no ___ protegidos.", "estuvieran", ["están", "estarán", "estarían"], "Imagined present.", tr="Authors could not live from their work if they were not protected.", lemma="estar:ellos:isubj"),
    ],
    verify=vpq("existir", "existiera", "existieras", "existiera", "existiéramos", "existierais", "existieran"),
)

# ---------------------------------------------------------------------------- 871
L871 = lesson(
    "Intellectual property: derechos de autor, patente, marca",
    "Un autor tiene derechos sobre su libro. Un inventor puede registrar una patente.",
    requires=["derecho", "autor", "ley", "convenio", "copia", "marca", "patente", "pirata", "acuerdo", "país", "creador", "proteger"],
    cards=[
        card("Key words",
             "Intellectual property (la propiedad intelectual) protects creations of the mind. Copyright protects books, music, films and similar works. A patent protects an invention. A trademark protects a brand name or logo.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la propiedad intelectual", "intellectual property", "La propiedad intelectual protege las creaciones."],
                            ["los derechos de autor", "copyright", "Los derechos de autor protegen un libro."],
                            ["la patente", "patent", "El inventor registró una patente."],
                            ["la marca registrada", "registered trademark", "Ese nombre es una marca registrada."],
                            ["el convenio", "convention, agreement", "Varios países firmaron el convenio."],
                            ["la piratería", "piracy", "La piratería causa pérdidas."],
                            ["lucrarse", "to profit", "Los creadores quieren lucrarse de su obra."],
                            ["difundir", "to spread, circulate", "Internet permite difundir las obras."],
                            ["infringir", "to violate", "Copiar sin permiso puede infringir la ley."]],
                           say=[0, 2])]),
        card("History and debate (brief)",
             "International agreements on intellectual property go back to the nineteenth century. The Paris Convention (1883) deals with industrial property, such as patents and trademarks, and the Berne Convention (1886) deals with literary and artistic works. "
             "In the 1990s, the trade agreement known in Spanish as ADPIC (TRIPS in English) set minimum rules for many countries. People disagree about how strict the rules should be: some stress protecting creators, while others stress access to knowledge and culture.",
             examples=[
                 ex("El Convenio de Berna, del siglo diecinueve, protege obras literarias y artísticas.", "The Berne Convention, from the nineteenth century, protects literary and artistic works.", "Convenio de Berna"),
                 ex("Algunas personas quieren más protección y otras quieren más acceso a la cultura.", "Some people want more protection and others want more access to culture.", "más acceso"),
             ]),
    ],
    exercises=[
        M("What does a patent protect?", "An invention", ["A book", "A song", "A recipe name"], "Patente."),
        M("What does copyright protect?", "Books, music, films and similar works", ["Only buildings", "Only food", "Only land"], "Derechos de autor."),
        M("What do people debate about intellectual property rules?", "How strict they should be", ["Whether books exist", "Which day to celebrate", "How to spell the word"], "Protection versus access."),
        F("Un libro está protegido por los ___ de autor.", "derechos", ["convenios", "piratas", "inventos"], "Copyright.", tr="A book is protected by copyright."),
        F("El inventor registró una ___ para su máquina.", "patente", ["frontera", "copia", "piratería"], "Patent.", tr="The inventor registered a patent for his machine."),
        F("Copiar películas sin permiso es una forma de ___.", "piratería", ["patente", "marca", "convenio"], "Piracy.", tr="Copying movies without permission is a form of piracy."),
        F("Varios países ___ el convenio en el siglo diecinueve.", "firmaron", ["firmó", "firmamos", "firmaste"], "Plural subject.", tr="Several countries signed the convention in the nineteenth century.", lemma="firmar:ellos:pret"),
        F("Esa empresa tiene una ___ registrada para su logotipo.", "marca", ["patente", "copia", "piratería"], "A brand.", tr="That company has a registered trademark for its logo."),
        F("Los creadores quieren ___ de su trabajo.", "lucrarse", ["lucro", "lucraron", "lucrando"], "Infinitive after quieren.", tr="Creators want to profit from their work."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 872
L872 = lesson(
    "Review: what would have happened? (invented inventor story)",
    "Si la inventora hubiera registrado la patente, ahora tendría más ingresos.",
    requires=["invento", "registrar", "patente", "ingreso", "empresa", "fábrica", "idea", "máquina", "copiar", "vender", "tiempo", "éxito"],
    cards=[
        card("Practice with all hypothetical forms",
             "This invented story lets you review three forms: si + pluperfect subjunctive with the conditional perfect, mixed past and present with the simple conditional, and wishes with ojalá. The characters are fictional.",
             tables=[table(["Hecho (inventado)", "Posibilidad imaginaria"],
                           [["La inventora no registró la patente.", "Si la hubiera registrado, habría protegido su idea."],
                            ["Otra empresa copió la máquina.", "Si no la hubieran copiado, ella habría vendido más."],
                            ["Ahora tiene pocos ingresos.", "Si hubiera registrado la patente, ahora tendría más ingresos."],
                            ["Se arrepiente.", "Ojalá hubiera registrado la patente a tiempo."]],
                           say=[1])]),
        card("Check yourself",
             "The si-clause names the unreal past. The result clause names either a past result (habría + participle) or a present result (simple conditional).",
             examples=[
                 ex("Si hubiera registrado la patente, habría protegido su idea.", "If she had registered the patent, she would have protected her idea.", "habría protegido"),
                 ex("Si lo hubiera hecho, ahora tendría más ingresos.", "If she had done it, she would have more income now.", "tendría"),
             ]),
    ],
    exercises=[
        M("Which form follows “Si hubiera registrado la patente,” when the result is in the past?", "habría protegido", ["protegería", "protegió", "protegerá"], "Conditional perfect."),
        M("Which form is used when the result is in the present?", "the simple conditional", ["the preterite", "the future", "the present"], "Ahora tendría."),
        M("What does “Ojalá hubiera registrado la patente a tiempo” express?", "A regret", ["A command", "A prediction", "A polite request"], "Past regret."),
        F("Si ella ___ registrado la patente, habría protegido su idea.", "hubiera", ["habría", "había", "ha"], "Si + hubiera.", tr="If she had registered the patent, she would have protected her idea.", lemma="haber:ella:isubj"),
        F("Si no la hubieran copiado, ella ___ vendido más.", "habría", ["había", "hubo", "habrá"], "Conditional perfect.", tr="If they had not copied it, she would have sold more.", lemma="haber:ella:cond"),
        F("Si hubiera registrado la patente, ahora ___ más ingresos.", "tendría", ["tuvo", "tiene", "tendrá"], "Present result: conditional.", tr="If she had registered the patent, she would have more income now.", lemma="tener:ella:cond"),
        F("Ojalá ella hubiera ___ la patente a tiempo.", "registrado", ["registrar", "registrando", "registró"], "Participle of registrar.", tr="I wish she had registered the patent in time.", lemma="registrar:part"),
        F("Si ellos ___ copiado la máquina, ella habría ganado más.", "no hubieran", ["no habían", "no habrían", "no han"], "Si + hubieran.", tr="If they had not copied the machine, she would have earned more."),
        F("Habríamos ayudado a la inventora si ___ sabido su problema.", "hubiéramos", ["habíamos", "habríamos", "hemos"], "Si + hubiéramos.", tr="We would have helped the inventor if we had known her problem.", lemma="haber:nosotros:isubj"),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 873
L873 = lesson(
    "Review: government, branches and ideologies",
    "En una democracia, el pueblo elige a sus gobernantes. El poder legislativo hace las leyes.",
    requires=["rey", "reina", "ley", "poder", "legislativo", "ejecutivo", "judicial", "tribunal", "votar", "elegir", "partido", "gobernar"],
    cards=[
        card("Words to recognize",
             "These words are the foundation for reading political news. Notice that poder (power) is also a verb. Here it is a noun.",
             tables=[table(["Palabra", "English", "Ejemplo"],
                           [["la monarquía", "monarchy", "En una monarquía hay un rey o una reina."],
                            ["la república", "republic", "En muchas repúblicas hay un presidente."],
                            ["la democracia", "democracy", "En una democracia el pueblo elige."],
                            ["la dictadura", "dictatorship", "En una dictadura una persona o un grupo concentra el poder."],
                            ["el poder legislativo", "legislative branch", "El poder legislativo hace las leyes."],
                            ["el poder ejecutivo", "executive branch", "El presidente dirige el poder ejecutivo."],
                            ["el poder judicial", "judicial branch", "El poder judicial interpreta las leyes."],
                            ["el partido político", "political party", "Cada partido defiende ideas diferentes."],
                            ["la ideología", "ideology", "Una ideología es un conjunto de ideas."],
                            ["votar, elegir", "to vote, to elect", "Los ciudadanos votan y eligen."]],
                           say=[0, 2])]),
        card("A neutral note",
             "Political words can carry strong feelings. In reports, journalists attribute opinions to sources and avoid presenting one opinion as a fact. Words like dictadura and democracia are used by people from many different positions, and they may disagree about which label fits a particular country.",
             examples=[
                 ex("Los ciudadanos votan y eligen a sus representantes.", "Citizens vote and choose their representatives.", "votan"),
                 ex("Según el periódico, el partido propone una ley nueva.", "According to the newspaper, the party proposes a new law.", "Según el periódico"),
             ]),
    ],
    exercises=[
        M("Which government is led by a king or queen?", "A monarchy", ["A republic", "A democracy", "An embassy"], "Monarquía."),
        M("Which branch makes laws?", "El poder legislativo", ["El poder ejecutivo", "El poder judicial", "El poder militar"], "Legislativo."),
        M("Which word means a set of ideas about politics?", "ideología", ["monarquía", "tribunal", "frontera"], "Ideología."),
        F("En una ___, el pueblo elige a sus gobernantes.", "democracia", ["dictadura", "monarquía", "peste"], "Citizens choose.", tr="In a democracy, the people choose their rulers."),
        F("El poder ___ aprueba las leyes.", "legislativo", ["judicial", "ejecutivo", "militar"], "Makes laws.", tr="The legislative branch passes laws."),
        F("El poder ___ interpreta las leyes en los tribunales.", "judicial", ["legislativo", "ejecutivo", "literario"], "Courts.", tr="The judicial branch interprets the laws in the courts."),
        F("El presidente dirige el poder ___.", "ejecutivo", ["legislativo", "judicial", "poético"], "Executive.", tr="The president leads the executive branch."),
        F("Cada partido político defiende una ___ diferente.", "ideología", ["montaña", "cosecha", "carta"], "Set of ideas.", tr="Each political party defends a different ideology."),
        F("En una ___, una persona o un grupo concentra el poder y hay pocas libertades.", "dictadura", ["democracia", "república", "ideología"], "Power is concentrated.", tr="In a dictatorship, one person or one group concentrates power and there are few freedoms."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 874
L874 = lesson(
    "Review: international organizations and their acronyms",
    "La OMS se ocupa de la salud. La OTAN es una alianza. La OPEP reúne a países productores de petróleo.",
    requires=["organización", "mundial", "salud", "educación", "ciencia", "cultura", "banco", "policía", "petróleo", "comercio", "país", "cooperación"],
    cards=[
        card("Spanish acronyms",
             "Spanish acronyms are often different from English ones because the words are in a different order. Learn the Spanish names and their jobs.",
             tables=[table(["Siglas", "Nombre", "Función general"],
                           [["ONU", "Organización de las Naciones Unidas", "paz, derechos y cooperación entre países"],
                            ["OMS", "Organización Mundial de la Salud", "salud pública"],
                            ["UNESCO", "Organización de las Naciones Unidas para la Educación, la Ciencia y la Cultura", "educación, ciencia y cultura"],
                            ["CEPAL", "Comisión Económica para América Latina y el Caribe", "estudios económicos de la región"],
                            ["OTAN", "Organización del Tratado del Atlántico Norte", "alianza de defensa"],
                            ["OPEP", "Organización de Países Exportadores de Petróleo", "países productores de petróleo"],
                            ["OMC", "Organización Mundial del Comercio", "reglas del comercio"],
                            ["INTERPOL", "Organización Internacional de Policía Criminal", "cooperación entre policías"],
                            ["BM", "Banco Mundial", "préstamos y programas de desarrollo"]],
                           say=[1, 2])]),
        card("Pronunciation note",
             "Most acronyms are pronounced as words (ONU, OTAN, OPEP, UNESCO, CEPAL, INTERPOL). OMS, OMC and BM are usually spelled out letter by letter.",
             examples=[
                 ex("La CEPAL estudia la economía de América Latina y el Caribe.", "ECLAC studies the economy of Latin America and the Caribbean.", "La CEPAL"),
                 ex("La OMS se ocupa de la salud pública.", "WHO handles public health.", "La OMS"),
             ]),
    ],
    exercises=[
        M("Which organization handles public health?", "La OMS", ["La OPEP", "La OTAN", "La UNESCO"], "Salud."),
        M("Which one is about education, science and culture?", "La UNESCO", ["La OMC", "El Banco Mundial", "La INTERPOL"], "Educación, ciencia y cultura."),
        M("Which one brings together oil-exporting countries?", "La OPEP", ["La CEPAL", "La OMS", "La ONU"], "Petróleo."),
        F("La ___ se ocupa de la salud pública.", "OMS", ["OPEP", "OTAN", "CEPAL"], "Salud.", tr="The WHO handles public health."),
        F("La ___ estudia la economía de América Latina y el Caribe.", "CEPAL", ["OMS", "OTAN", "INTERPOL"], "Regional economy.", tr="ECLAC studies the economy of Latin America and the Caribbean."),
        F("La ___ es una alianza de defensa.", "OTAN", ["OMS", "OPEP", "UNESCO"], "Defense alliance.", tr="NATO is a defense alliance."),
        F("La ___ ayuda a las policías de diferentes países a cooperar.", "INTERPOL", ["OPEP", "OMS", "CEPAL"], "Police cooperation.", tr="INTERPOL helps police forces of different countries to cooperate."),
        F("La ___ trabaja por la educación, la ciencia y la cultura.", "UNESCO", ["OPEP", "OTAN", "INTERPOL"], "Education, science, culture.", tr="UNESCO works for education, science and culture."),
        F("La ___ reúne a muchos países para hablar de paz y cooperación.", "ONU", ["OPEP", "INTERPOL", "CEPAL"], "United Nations.", tr="The UN brings many countries together to talk about peace and cooperation."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 875
L875 = lesson(
    "Diego Rivera: murals of work and history",
    "Diego Rivera nació en México y pintó murales sobre el trabajo y la historia.",
    requires=["pintor", "pintar", "pintura", "arte", "fábrica", "trabajador", "historia", "ciudad", "museo", "nacer", "viajar", "obra"],
    cards=[
        card("Who was Diego Rivera?",
             "Diego Rivera (1886–1957) was a Mexican painter and one of the best-known muralists of the twentieth century. A mural is a large painting made directly on a wall. "
             "His murals show workers, farmers, factories and scenes from history. He supported left-wing causes, and some of his works produced political controversy.",
             tables=[table(["Dato", "Información"],
                           [["Nacionalidad", "mexicano"], ["Oficio", "pintor y muralista"],
                            ["Temas", "el trabajo, la industria y la historia"],
                            ["Obra en Estados Unidos", "murales sobre la industria en un museo de Detroit"]],
                           say=[1])]),
        card("Detroit",
             "In the early 1930s, a car-company leader helped commission a series of murals about local industry for a museum in Detroit. "
             "The murals show factory workers, machines and the link between industry and science. Later artists and photographers also documented the changes in that city, which shows how art can serve as a record of different periods.",
             examples=[
                 ex("Rivera pintó fábricas, máquinas y trabajadores.", "Rivera painted factories, machines and workers.", "pintó"),
                 ex("Algunos de sus murales causaron controversia política.", "Some of his murals caused political controversy.", "causaron"),
             ]),
    ],
    exercises=[
        M("What is a mural?", "A large painting made on a wall", ["A small drawing", "A type of statue", "A book cover"], "Painted on a wall."),
        M("What themes appear in Rivera's murals?", "Work, industry and history", ["Only landscapes", "Only portraits of kings", "Only fruit"], "El trabajo, la industria y la historia."),
        M("How can art serve, according to the lesson?", "As a record of different periods", ["As a weapon", "As a map", "As a menu"], "A record."),
        F("Diego Rivera ___ en México.", "nació", ["nacieron", "nací", "naciste"], "Singular subject.", tr="Diego Rivera was born in Mexico.", lemma="nacer:él:pret"),
        F("Rivera ___ fábricas, máquinas y trabajadores.", "pintó", ["pintaron", "pinté", "pintamos"], "Singular subject.", tr="Rivera painted factories, machines and workers.", lemma="pintar:él:pret"),
        F("Los murales ___ la vida de los trabajadores.", "muestran", ["muestra", "mostramos", "muestras"], "Plural subject.", tr="The murals show the life of the workers.", lemma="mostrar:ellos"),
        F("Algunos murales ___ controversia política.", "causaron", ["causó", "causé", "causamos"], "Plural subject.", tr="Some murals caused political controversy.", lemma="causar:ellos:pret"),
        F("Un mural es una pintura grande en una ___.", "pared", ["carta", "silla", "ventana"], "On a wall.", tr="A mural is a large painting on a wall."),
        F("Muchos turistas ___ el museo para ver las pinturas.", "visitan", ["visita", "visitamos", "visitas"], "Plural subject.", tr="Many tourists visit the museum to see the paintings.", lemma="visitar:ellos"),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 876
L876 = lesson(
    "Describing places and works: desolador, minucioso, pintoresco, inverosímil…",
    "El mural es minucioso y la historia es inverosímil. El barrio es pintoresco.",
    requires=["sencillo", "fantástico", "impresionante", "profundo", "barrio", "pared", "historia", "calle", "ciudad", "paisaje", "tormenta", "detalle"],
    cards=[
        card("Thirteen adjectives",
             "Most adjectives ending in -o change to -a, -os, -as. Adjectives ending in -dor take -dora. Adjectives ending in -e or -nte stay the same in the feminine.",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["agobiante", "overwhelming, oppressive", "El calor era agobiante."],
                            ["apremiante", "pressing, urgent", "Hay una necesidad apremiante."],
                            ["atroz", "atrocious, terrible", "Fue un crimen atroz."],
                            ["desolador, desoladora", "bleak, devastating", "La escena era desoladora."],
                            ["disparatado, disparatada", "absurd, crazy", "Era un plan disparatado."],
                            ["ficticio, ficticia", "fictional", "Es un personaje ficticio."],
                            ["hondo, honda", "deep", "Sintió una pena honda."],
                            ["inigualable", "unmatched", "Tiene una belleza inigualable."],
                            ["inverosímil", "implausible", "La historia es inverosímil."],
                            ["minucioso, minuciosa", "meticulous, detailed", "Es un mural muy minucioso."],
                            ["pintoresco, pintoresca", "picturesque", "Vivimos en un barrio pintoresco."],
                            ["sencillo, sencilla", "simple", "El estilo es sencillo."],
                            ["tormentoso, tormentosa", "stormy", "Fue una noche tormentosa."]],
                           say=[0, 2])]),
        card("Plural of atroz",
             "Atroz ends in -z, so the plural is atroces. Inigualable and inverosímil do not change for gender. The plural of inigualable is inigualables, and the plural of inverosímil is inverosímiles.",
             examples=[
                 ex("Fueron crímenes atroces.", "They were atrocious crimes.", "atroces"),
                 ex("Las historias inverosímiles pueden ser divertidas.", "Implausible stories can be fun.", "inverosímiles"),
             ]),
    ],
    exercises=[
        M("What is the plural of “atroz”?", "atroces", ["atrozes", "atrozos", "atroz"], "-z → -ces."),
        M("What does “inverosímil” mean?", "Implausible", ["Very large", "Very old", "Very noisy"], "Hard to believe."),
        M("Which adjective means “picturesque”?", "pintoresco", ["tormentoso", "disparatado", "agobiante"], "Pintoresco."),
        F("El mural es muy ___ y muestra cada detalle.", "minucioso", ["minuciosa", "minuciosos", "minuciosas"], "Masculine singular: mural.", tr="The mural is very meticulous and shows every detail.", ),
        F("La escena era ___ y todos guardamos silencio.", "desoladora", ["desolador", "desoladoras", "desolados"], "Feminine singular.", tr="The scene was bleak and we all kept silent."),
        F("Fue una noche ___ con mucho viento y lluvia.", "tormentosa", ["tormentoso", "tormentosas", "tormentosos"], "Feminine singular.", tr="It was a stormy night with a lot of wind and rain."),
        F("Fueron crímenes ___.", "atroces", ["atroz", "atrozes", "atrozas"], "Plural.", tr="They were atrocious crimes."),
        F("Es un personaje ___; no existió.", "ficticio", ["ficticia", "ficticios", "ficticias"], "Masculine singular.", tr="He is a fictional character; he never existed."),
        F("Es un barrio ___ con casas de muchos colores.", "pintoresco", ["pintoresca", "pintorescos", "pintorescas"], "Masculine singular: barrio.", tr="It is a picturesque neighborhood with houses of many colors."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 877
L877 = lesson(
    "Describing people: pragmático, atrevido, cobarde, benévolo, fiero…",
    "Es una persona pragmática y atrevida. No es cobarde. Tiene un carácter fiero.",
    requires=["persona", "carácter", "decisión", "amigo", "jefe", "vecino", "problema", "valiente", "miedo", "ayuda", "idea", "vida"],
    cards=[
        card("Nine adjectives for character",
             "These adjectives describe a person's attitude or personality. Use them with ser. Cobarde and ambivalente do not change in the feminine.",
             tables=[table(["Adjetivo", "English", "Ejemplo"],
                           [["ambivalente", "ambivalent", "Tiene sentimientos ambivalentes."],
                            ["arraigado, arraigada", "deep-rooted", "Es una costumbre muy arraigada."],
                            ["atrevido, atrevida", "bold, daring", "Es una persona atrevida."],
                            ["benévolo, benévola", "kind, generous", "El jefe fue benévolo con ellos."],
                            ["cobarde", "cowardly", "No fue cobarde; pidió ayuda."],
                            ["fiero, fiera", "fierce", "Tiene un carácter fiero."],
                            ["inescrupuloso, inescrupulosa", "unscrupulous", "Un comerciante inescrupuloso engañó a los clientes."],
                            ["pragmático, pragmática", "practical, pragmatic", "Es una persona pragmática."],
                            ["controvertido, controvertida", "controversial", "Su idea es controvertida."]],
                           say=[0, 2])]),
        card("Tone",
             "Calling someone cobarde or inescrupuloso is a strong judgment. In careful speech, people often describe the behavior (por ejemplo, no dijo la verdad) rather than label the person.",
             examples=[
                 ex("Es una persona pragmática; busca soluciones concretas.", "She is a pragmatic person; she looks for concrete solutions.", "pragmática"),
                 ex("Es una costumbre muy arraigada en el pueblo.", "It is a deep-rooted custom in the town.", "arraigada"),
             ]),
    ],
    exercises=[
        M("What does “arraigado” mean?", "Deep-rooted", ["Very fast", "Very thin", "Very rare"], "Rooted."),
        M("Which adjective stays the same for masculine and feminine?", "cobarde", ["atrevido", "pragmático", "benévolo"], "-e."),
        M("What does “pragmático” describe?", "A practical person", ["A shy person", "A tired person", "A famous person"], "Practical."),
        F("Mi hermana es una persona muy ___ y siempre busca soluciones.", "pragmática", ["pragmático", "pragmáticas", "pragmáticos"], "Feminine singular.", tr="My sister is a very pragmatic person and always looks for solutions."),
        F("Es una costumbre muy ___ en el pueblo.", "arraigada", ["arraigado", "arraigadas", "arraigados"], "Feminine singular: costumbre.", tr="It is a very deep-rooted custom in the town."),
        F("Los jefes fueron ___ con los nuevos empleados.", "benévolos", ["benévolo", "benévola", "benévolas"], "Masculine plural.", tr="The bosses were generous with the new employees."),
        F("Ellas no son ___; piden ayuda cuando la necesitan.", "cobardes", ["cobarde", "cobardas", "cobardos"], "Plural.", tr="They are not cowards; they ask for help when they need it."),
        F("Tiene un carácter ___ y no le gusta perder.", "fiero", ["fiera", "fieros", "fieras"], "Masculine singular: carácter.", tr="He has a fierce character and does not like to lose."),
        F("Su idea es ___: algunas personas la apoyan y otras no.", "controvertida", ["controvertido", "controvertidas", "controvertidos"], "Feminine singular: idea.", tr="Her idea is controversial: some people support it and others do not."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 878
L878 = lesson(
    "Reading: Piedranegra, un mural y unas fotografías (invented text)",
    "En Piedranegra, una ciudad imaginaria, el mural y las fotografías cuentan dos épocas.",
    requires=["ciudad", "fábrica", "trabajador", "pintor", "pared", "edificio", "vacío", "fotógrafo", "libro", "esperanza", "invertir", "autoridad"],
    cards=[
        card("Texto inventado, primera parte",
             "Piedranegra is an imaginary city. The text uses ser/estar/haber in the past, the pluperfect subjunctive and the present perfect subjunctive.",
             examples=[
                 ex("A principios del siglo veinte, la fábrica de motores de Piedranegra era famosa y llegaban trabajadores de muchos países.", "At the beginning of the twentieth century, the engine factory of Piedranegra was famous and workers came from many countries.", "era famosa"),
                 ex("Un pintor de la ciudad pintó un mural enorme sobre la vida en la fábrica.", "A painter from the city painted an enormous mural about life in the factory.", "pintó"),
                 ex("Años después, la fábrica cerró y los edificios quedaron vacíos.", "Years later, the factory closed and the buildings were left empty.", "quedaron"),
                 ex("Una fotógrafa publicó un libro con imágenes de calles solitarias y casas abandonadas.", "A photographer published a book with images of lonely streets and abandoned houses.", "publicó"),
             ]),
        card("Texto inventado, segunda parte",
             "People in the city have different explanations.",
             examples=[
                 ex("Algunos dicen que el mural y las fotografías cuentan dos mitades de la misma historia.", "Some say the mural and the photographs tell two halves of the same story.", "cuentan"),
                 ex("Otros piensan que la ciudad no habría caído si las autoridades hubieran invertido a tiempo.", "Others think the city would not have fallen if the authorities had invested in time.", "hubieran invertido"),
                 ex("Un vecino dijo: Ojalá los políticos se hayan dado cuenta de lo que pasó.", "A neighbor said: I hope the politicians have realized what happened.", "se hayan dado cuenta"),
                 ex("Cuando hayan decidido ayudar, quizá la ciudad vuelva a tener esperanza.", "When they have decided to help, perhaps the city will have hope again.", "hayan decidido"),
             ]),
    ],
    exercises=[
        M("What did the painter do?", "He painted a mural about life in the factory", ["He closed the factory", "He wrote a law", "He built a bridge"], "Un mural enorme."),
        M("What did the photographer publish?", "A book of images of empty streets and abandoned houses", ["A map", "A recipe book", "A newspaper"], "Un libro con imágenes."),
        M("What do some people say about the mural and the photographs?", "They tell two halves of one story", ["They are identical", "They are false", "They are about another city"], "Dos mitades."),
        M("What do others think?", "The city would not have fallen if authorities had invested in time", ["The city never changed", "The factory never existed", "The photographer was unfair"], "Si hubieran invertido…"),
        F("A principios del siglo, la fábrica ___ famosa y llegaban trabajadores de muchos países.", "era", ["fue", "eran", "estaba"], "Description in the past.", tr="At the beginning of the century, the factory was famous and workers came from many countries.", lemma="ser:él:impf"),
        F("Años después, los edificios ___ vacíos.", "quedaron", ["quedó", "quedé", "quedamos"], "Plural subject.", tr="Years later, the buildings were left empty.", lemma="quedar:ellos:pret"),
        F("La ciudad no habría caído si las autoridades ___ invertido a tiempo.", "hubieran", ["habían", "habrían", "han"], "Si + hubieran.", tr="The city would not have fallen if the authorities had invested in time.", lemma="haber:ellos:isubj"),
        F("Ojalá los políticos se ___ dado cuenta ya de lo que pasó.", "hayan", ["han", "hayas", "hubieran"], "Ojalá + hayan.", tr="I hope the politicians have realized what happened.", lemma="haber:ellos:subj"),
        F("Cuando hayan ___ ayudar, quizá la ciudad vuelva a tener esperanza.", "decidido", ["decidir", "decidiendo", "decidieron"], "Participle of decidir.", tr="When they have decided to help, perhaps the city will have hope again.", lemma="decidir:part"),
    ],
    verify=vpj("haber", "haya", "hayas", "haya", "hayamos", "hayáis", "hayan"),
)

# ---------------------------------------------------------------------------- 879
L879 = lesson(
    "Review: como si, ojalá and quisiera",
    "Actúa como si no supiera nada. Ojalá lleguen pronto. Quisiéramos una habitación doble.",
    requires=["actuar", "saber", "llegar", "decir", "tener", "querer", "habitación", "doble", "verdad", "pronto", "llover", "año"],
    cards=[
        card("Quick map",
             "Como si + imperfect subjunctive (or pluperfect subjunctive for an earlier imagined situation). Ojalá + present subjunctive for a possible hope, + imperfect subjunctive for an unlikely present wish, + pluperfect subjunctive for a past regret. "
             "Quisiera + infinitive when the subject is the same, quisiera que + imperfect subjunctive when the subjects differ.",
             tables=[table(["Estructura", "Ejemplo"],
                           [["como si + imperfecto", "Actúa como si no supiera nada."],
                            ["como si + pluscuamperfecto", "Habla como si hubiera visto todo."],
                            ["ojalá + presente", "Ojalá lleguen pronto."],
                            ["ojalá + imperfecto", "Ojalá tuviera más tiempo."],
                            ["ojalá + pluscuamperfecto", "Ojalá no hubiera llovido tanto."],
                            ["quisiera + infinitivo", "Quisiera viajar este año."],
                            ["quisiera que + imperfecto", "Quisiera que me dijeras la verdad."]],
                           say=[1])]),
        card("Reminder",
             "None of these structures accepts the future or the conditional right after the key word. Como si takes the imperfect or pluperfect subjunctive. Ojalá takes the present, present perfect, imperfect or pluperfect subjunctive, depending on the meaning.",
             examples=[
                 ex("Nosotros quisiéramos una habitación doble, por favor.", "We would like a double room, please.", "quisiéramos"),
             ]),
    ],
    exercises=[
        M("Which mood follows “como si”?", "The imperfect subjunctive", ["The present subjunctive", "The future", "The conditional"], "Como si + imperfect."),
        M("Which form expresses regret about the past?", "Ojalá + pluperfect subjunctive", ["Ojalá + present subjunctive", "Quisiera + infinitive", "Como si + infinitive"], "Past regret."),
        M("When do you use “quisiera que”?", "When the subjects are different", ["When the subjects are the same", "Only in questions", "Only in the past"], "Different subjects."),
        F("Actúa como si no ___ nada.", "supiera", ["sabe", "sabrá", "sabría"], "Imperfect subjunctive.", tr="He acts as if he did not know anything.", lemma="saber:él:isubj"),
        F("Ojalá ellos ___ pronto.", "lleguen", ["llegan", "llegarán", "llegarían"], "Present subjunctive.", tr="I hope they arrive soon.", lemma="llegar:ellos:subj"),
        F("Quisiera que tú me ___ la verdad.", "dijeras", ["dices", "dirás", "digas"], "Imperfect subjunctive.", tr="I would like you to tell me the truth.", lemma="decir:tú:isubj"),
        F("Ojalá no ___ llovido tanto el año pasado.", "hubiera", ["había", "habría", "ha"], "Pluperfect subjunctive.", tr="I wish it had not rained so much last year.", lemma="haber:él:isubj"),
        F("Nosotros ___ una habitación doble, por favor.", "quisiéramos", ["quisieran", "quisiera", "quisierais"], "Nosotros form.", tr="We would like a double room, please.", lemma="querer:nosotros:isubj"),
        F("Habla como si ___ visto todo.", "hubiera", ["había", "habría", "ha"], "Earlier imagined situation.", tr="He talks as if he had seen everything.", lemma="haber:él:isubj"),
    ],
    verify=vpq("decir", "dijera", "dijeras", "dijera", "dijéramos", "dijerais", "dijeran") + vpq("saber", "supiera", "supieras", "supiera", "supiéramos", "supierais", "supieran"),
)

# ---------------------------------------------------------------------------- 880
L880 = lesson(
    "Review: conditional perfect and pluperfect subjunctive",
    "Si hubieran llegado antes, habrían visto el final. Habríamos ido, pero llovía.",
    requires=["llegar", "ver", "ir", "estudiar", "aprobar", "decir", "comprar", "leer", "volver", "mensaje", "casa", "final"],
    cards=[
        card("Two forms, several jobs",
             "Si-clause: hubiera / hubiese + participle. Result: habría + participle. The same participles are used in all perfect tenses. "
             "The conditional perfect also works alone for what would have happened (Habríamos ido, pero llovía) and for guesses about something that happened before a past moment (Ya habrían salido).",
             tables=[table(["Función", "Ejemplo"],
                           [["irreal en el pasado", "Si hubieran llegado antes, habrían visto el final."],
                            ["posibilidad que no ocurrió", "Habríamos ido, pero llovía."],
                            ["suposición sobre el pasado", "Nadie contestó. Ya habrían salido."],
                            ["pesar", "Ojalá hubiera estudiado más."]],
                           say=[1])]),
        card("Irregular participles",
             "abrir → abierto, decir → dicho, escribir → escrito, hacer → hecho, poner → puesto, ver → visto, volver → vuelto, romper → roto. The participle of leer is leído, which has an accent.",
             examples=[
                 ex("Si hubiera leído el mensaje, habría contestado.", "If I had read the message, I would have answered.", "hubiera leído"),
             ]),
    ],
    exercises=[
        M("Which sentence is correct?", "Si hubieran llegado antes, habrían visto el final.", ["Si habrían llegado antes, habrían visto el final.", "Si hubieran llegado antes, ven el final.", "Si llegaron antes, habrían visto el final."], "Si + hubieran; result habrían."),
        M("What does “Habríamos ido, pero llovía” mean?", "We would have gone, but it was raining", ["We went, and it rained", "We will go if it rains", "We had gone because it rained"], "Would have gone."),
        M("What is the participle of “abrir”?", "abierto", ["abrido", "abriendo", "abrí"], "Abierto."),
        F("Si tú ___ estudiado, habrías aprobado.", "hubieras", ["habías", "habrías", "has"], "Tú form.", tr="If you had studied, you would have passed.", lemma="haber:tú:isubj"),
        F("Nosotros ___ ido, pero llovía mucho.", "habríamos", ["habíamos", "hemos", "habremos"], "Conditional perfect.", tr="We would have gone, but it was raining a lot.", lemma="haber:nosotros:cond"),
        F("Si ella hubiera ___ la verdad, nadie habría sufrido.", "dicho", ["decido", "diciendo", "dijo"], "Participle of decir.", tr="If she had told the truth, nobody would have suffered.", lemma="decir:part"),
        F("Ellos habrían ___ la casa, pero no tenían dinero.", "comprado", ["comprar", "comprando", "compraron"], "Participle of comprar.", tr="They would have bought the house, but they did not have money.", lemma="comprar:part"),
        F("Si yo hubiera ___ el mensaje, habría contestado.", "leído", ["leer", "leyendo", "leyó"], "Participle of leer.", tr="If I had read the message, I would have answered.", lemma="leer:part"),
        F("Ojalá ella ___ vuelto antes.", "hubiera", ["había", "habría", "ha"], "Ojalá + hubiera.", tr="I wish she had come back earlier.", lemma="haber:ella:isubj"),
    ],
    verify=vpa("leer", "leído") + vpa("volver", "vuelto") + vpa("comprar", "comprado"),
)

# ---------------------------------------------------------------------------- 881
L881 = lesson(
    "Review: connectors and set expressions",
    "Estudió mucho; sin embargo, no aprobó. A pesar de la lluvia, salimos.",
    requires=["embargo", "obstante", "tanto", "pesar", "aunque", "además", "cambio", "mientras", "fin", "golpe", "cabo", "encima"],
    cards=[
        card("Connecting ideas",
             "Connectors show how two ideas relate. Contrast: sin embargo, no obstante, aunque, a pesar de. Result: por lo tanto, por eso, así que. Addition: además. Comparison: en cambio, por un lado… por otro.",
             tables=[table(["Conector", "Función", "Ejemplo"],
                           [["sin embargo / no obstante", "contraste", "Estudió mucho; sin embargo, no aprobó."],
                            ["a pesar de + nombre", "contraste", "A pesar de la lluvia, salimos."],
                            ["aunque", "contraste", "Salimos aunque llovía."],
                            ["por lo tanto / por eso", "resultado", "No tenía dinero; por lo tanto, no compró el libro."],
                            ["además", "adición", "Es un libro largo; además, es difícil."],
                            ["en cambio", "comparación", "Mi hermano estudia ciencias; yo, en cambio, estudio arte."]],
                           say=[2])]),
        card("From this stretch of the course",
             "Add these fixed phrases from the unit: de golpe (suddenly), al cabo de (after), a partir de entonces (from then on), desde luego (of course), en fin (anyway), ni mucho menos (far from it), por encima de (above).",
             examples=[
                 ex("Al cabo de una hora, terminó la reunión.", "After an hour, the meeting ended.", "Al cabo de"),
                 ex("No es fácil, ni mucho menos.", "It is not easy, not by a long shot.", "ni mucho menos"),
             ]),
    ],
    exercises=[
        M("Which means “however”?", "sin embargo", ["por lo tanto", "además", "por eso"], "Contrast."),
        M("Which means “therefore”?", "por lo tanto", ["sin embargo", "aunque", "a pesar de"], "Result."),
        M("Which means “despite”?", "a pesar de", ["por eso", "además", "así que"], "Contrast."),
        F("Estudié mucho; ___, no aprobé el examen.", "sin embargo", ["por lo tanto", "además", "es decir"], "Contrast.", tr="I studied a lot; however, I did not pass the exam."),
        F("No tenía dinero; ___, no compró el libro.", "por lo tanto", ["sin embargo", "no obstante", "a pesar de"], "Result.", tr="He had no money; therefore, he did not buy the book."),
        F("___ de la lluvia, salimos a caminar.", "A pesar", ["Por", "Con", "En"], "A pesar de.", tr="Despite the rain, we went out for a walk."),
        F("Salimos a caminar ___ llovía.", "aunque", ["así que", "por lo tanto", "sin embargo"], "Contrast.", tr="We went out for a walk even though it was raining."),
        F("Hizo mucho calor; ___, abrimos las ventanas.", "por eso", ["aunque", "a pesar de", "ni mucho menos"], "Result.", tr="It was very hot; that is why we opened the windows."),
        F("Mi hermano estudia ciencias; yo, ___, estudio arte.", "en cambio", ["por eso", "a pesar de", "aunque"], "Comparison.", tr="My brother studies science; I, on the other hand, study art."),
    ],
    verify=[],
)

# ---------------------------------------------------------------------------- 882
L882 = lesson(
    "Review: who wrote or made what? (culture review)",
    "Cervantes escribió Don Quijote. Botero pintó figuras voluminosas. Mistral ganó el Nobel.",
    requires=["escribir", "pintar", "ganar", "novela", "pintor", "poeta", "escritor", "premio", "canción", "película", "obra", "autor"],
    cards=[
        card("Quick fact sheet",
             "These facts come from the lessons in this unit. Use the preterite for completed actions of people in the past.",
             tables=[table(["Persona", "Qué hizo"],
                           [["Cervantes", "escribió Don Quijote"], ["Calderón de la Barca", "escribió La vida es sueño"],
                            ["Fernando Botero", "pintó figuras voluminosas"], ["Violeta Parra", "compuso canciones y creó arte textil"],
                            ["Rubén Darío", "fue una figura central del modernismo"], ["Gabriela Mistral", "ganó el Premio Nobel en mil novecientos cuarenta y cinco"],
                            ["Gabriel García Márquez", "escribió Cien años de soledad"], ["Miguel Ángel Asturias", "escribió El Señor Presidente"],
                            ["Mario Vargas Llosa", "escribió La ciudad y los perros"], ["Diego Rivera", "pintó murales sobre el trabajo y la historia"]],
                           say=[1])]),
        card("Practice sentence",
             "Notice that the subject often stays at the beginning, and the verb is in the third person singular.",
             examples=[
                 ex("García Márquez escribió Cien años de soledad.", "García Márquez wrote One Hundred Years of Solitude.", "escribió"),
                 ex("Mistral ganó el Premio Nobel en mil novecientos cuarenta y cinco.", "Mistral won the Nobel Prize in nineteen forty-five.", "ganó"),
             ]),
    ],
    exercises=[
        M("Who wrote Don Quijote?", "Cervantes", ["Darío", "Botero", "Asturias"], "Cervantes."),
        M("Which movement is Rubén Darío linked to?", "Modernismo", ["Realismo mágico", "El boom", "Romanticismo"], "Modernismo."),
        M("Who painted voluminous figures?", "Fernando Botero", ["Diego Rivera", "Violeta Parra", "Calderón"], "Botero."),
        M("Who wrote La ciudad y los perros?", "Mario Vargas Llosa", ["Gabriela Mistral", "Isabel Allende", "Julio Cortázar"], "Vargas Llosa."),
        F("Cervantes ___ Don Quijote.", "escribió", ["escribieron", "escribí", "escribimos"], "Singular subject.", tr="Cervantes wrote Don Quixote.", lemma="escribir:él:pret"),
        F("Botero ___ figuras voluminosas.", "pintó", ["pintaron", "pinté", "pintamos"], "Singular subject.", tr="Botero painted voluminous figures.", lemma="pintar:él:pret"),
        F("Violeta Parra ___ canciones.", "compuso", ["compusieron", "compuse", "compusimos"], "Singular subject.", tr="Violeta Parra composed songs.", lemma="componer:ella:pret"),
        F("Gabriela Mistral ___ el Premio Nobel en mil novecientos cuarenta y cinco.", "ganó", ["ganaron", "gané", "ganamos"], "Singular subject.", tr="Gabriela Mistral won the Nobel Prize in nineteen forty-five.", lemma="ganar:ella:pret"),
        F("García Márquez ___ Cien años de soledad.", "escribió", ["escribieron", "escribí", "escribimos"], "Singular subject.", tr="García Márquez wrote One Hundred Years of Solitude.", lemma="escribir:él:pret"),
    ],
    verify=vpp("componer", "compuse", "compusiste", "compuso", "compusimos", "compusisteis", "compusieron"),
)

# ---------------------------------------------------------------------------- 883
L883 = lesson(
    "Final reading: la feria del libro de Valdeluna (invented text)",
    "La feria del libro duró tres días. Hubo charlas, cuentos y mucho debate.",
    requires=["libro", "escritor", "derecho", "autor", "comercio", "niño", "cuento", "directora", "lector", "acceso", "repetir", "año"],
    cards=[
        card("Texto inventado, primera parte",
             "This final text uses many structures from the unit. Valdeluna is an imaginary town.",
             examples=[
                 ex("La feria del libro de Valdeluna duró tres días.", "The Valdeluna book fair lasted three days.", "duró"),
                 ex("El primer día hubo una charla sobre los derechos de autor.", "On the first day there was a talk about copyright.", "hubo"),
                 ex("La conferencista, una escritora, habló como si hubiera pasado años estudiando el tema.", "The speaker, a writer, spoke as if she had spent years studying the subject.", "como si hubiera pasado"),
                 ex("Dijo que, si los autores no tuvieran protección, muchos no podrían vivir de su trabajo.", "She said that if authors had no protection, many could not live from their work.", "tuvieran"),
                 ex("Pero también dijo que, si el acceso a los libros fuera más fácil, habría más lectores.", "But she also said that if access to books were easier, there would be more readers.", "fuera"),
             ]),
        card("Texto inventado, segunda parte",
             "The fair ends with wishes.",
             examples=[
                 ex("El segundo día, un editor explicó que el comercio de libros entre países ha crecido, aunque sigue habiendo desigualdades.", "On the second day, an editor explained that the book trade between countries has grown, although inequalities remain.", "ha crecido"),
                 ex("El tercer día, los niños escucharon cuentos.", "On the third day, the children listened to stories.", "escucharon"),
                 ex("Al final, la directora dijo: Ojalá hayamos inspirado a muchos lectores.", "At the end, the director said: I hope we have inspired many readers.", "hayamos inspirado"),
                 ex("La directora añadió: Quisiera que la feria se repitiera todos los años.", "The director added: I would like the fair to be repeated every year.", "se repitiera"),
             ]),
    ],
    exercises=[
        M("How long did the fair last?", "Three days", ["One day", "Two weeks", "A month"], "Tres días."),
        M("What was the first day's talk about?", "Copyright", ["Cooking", "Soccer", "Weather"], "Derechos de autor."),
        M("What did the speaker say about easier access to books?", "There would be more readers", ["There would be fewer books", "Nobody would read", "Writers would stop"], "Habría más lectores."),
        M("What did the director wish for?", "That the fair be repeated every year", ["That it never happen again", "That it be shorter", "That it change towns"], "Quisiera que se repitiera."),
        F("La conferencista habló como si ___ pasado años estudiando el tema.", "hubiera", ["había", "habría", "ha"], "Como si + hubiera.", tr="The speaker spoke as if she had spent years studying the subject.", lemma="haber:ella:isubj"),
        F("Si los autores no ___ protección, muchos no podrían vivir de su trabajo.", "tuvieran", ["tienen", "tendrán", "tendrían"], "Si + imperfect subjunctive.", tr="If authors had no protection, many could not live from their work.", lemma="tener:ellos:isubj"),
        F("Si el acceso a los libros ___ más fácil, habría más lectores.", "fuera", ["es", "será", "sería"], "Si + imperfect subjunctive.", tr="If access to books were easier, there would be more readers.", lemma="ser:él:isubj"),
        F("El comercio de libros entre países ___ crecido.", "ha", ["han", "he", "hemos"], "Singular subject.", tr="The book trade between countries has grown.", lemma="haber:él"),
        F("Ojalá nosotros ___ inspirado ya a muchos lectores.", "hayamos", ["hemos", "hayan", "hubiéramos"], "Ojalá + hayamos.", tr="I hope we have inspired many readers.", lemma="haber:nosotros:subj"),
    ],
    verify=[],
)
UNIT = unit("Repaso de la unidad 8", [L864, L865, L866, L867, L868, L869, L870, L871, L872, L873, L874, L875, L876, L877, L878, L879, L880, L881, L882, L883])
