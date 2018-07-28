config = {
    # could reduce db name to just project_name.json
    "project_name":
    "muni_elxn",
    "name":
    "spec",
    "db_name":
    "db.json",
    "db_fields_dflt": {
        'desc_user': '',
        'draft_user': 0,  # int 0:published, 1-2: draft
        'rank': 0,  # int
        'rank_time': 0,  # int
        'label_user': '',
        'title_user': '',
        'tags_user': [],  # list of strings
    },
    "db_fields": [
        'asset_id', 'author_api', 'caption_api', 'categories_api', 'label_api',
        'source_api', 'desc_api', 'draft_api', 'link', 'img_api',
        'img_api_thumb', 'pubdate_api', 'region_api', 'site_api', 'tags_api',
        'timestamp', 'title_api'
    ],
    "apis": [
        {
            "url":
            'http://api.zuza.com/search/article/default?&category=news&subcategory=municipal-election&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10',
            "filter": ["searchResultView"]
        },
    ],
    "munge": [],
    "candidates": {
        "mayor": {
            "link": "",
            "people": [
                {"name": "Jim Davis", "link": ""},
                {"name": "Fred Eisenberger*", "link": ""},
                {"name": "Paul Fromm", "link": ""},
                {"name": "Henry Geissler", "link": ""},         
                {"name": "Carlos Gomes", "link": ""},
                {"name": "Edward Graydon", "link": ""},
                {"name": "Todd May", "link": ""},
                {"name": "Michael Pattison", "link": ""},
                {"name": "George Rusich", "link": ""},
                {"name": "Phil Ryerson", "link": ""},
                {"name": "Ute Schmid-Jones", "link": ""},
                {"name": "Vito Sgro", "link": ""},
                {"name": "Ricky Tavares", "link": ""},
                {"name": "Mark Wozny", "link": ""},
                {"name": "Nathalie Xian Yi Yan", "link": ""},
            ]
        },
        "wards": [
            {
                "title": "Ward 1", 
                "link": "", 
                "people": [
                    {"name": "Jason Allen", "link": ""},
                    {"name": "Sharon Anderson", "link": ""},
                    {"name": "Syed Bakht", "link": ""},
                    {"name": "Sharon Elizabeth Cole", "link": ""},
                    {"name": "Ela Eroglu", "link": ""},
                    {"name": "Jordan Geertsma", "link": ""},
                    {"name": "Sophie Geffros", "link": ""},
                    {"name": "Carol E. Lazich", "link": ""},
                    {"name": "Richard Massie", "link": ""},
                    {"name": "Lyla Miklos", "link": ""},
                    {"name": "Linda Narducci", "link": ""},
                    {"name": "Harrison White", "link": ""},
                    {"name": "Maureen Wilson", "link": ""},
                ]
            },
            {
                "title": "Ward 2", 
                "link": "", 
                "people": [
                    {"name": "Diane Chiarelli", "link": ""},
                    {"name": "Jason Farr*", "link": ""},
                    {"name": "Cameron Kroetsch", "link": ""},
                    {"name": "Nicole Smith", "link": ""},
                    {"name": "Mark Tennant", "link": ""},
                    {"name": "James Unsworth", "link": ""},
                    {"name": "John Vail", "link": ""},
                    {"name": "Suresh Venodh Daljeet", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 3", 
                "link": "", 
                "people": [
                    {"name": "Milena Balta", "link": ""},
                    {"name": "Keith Beck", "link": ""},
                    {"name": "Alain Bureau", "link": ""},
                    {"name": "Steven Paul Denault", "link": ""},
                    {"name": "Laura Farr", "link": ""},
                    {"name": "Brendan Kavanaugh", "link": ""},
                    {"name": "Ned Kuruc", "link": ""},
                    {"name": "Tony Lemma", "link": ""},
                    {"name": "Evelyn Myrie", "link": ""},
                    {"name": "Nrinder Nann", "link": ""},
                    {"name": "Stephen Rowe", "link": ""},
                    {"name": "Amanda Salonen", "link": ""},
                    {"name": "Dan Smith", "link": ""},                
                    {"name": "Kristeen Sprague", "link": ""},
                ]
            },
            {
                "title": "Ward 4", 
                "link": "", 
                "people": [
                    {"name": "Rod Douglas", "link": ""},
                    {"name": "Sam Merulla*", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 5", 
                "link": "", 
                "people": [
                    {"name": "Chad Collins*", "link": ""},
                    {"name": "Stewart Klazinga", "link": ""},
                    {"name": "Juanita Maldonado", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 6", 
                "link": "", 
                "people": [
                    {"name": "Tom Jackson*", "link": ""},
                    {"name": "Timothy Taylor", "link": ""},
                    {"name": "Brad Young", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 7", 
                "link": "", 
                "people": [
                    {"name": "Steve Benson", "link": ""},
                    {"name": "Steve Clarke", "link": ""},
                    {"name": "Kristopher Clowater", "link": ""},
                    {"name": "Adam Dirani", "link": ""},
                    {"name": "Karen Grice-Uggenti", "link": ""},
                    {"name": "Joseph Kazubek", "link": ""},
                    {"name": "Dan MacIntyre", "link": ""},
                    {"name": "Jim McColl", "link": ""},
                    {"name": "Geraldine McMullen", "link": ""},
                    {"name": "Esther Pauls", "link": ""},
                    {"name": "Roland Schneider", "link": ""},
                ]
            },
            {
                "title": "Ward 8", 
                "link": "", 
                "people": [
                    {"name": "Eve Adams", "link": ""},
                    {"name": "Christopher Climie", "link": ""},
                    {"name": "John-Paul Danko", "link": ""},
                    {"name": "Steve Ruddick", "link": ""},
                    {"name": "Anthony Simpson", "link": ""},
                    {"name": "Colleen Wicken", "link": ""},
                ]
            },
            {
                "title": "Ward 9", 
                "link": "", 
                "people": [
                    {"name": "Brad Clark", "link": ""},
                    {"name": "Doug Conley*", "link": ""},
                    {"name": "David Ford", "link": ""},
                    {"name": "Peter Lanza", "link": ""},
                    {"name": "Lakhwinder Singh Multani", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 10", 
                "link": "", 
                "people": [
                    {"name": "Jeff Beattie", "link": ""},
                    {"name": "Louie Milojevic", "link": ""},
                    {"name": "Ian Thompson", "link": ""},
                    {"name": "Maria Pearson*", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 11", 
                "link": "", 
                "people": [
                    {"name": "Brenda Johnson*", "link": ""},
                    {"name": "Waleed Shewayhat", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 12", 
                "link": "", 
                "people": [
                    {"name": "Mike Bell", "link": ""},
                    {"name": "Lloyd Ferguson*", "link": ""},
                    {"name": "Kevin Marley", "link": ""},
                    {"name": "Miranda Reis", "link": ""},
                    {"name": "John Scime", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 13", 
                "link": "", 
                "people": [
                    {"name": "Rich Gelder", "link": ""},
                    {"name": "Kevin Gray", "link": ""},
                    {"name": "Pamela Mitchell", "link": ""},
                    {"name": "John Mykytyshyn", "link": ""},
                    {"name": "John Roberts", "link": ""},
                    {"name": "Arlene Vanderbeek*", "link": ""},
                    {"name": "* incumbent", "link": ""}
                ]
            },
            {
                "title": "Ward 14", 
                "link": "", 
                "people": [
                    {"name": "Roslyn French-Sanges", "link": ""},
                    {"name": "Robert Iszkula", "link": ""},
                    {"name": "Vincent Samuel", "link": ""},
                    {"name": "Terry Whitehead*", "link": ""},
                    {"name": "Bryan Wilson", "link": ""},
                    {"name": "* incumbent", "link": ""}
                ]
            },
            {
                "title": "Ward 15", 
                "link": "", 
                "people": [
                    {"name": "Susan McKechnie", "link": ""},
                    {"name": "Judi Partidge*", "link": ""},
                    {"name": "* incumbent", "link": ""}
                ]
            },
        ],
        "trustees": {
            "hwdsb": ["<b>Ward 1 and 2</b>: Christine Ann Bingham, Rahimuddin Chowdhury", "<b>Ward 3</b>: Chris Parkinson, Jocelynn Vieira, Livia Jones, Gail Tessier, Marlene A.S. Thomas, Maria Felix Miller, Steven Paul Denault", "<b>Ward 4</b>: Ray Mulholland", "<b>Ward 5</b>: Jason McLaughlin, Todd White, Carole Paikin Miller", "<b>Ward 6</b>: Jay Edington, Kathy Archer, Eamon O’Donnell", "<b>Ward 7</b>: Dawn Danko", "<b>Ward 8 and 14</b>:, Damin Starr, Rochelle Butler, Erica Villabroza, Becky Buck", "<b>Ward 9 and 10</b>: Wayne Marston", "<b>Ward 11 and 12</b>: Blake Hambly, Alex Johnstone, Bruce Carnegie", "<b>Ward 13</b>: Noor Nizam, Sukhi Dhillon, Chris Parr, Paul Tut, Steven James Laur", "<b>Ward 15</b>: Penny Deathe, Janet Creet"
            ],
            "hwcdsb": ["<b>Ward 1, 2 and 15</b>: Mark Valvasori", "<b>Ward 3 and 4</b>: Anthony Perri", "<b>Ward 5</b>: Aldo D’Intino, Ralph Agostino", "<b>Ward 6</b>: Joseph Baiardo, Ellen Agostino, Elen Ranas", "<b>Ward 7</b>: Patrick J. Daly", "<b>Ward 8 and 14</b>: John Valvasori, George Kalacherry", "<b>Ward 9 and 11</b>: Antonio (Tony) Di Mambro, Karmen Crea, Louis Agro, Tyler Iorio", "<b>Ward 10</b>: Mary Nardini", "<b>Ward 12 and 13</b>: Phil Homerski, Neil Chopp"],
            "french": ["<b>Conseil Scolaire Catholique MonAvenir</b>", "Marcel Levesque", "<b>Conseil Scolaire Viamonde</b>", "Pierre Girouard, Denis S. Frawley"]
        }
    }
}

# BY KEYWORD
# http://api.zuza.com/search/article/default?q=KeywordsAlias:”XXXXX"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5
# BY CATEGORY/SUBCATEGORY
# http://api.zuza.com/search/article/default?&category=XXXX&subcategory=XXXX&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# BY AUTHOR: where guid: is author page key.
# http://api.zuza.com/search/article/default?guid=25a2fb14-ae69-41f2-beab-bdda47383f93&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=5