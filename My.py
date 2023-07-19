from pywidevine import WidevineDecrypt

# Replace these URLs with the actual values
MPD_URL = 'https://bpprod3linear.akamaized.net/bpk-tv/irdeto_com_Channel_365/output/manifest.mpd'
WIDEVINE_LICENSE_URL = 'https://tataplay.live.ott.irdeto.com/Widevine/getlicense?CrmId=tatasky&AccountId=tatasky&ContentId=400000044&ls_session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImNvbnRyb2xfc2lnbmluZ19rZXlfcHJvZHVjdGlvbl8xNjYxMjc5NjMyMDEwIn0.eyJzdWIiOiIxNDI1NjE3NjU5IiwiaXNlIjp0cnVlLCJqdGkiOiI5NGVkNzc0Zi1kZjQxLTQxZjgtODkwZS03MWYzODlhNWYwMTQiLCJhaWQiOiJ0YXRhc2t5IiwiZXhwIjoxNjg5ODQ0NDI0LCJuYW1lIjoidW5kZWZpbmVkIiwiaWF0IjoxNjg5NzU4MDI0LCJlbnQiOlt7ImVwaWQiOiJTdWJzY3JpcHRpb25fQnJvd3Nlcl9TdHJlYW1pbmciLCJiaWQiOiIxMDAwMDAxNTIzIn0seyJlcGlkIjoiU3Vic2NyaXB0aW9uX0Jyb3dzZXJfU3RyZWFtaW5nIiwiYmlkIjoiMTAwMDAwMTAzOCJ9LHsiZXBpZCI6IlN1YnNjcmlwdGlvbl9Ccm93c2VyX1N0cmVhbWluZyIsImJpZCI6IjEwMDAwMDAwMzMifSx7ImVwaWQiOiJTdWJzY3JpcHRpb25fQnJvd3Nlcl9TdHJlYW1pbmciLCJiaWQiOiIxMDAwMDAwMDAyIn0seyJlcGlkIjoiU3Vic2NyaXB0aW9uX0Jyb3dzZXJfU3RyZWFtaW5nIiwiYmlkIjoiMTAwMDAwMTAzNSJ9LHsiZXBpZCI6IlN1YnNjcmlwdGlvbl9Ccm93c2VyX1N0cmVhbWluZyIsImJpZCI6IjEwMDAwMDAwMDEifV0sImNzbW8iOnsibWFzIjoiNiIsImR0IjoidHBtYSIsIm1hc2QiOiIyIn0sImlzcyI6InRwbWFfd2ViIn0.gVqzBS4ftEBLRl-IIsGfDAZUuGoaI8C7IoUVJIbwiVA'

def extract_widevine_keys_from_license(widevine_license_url):
    response = requests.get(widevine_license_url)
    if response.status_code == 200:
        license_data = response.content
        decryptor = WidevineDecrypt()
        keys = decryptor.get_keys(license_data)
        return keys
    else:
        print(f"Failed to fetch Widevine license. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    extracted_keys = extract_widevine_keys_from_license(WIDEVINE_LICENSE_URL)
    if extracted_keys:
        print("Extracted Widevine Keys:")
        for key in extracted_keys:
            print(key)
