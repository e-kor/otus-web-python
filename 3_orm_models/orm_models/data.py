DB_NAME = 'blog.db'

USER_NAMES = ('Svetlana', 'Vladimir', 'Pavel', 'Alex')
TAG_NAMES = ('whisky', 'vodka', 'beer', 'wine', 'juice', 'water', "rum")

USER_QUERY = 1
TAG_IDS_QUERY = [2, 3]

POSTS_INFO = ({"title": "whisky_wiki",
               "text": "Whisky or whiskey is a type of distilled alcoholic beverage made from fermented grain mash. Various grains (which may be malted) are used for different varieties, including barley, corn, rye, and wheat. Whisky is typically aged in wooden casks, generally made of charred white oak. Whisky is a strictlyregulated spirit worldwide with many classes and types. The typical unifying characteristics of the different classes and types are the fermentation of grains, distillation, and aging in wooden barrels.",
               "user_id": 2,
               "is_published": True,
               "tag_ids": [1, 2, 5]},
              {'title': 'whisky etymology',
               'text': 'The word whisky (or whiskey) is an anglicisation of the Classical Gaelic word uisce (or uisge) meaning "water" (now written as uisce in Modern Irish, and uisge in Scottish Gaelic). Distilled alcohol was known in Latin as aqua vitae ("water of life"). This was translated into Old Irish as uisce beatha ("water of life"), which became uisce beatha in Irish and uisge beatha [ˈɯʃkʲə ˈbɛhə] in Scottish Gaelic. Early forms of the word in English included uskebeaghe (1581), usquebaugh (1610), usquebath (1621), and usquebae (1715).[1]',
               "is_published": False,
               'user_id': 1,
               'tag_ids': [2, 3]},
              {'title': 'whisky history',
               'text': 'The earliest certain chemical distillations were by Greeks in Alexandria in the 1st century AD,[10] but these were not distillations of alcohol. The medieval Arabs adopted the distillation technique of the Alexandrian Greeks, and written records in Arabic begin in the 9th century, but again these were not distillations of alcohol.[10] Distilling technology passed from the medieval Arabs to the medieval Latins, with the earliest records in Latin in the early 12th century.[10][11]',
               "is_published": False,
               'user_id': 1,
               'tag_ids': [1, 3]},
              {'title': 'wine history',
               'text': 'Wine has been produced for thousands of years. The earliest evidence of wine is from Georgia (6000 BC),[1][2][3] Iran (5000 BC),[4] and Sicily (4000 BC).[5] In modern times, the five countries with the largest wine-producing regions are in Italy, Spain, France, the United States, and China.[6]',
               "is_published": False,
               'user_id': 2,
               'tag_ids': [4, 5]},
              {'title': 'wine etymology',
               'text': 'The English word "wine" comes from the Proto-Germanic *winam, an early borrowing from the Latin vinum, "wine" or "(grape) vine", itself derived from the Proto-Indo-European stem *win-o- (cf. Armenian: գինի, gini; Ancient Greek: οἶνος oinos; Aeolic Greek: ϝοῖνος woinos; Hittite: wiyana; Lycian: oino).[43][44][45] The earliest attested terms referring to wine are the Mycenaean Greek 𐀕𐀶𐀺𐄀𐀚𐀺 me-tu-wo ne-wo (*μέθυϝος νέϝῳ),[46][47] meaning "in (the month)" or "(festival) of the new wine", and 𐀺𐀜𐀷𐀴𐀯 wo-no-wa-ti-si,[48] meaning "wine garden", written in Linear B inscriptions.[49][50][51][52] Linear B also includes, inter alia, an ideogram for wine, i.e. 𐂖.',
               "is_published": False,
               'user_id': 2,
               'tag_ids': [1, 3]},
              {'title': 'red wine',
               'text': 'The red-wine production process involves extraction of color and flavor components from the grape skin. Red wine is made from dark-colored grape varieties. The actual color of the wine can range from violet, typical of young wines, through red for mature wines, to brown for older red wines. The juice from most purple grapes is actually greenish-white; the red color comes from anthocyan pigments (also called anthocyanins) present in the skin of the grape; exceptions are the relatively uncommon teinturier varieties, which actually have red flesh and produce red juice.',
               "is_published": False,
               'user_id': 2,
               'tag_ids': [3, 4]},
              {'title': 'rum history',
               'text': 'Rum is a distilled alcoholic drink made by fermenting then distilling sugarcane molasses or sugarcane juice. The distillate, a clear liquid, is usually aged in oak barrels. Most rums are produced in Caribbean and American countries, but also in other sugar producing countries, such as the Philippines and India.[1]',
               "is_published": False,
               'user_id': 1,
               'tag_ids': [1, 2]},
              {'title': 'rum origins',
               'text': 'Another early rum-like drink is brum. Produced by the Malay people, brum dates back thousands of years.[17] Marco Polo also recorded a 14th-century account of a "very good wine of sugar" that was offered to him in the area that became modern-day Iran.[5]',
               "is_published": False,
               'user_id': 2,
               'tag_ids': [3, 5]}
              )
