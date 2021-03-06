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
            "bios": "/news-story/8894782-mayor-race-information-for-hamilton-voters/",
            "issues": "/news-story/8975425-what-will-your-mayoral-candidate-do-/",
            "people": [
                # NA http://media.zuza.com/8/8/88762817-369c-472b-83ad-02346de2b733/na.png
                {"name": "Jim Davis", "link": "",
                    "img": "http://media.zuza.com/a/f/af3c8c9b-7010-43df-a2f2-341a81d7c5b2/mayor_candidate_Jim_Davis.jpg"},
                {"name": "Fred Eisenberger*", "link": "https://www.thespec.com/opinion-story/8916986-fred-eisenberger-mayoral-candidate/",
                    "img": "http://media.zuza.com/d/5/d5bf4879-6cc2-492d-b5e9-06e23bcaa44b/mayor_candidate_Fred_Eisenberger.jpg"},
                {"name": "Paul Fromm", "link": "https://www.thespec.com/opinion-story/8959631-paul-fromm-hamilton-mayoral-candidate/",
                    "img": "http://media.zuza.com/7/d/7dc0baaf-81fc-4b82-b61b-2d86fa435fa3/mayor_candidate_Paul_Fromm_Star.jpg"},
                {"name": "Henry Geissler", "link": "https://www.thespec.com/opinion-story/8935620-henry-geissler-candidate-for-hamilton-mayor/", "img": "http://media.zuza.com/b/b/bba0ccbf-5e0e-424c-adf9-fd9231d6d547/mayor_canadidate_Henry_Geissler.jpg"},
                {"name": "Carlos Gomes", "link": "", "img": ""},
                {"name": "Edward Graydon", "link": "",
                    "img": "http://media.zuza.com/0/7/07bb2cc5-c64b-4939-a918-2597ab9e0022/mayor_candidate_Edward_Graydon.jpg"},
                {"name": "Todd May", "link": "", "img": ""},
                {"name": "Michael Pattison", "link": "https://www.thespec.com/opinion-story/8969377-michael-a-pattison-candidate-for-hamilton-mayor/", "img": "http://media.zuza.com/e/3/e3d3ffe1-a1e7-40b1-a2ee-1f3483e1ca7b/B88411555Z.1_20181016151158_000_GO9C4K9S.2-0_Thumbnail.jpg"},
                {"name": "George Rusich", "link": "", "img": "http://media.zuza.com/0/a/0a76cb31-5884-46cf-9ef7-832153e92fa1/mayor_candidate_George_Rusich___300x200.jpg"},
                {"name": "Phil Ryerson", "link": "",
                    "img": "http://media.zuza.com/a/e/ae228af1-457d-4bbb-b1db-8e5e16d5237e/mayor_candidate_Phil_Ryerson.jpg"},
                {"name": "Ute Schmid-Jones", "link": "",
                    "img": "http://media.zuza.com/1/0/10d8eeed-5716-474b-bfa7-b0b73eb94307/mayor_candidate_Ute_Schmid-Jones.jpg"},
                {"name": "Vito Sgro", "link": "https://www.thespec.com/opinion-story/8959620-vito-sgro-hamilton-mayoral-candidate/",
                    "img": "http://media.zuza.com/1/f/1fd6f5be-2ffe-401a-9237-5f2f037f0c3a/mayor_candidate_Vito_Sgro.jpg"},
                {"name": "Ricky Tavares", "link": "", "img": ""},
                {"name": "Mark Wozny", "link": "", "img": ""},
                {"name": "Nathalie Xian Yi Yan", "link": "",
                    "img": "http://media.zuza.com/4/0/4006ae8e-342d-43ef-b71d-3d255da0ec0e/mayor_candidate_Nathalie_Xian_Yi_Yan.jpg"},
            ]
        },
        "wards": [
            {
                "title": "Ward 1",
                "bios": "/news-story/8891703-ward-1-information-for-hamilton-voters/",
                "issues": "/news-story/8907503-ward-1-election-issues/",
                "people": [
                    {"name": "Jason Allen", "link": "https://www.thespec.com/opinion-story/8959625-jason-allen-hamilton-ward-1-candidate/", "img": ""},
                    {"name": "Sharon Anderson", "link": "", "img": ""},
                    {"name": "Syed Bakht", "link": "", "img": ""},
                    {"name": "Sharon Elizabeth Cole", "link": "", "img": ""},
                    {"name": "Ela Eroglu", "link": "", "img": ""},
                    {"name": "Jordan Geertsma", "link": "", "img": ""},
                    {"name": "Sophie Geffros", "link": "", "img": ""},
                    {"name": "Carol E. Lazich", "link": "", "img": ""},
                    {"name": "Richard Massie", "link": "", "img": ""},
                    {"name": "Lyla Miklos", "link": "", "img": ""},
                    {"name": "Linda Narducci", "link": "", "img": ""},
                    {"name": "Harrison White", "link": "", "img": ""},
                    {"name": "Maureen Wilson", "link": "", "img": ""},
                ]
            },
            {
                "title": "Ward 2",
                "bios": "/news-story/8894752-ward-2-information-for-hamilton-voters/",
                "issues": "/news-story/8910104-ward-2-election-issues/",
                "people": [
                    {"name": "Diane Chiarelli", "link": "", "img": ""},
                    {"name": "Jason Farr*", "link": "", "img": ""},
                    {"name": "Cameron Kroetsch", "link": "", "img": ""},
                    {"name": "Nicole Smith", "link": "", "img": ""},
                    {"name": "Mark Tennant", "link": "", "img": ""},
                    {"name": "James Unsworth", "link": "", "img": ""},
                    {"name": "John Vail", "link": "", "img": ""},
                    {"name": "Suresh Venodh Daljeet", "link": "", "img": ""},
                    {"name": "<small>* incumbent</small>"}
                ]
            },
            {
                "title": "Ward 3",
                "bios": "/news-story/8894683-ward-3-information-for-hamilton-voters/",
                "issues": "/news-story/8915451-ward-3-election-issues/",
                "people": [
                    {"name": "Milena Balta", "link": ""},
                    {"name": "Keith Beck", "link": ""},
                    {"name": "Alain Bureau", "link": ""},
                    {"name": "Steven Paul Denault", "link": ""},
                    {"name": "Laura Farr", "link": ""},
                    {"name": "Brendan Kavanaugh", "link": ""},
                    {"name": "Ned Kuruc", "link": ""},
                    {"name": "Tony Lemma", "link": ""},
                    {"name": "Nrinder Nann", "link": ""},
                    {"name": "Stephen Rowe", "link": ""},
                    {"name": "Amanda Salonen", "link": ""},
                    {"name": "Dan Smith", "link": ""},                
                    {"name": "Kristeen Sprague", "link": ""},
                ]
            },
            {
                "title": "Ward 4",
                "bios": "/news-story/8893750-ward-4-information-for-hamilton-voters/",
                "issues": "/news-story/8920382-ward-4-election-issues/",
                "people": [
                    {"name": "Rod Douglas", "link": "", "img": ""},
                    {"name": "Sam Merulla*", "link": "", "img": ""},
                    {"name": "<small>* incumbent</small>"}
                ]
            },
            {
                "title": "Ward 5",
                "bios": "/news-story/8926164-ward-5-election-issues/",
                "issues": "/news-story/8893796-ward-5-information-for-hamilton-voters/",
                "people": [
                    {"name": "Chad Collins*", "link": "", "img": ""},
                    {"name": "Stewart Klazinga", "link": "", "img": ""},
                    {"name": "Juanita Maldonado", "link": "", "img": ""},
                    {"name": "<small>* incumbent</small>"}
                ]
            },
            {
                "title": "Ward 6",
                "bios": "/news-story/8893830-ward-6-information-for-hamilton-voters/",
                "issues": "/news-story/8931216-ward-6-election-issues-rope-rescues-and-high-speed-chases/",
                "people": [
                    {"name": "Tom Jackson*", "link": "", "img": ""},
                    {"name": "Timothy Taylor", "link": "", "img": ""},
                    {"name": "Brad Young", "link": "https://www.thespec.com/opinion-story/8970836-bradley-young-ward-6-candidate-in-hamilton/", "img": ""},
                    {"name": "<small>* incumbent</small>"}
                ]
            },
            {
                "title": "Ward 7",
                "bios": "/news-story/8894617-ward-7-information-for-hamilton-voters/",
                "issues": "/news-story/8936129-ward-7-election-issues/",
                "people": [
                    {"name": "Steve Benson", "link": "", "img": ""},
                    {"name": "Steve Clarke", "link": "", "img": ""},
                    {"name": "Kristopher Clowater", "link": "", "img": ""},
                    {"name": "Adam Dirani", "link": "", "img": ""},
                    {"name": "Karen Grice-Uggenti", "link": "", "img": ""},
                    {"name": "Joseph Kazubek", "link": "", "img": ""},
                    {"name": "Dan MacIntyre", "link": "", "img": ""},
                    {"name": "Jim McColl", "link": "", "img": ""},
                    {"name": "Geraldine McMullen", "link": "https://www.thespec.com/opinion-story/8969410-geraldine-mcmullen-ward-7-council-candidate/", "img": ""},
                    {"name": "Esther Pauls", "link": "", "img": ""},
                    {"name": "Roland Schneider", "link": "", "img": ""},
                ]
            },
            {
                "title": "Ward 8",
                "bios": "/news-story/8894589-ward-8-information-for-hamilton-voters/",
                "issues": "/news-story/8941240-ward-8-election-issues/",
                "people": [
                    {"name": "Eve Adams", "link": "", "img": ""},
                    {"name": "Christopher Climie", "link": "", "img": ""},
                    {"name": "John-Paul Danko", "link": "", "img": ""},
                    {"name": "Steve Ruddick", "link": "", "img": ""},
                    {"name": "Anthony Simpson", "link": "", "img": ""},
                    {"name": "Colleen Wicken", "link": "", "img": ""},
                ]
            },
            {
                "title": "Ward 9",
                "bios": "/news-story/8894196-ward-9-information-for-hamilton-voters/",
                "issues": "/news-story/8946669-ward-9-election-issues/",
                "people": [
                    {"name": "Brad Clark", "link": "", "img": ""},
                    {"name": "Doug Conley*", "link": "", "img": ""},
                    {"name": "David Ford", "link": "", "img": ""},
                    {"name": "Peter Lanza", "link": "", "img": ""},
                    {"name": "Lakhwinder Singh Multani", "link": "", "img": ""},
                    {"name": "<small>* incumbent</small>"}
                ]
            },
            {
                "title": "Ward 10",
                "bios": "/news-story/8894195-ward-10-information-for-hamilton-voters/",
                "issues": "/news-story/8950860-ward-10-election-issues/",
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
                "bios": "/news-story/8894375-ward-11-information-for-hamilton-voters/",
                "issues": "/news-story/8955399-ward-11-election-issues/",
                "people": [
                    {"name": "Brenda Johnson*", "link": ""},
                    {"name": "Waleed Shewayhat", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 12",
                "bios": "/news-story/8894438-ward-12-information-for-hamilton-voters/",
                "issues": "/news-story/8960707-ward-12-election-issues/",
                "people": [
                    {"name": "Mike Bell", "link": "", "img": ""},
                    {"name": "Lloyd Ferguson*", "link": "", "img": ""},
                    {"name": "Kevin Marley", "link": "", "img": ""},
                    {"name": "Miranda Reis", "link": ""},
                    {"name": "John Scime", "link": ""},
                    {"name": "<small>* incumbent</small>", "link": ""}
                ]
            },
            {
                "title": "Ward 13",
                "bios": "/news-story/8894550-ward-13-information-for-hamilton-voters/",
                "issues": "/news-story/8964616-ward-13-election-issues/",
                "people": [
                    {"name": "Gaspare Bonomo"},
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
                "bios": "/news-story/8894506-ward-14-information-for-hamilton-voters/",
                "issues": "/news-story/8970076-ward-14-election-issues/",
                "people": [
                    {"name": "Roslyn French-Sanges", "link": "", "img": ""},
                    {"name": "Robert Iszkula", "link": "", "img": ""},
                    {"name": "Vincent Samuel", "link": "", "img": ""},
                    {"name": "Terry Whitehead*", "link": "", "img": ""},
                    {"name": "Bryan Wilson", "link": "", "img": ""},
                    {"name": "* incumbent", "link": "", "img": ""}
                ]
            },
            {
                "title": "Ward 15",
                "bios": "/news-story/8894395-ward-15-information-for-hamilton-voters/",
                "issues": "/news-story/8974920-ward-15-election-issues/",
                "people": [
                    {"name": "Susan McKechnie", "link": "", "img": ""},
                    {"name": "Judi Partridge*", "link": "", "img": ""},
                    {"name": "* incumbent", "link": "", "img": ""}
                ]
            },
        ],
        "trustees": {
            "hwdsb": ["<b>Ward 1 and 2</b>: Christine Ann Bingham, Rahimuddin Chowdhury", "<b>Ward 3</b>: Chris Parkinson, Jocelynn Vieira, Livia Jones, Gail Tessier, Marlene A.S. Thomas, Maria Felix Miller", "<b>Ward 4</b>: Ray Mulholland", "<b>Ward 5</b>: Jason McLaughlin, Todd White, Carole Paikin Miller", "<b>Ward 6</b>: Jay Edington, Kathy Archer, Eamon O’Donnell", "<b>Ward 7</b>: Dawn Danko", "<b>Ward 8 and 14</b>:, Damin Starr, Rochelle Butler, Erica Villabroza, Becky Buck, Yousaf Malik", "<b>Ward 9 and 10</b>: Wayne Marston, Cam Galindo", "<b>Ward 11 and 12</b>: Blake Hambly, Alex Johnstone, Bruce Carnegie", "<b>Ward 13</b>: Noor Nizam, Sukhi Dhillon, Chris Parr, Paul Tut, Steven James Laur", "<b>Ward 15</b>: Penny Deathe, Janet Creet"
                      ],
            "hwcdsb": ["<b>Ward 1, 2 and 15</b>: Mark Valvasori", "<b>Ward 3 and 4</b>: Anthony Perri", "<b>Ward 5</b>: Aldo D’Intino, Ralph Agostino", "<b>Ward 6</b>: Joseph Baiardo, Ellen Agostino, Elen Ranas", "<b>Ward 7</b>: Patrick J. Daly", "<b>Ward 8 and 14</b>: John Valvasori, George Kalacherry", "<b>Ward 9 and 11</b>: Antonio (Tony) Di Mambro, Karmen Crea, Louis Agro, Tyler Iorio", "<b>Ward 10</b>: Mary Nardini", "<b>Ward 12 and 13</b>: Phil Homerski, Neil Chopp, Olya Lydia Chan"],
            "french": ["<b>Conseil Scolaire Catholique MonAvenir</b>", "Marcel Levesque", "<b>Conseil Scolaire Viamonde</b>", "Pierre Girouard, Denis S. Frawley"]
        }
    },
    # category -> section -> topic -> tags
    #   DNN        'page'     
    "categories": ["municipal election"],
    "sections": ["Hamilton", "Burlington", "Niagara", "Haldimand"],
    "topics": ["mayor", "wards", "school boards"],
    "tags": ["Ward 1", "Ward 2", "Ward 3", "Ward 4", "Ward 5", "Ward 6", "Ward 7", "Ward 8", "Ward 9", "Ward 10", "Ward 11", "Ward 12", "Ward 13", "Ward 14", "Ward 15"]
}

# BY KEYWORD
# http://api.zuza.com/search/article/default?q=KeywordsAlias:”XXXXX"&pageIndex=1&location=hamilton&sort=datedesc&pageSize=5startindex=1&endindex=5
# BY CATEGORY/SUBCATEGORY
# http://api.zuza.com/search/article/default?&category=XXXX&subcategory=XXXX&pageIndex=1&location=hamilton&sort=datedesc&pageSize=10&startindex=1&endindex=10
# BY AUTHOR: where guid: is author page key.
# http://api.zuza.com/search/article/default?guid=25a2fb14-ae69-41f2-beab-bdda47383f93&pageIndex=1&location=hamilton&sort=datedesc&pageSize=15&startindex=1&endindex=5
