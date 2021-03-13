from writingData import write_json, update_json

write_json({}, filename='register.json')

new_data = [12, 123456]

update_json('register.json', new_data)

new_data2 = [13, 123456]
update_json('register.json', new_data2)