# rider-api


- Sign Up
```bash
curl  -X POST \
'http://127.0.0.1:8000/app/signup' \
--header 'Accept: */*' \
--header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
--form 'contact_number="456789"' \
--form 'password="123"' \
--form 'name="Shantanu"' \
--form 'aadhaar_card=@c:\Users\Shant\OneDrive\Pictures\ABT33410F98F2E5CCB902A740C7C2A7111F7B34BF0E845D291EFF6E6915E11262C5.jpg'
```

- Update Profile
```bash
curl  -X PUT \
  'http://127.0.0.1:8000/app/update_profile' \
  --header 'Accept: */*' \
  --header 'User-Agent: Thunder Client (https://www.thunderclient.com)' \
  --form 'user_id="5"' \
  --form 'contact_number="456789"' \
  --form 'password="123"' \
  --form 'name="Shantanu"' \
  --form 'aadhaar_card=@c:\Users\Shant\OneDrive\Pictures\ABT33410F98F2E5CCB902A740C7C2A7111F7B34BF0E845D291EFF6E6915E11262C5.jpg'
```