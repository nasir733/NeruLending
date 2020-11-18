from urllib.request import urlopen
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from dynamic.models import Subdomain

a = ["Travis Saly",
     "LaPorsha Robinson",
     "Christina gambler",
     "nyra almond",
     "Ashley Stewart",
     "Cornelius cole",
     "Neil Bibbs",
     "Carmen Rosario Castro",
     "Pee Da Don",
     "Sylvens (Dark Wolf) Bellanton",
     "Fred Birks",
     "Camilo Henao",
     "Latesha Everhart",
     "Perry Jeter",
     "Michael Sanchez",
     "Martha charry",
     "Joel Jones",
     "Rodney Doss",
     "Que Royal",
     "Calvin Linton",
     "Roxanne Henderson Washington",
     "Tahnee Mims",
     "Tonisha peebles",
     "Chris Wilkinson",
     "Mary Jane Wilkerson",
     "Reginald Jenkins",
     "Ray Romilla",
     "Tamashia Jones",
     "Tejuan Browder",
     "NeilT urner",
     "Derek S. O'Neal Sr.",
     "Shaneequa Graham",
     "Qazi Mahmood",
     "Andre D Mayfield",
     "Gregg Fluellen",
     "Candace Myrickes",
     "Aaron Howard",
     "maurice h thomas",
     "Rico Darrow Adams",
     "Tracy Michelle Story"
     ]

phns = [
    '14076196961',
    '1(207) 660-8947',
    '16128348703',
    '12563494569',
    '13147414922',
    '19016774764',
    '13138268532',
    '16785366838',
    '14142022466',
    '19513306985',
    '13214052483',
    '12038428134',
    '17175985841',
    '18082241887',
    '19152821575',
    '16308885791',
    '15616290432',
    '17578318463',
    '12039630130',
    '15742100759',
    '14696670310',
    '12512892297',
    '17165803284',
    '18653477969',
    '15045350880',
    '12534780872',
    '9374799762',
    '12298549208',
    '16148169306',
    '17174384906',
    '13372817717',
    '17572380049',
    '17033950155',
    '14043993362',
    '14787463122',
    '17737879850',
    '13174061062',
    '13138787632',
    '16303412098',
    '17064576681',
]

b = [i.split(' ')[0] for i in a]

for i in range(len(b)):
    name = b[i] + " businessbuilders"
    subn = name.replace(" ", '')
    sub = Subdomain(sub_name=subn.lower(),
                    title=name,
                    favicon_title=name,
                    seo_description=name,
                    phno=phns[i])


    gile = 'https://getdinerotodaybucket2.s3.amazonaws.com/documents/22dc7618-4078-4e9d-8f7a-e6c854c0a42d/bcb-removebg-preview.png'
    img_temp = NamedTemporaryFile(delete=True)

    img_temp.write(urlopen(gile).read())
    img_temp.flush()
    sub.logo.save(f"image_{i}.png", File(img_temp))
    sub.save()

