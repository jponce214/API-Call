try:
    import os
except ImportError:
    import pip
    pip.main(['install', '--user', 'os'])
    import os

try:
    import requests
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'requests'])
    import requests

# Update Start and End dates here:
start_date = "4/1/2024"
end_date = "6/20/2024"

# This will create the output file in the same folder where this script is saved.
# If this script is saved in your downloads folder, the output file will be
# there as well. 
script_dir = os.path.dirname(os.path.abspath(__file__))
outfile = os.path.join(script_dir, 'API_output.txt')

def main():
    url = # Insert URL Here

    params = {
        "buyer_key": # Buyer Key,
        "start_date": start_date,
        "end_date": end_date,
        "reports": "brands"
        }

    headers = {
     # Any relevant tokens here like token keys, etc
    }

    # Any additional level of detail needed where it'll be easier to create
    # paramenters rather than to write them one by one
    # brand_ids = ['025a484e-bac0-4bed-a1ae-0056e33e1359',
                '4ed644f2-3ff2-441c-adfc-1b26c5a32b95',
                '6c8bcb56-a9bb-4034-af95-35e1a9a3ef38',
                '939c27ac-df9a-4f60-a934-de2503d9e6d1',
                'f63d7126-eff7-4ab7-8a30-a5e83c06ab57']
    
    with open(outfile, 'w', encoding="utf-8") as f:
        for brand_id in brand_ids:
            params['reports'] = brand_id
            response = requests.get(url, headers=headers, params=params)
            f.write(response.text + '\n\n')

    print(os.path.dirname(outfile))

if __name__ == '__main__':
    main()
