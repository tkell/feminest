from pyechonest import artist
from names import male_names, female_names


for a in artist.top_hottt(start=0, results=10):
    bios = []
    male_pronoun_count = 0
    female_pronoun_count = 0
    male_name_count = 0
    female_name_count = 0

    bio_data = a.biographies
    for bio in bio_data:
        bios.append(bio['text'])

    for bio in bios:
        bio_list = bio.split(' ')
        bio_list = [word.strip(',./`!@#$%^&*()-_=+|\][{}') for word in bio_list]
        
        pronouns = {'he': 0,
                    'she': 0,
                    'him': 0,
                    'her': 0,
                    'his': 0,
                    'hers': 0,
                    'himself': 0,
                    'herself': 0,
         }
        
        for pronoun in pronouns:
            pronouns[pronoun] = bio_list.count(pronoun)
        male_pronoun_count = male_pronoun_count + pronouns['he'] + pronouns['him'] + pronouns['his'] + pronouns['himself']
        female_pronoun_count = female_pronoun_count + pronouns['she'] + pronouns['her'] + pronouns['hers'] + pronouns['herself']

        for name in male_names(): 
             male_name_count = male_name_count + bio_list.count(name)
        for name in female_names(): 
             female_name_count = female_name_count + bio_list.count(name)
        
    # should probably tweak these to dodge things below 5 or 10?   Or make the whole thing a machine-learning problem?
    print "%s:: male pronoun: %d, female pronoun: %d -- male names: %d, female names: %d" % (a.name, male_pronoun_count, female_pronoun_count, male_name_count, female_name_count)



