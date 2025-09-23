import json

def create_mini_ds(data_file, output_file, num_samples):
    mini_train_data = {"premise": {}, "hypothesis": {}, "label": {}}
    with open(output_file, 'w') as mini_train_ds_file:
        with open(data_file, 'r') as f:
            train_data = json.load(f)
            for key, value in train_data['premise'].items():
                if int(key) < num_samples:
                    mini_train_data['premise'][key] = value
                    mini_train_data['hypothesis'][key] = train_data['hypothesis'][key]
                    mini_train_data['label'][key] = train_data['label'][key]
            json.dump(mini_train_data, mini_train_ds_file, indent=4)


create_mini_ds('dset/train_formatted.json', 'dset/train_mini_ds.json', 2000)
create_mini_ds('dset/test_formatted.json', 'dset/test_mini_ds.json', 200)
create_mini_ds('dset/validation_formatted.json', 'dset/validation_mini_ds.json', 120)
